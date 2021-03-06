from flask import Blueprint, render_template, redirect, url_for, request, session
from models.user import User, UserErrors

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route("/register", methods=["GET", "POST"])
def register_user():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        try:
            User.register_user(email, password)
            session["email"] = email
            return email
        except UserErrors.UserError as ex:
            return ex.message
    
    return render_template("users/register.html")


@user_blueprint.route("/login", methods=["GET", "POST"])
def login_user():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        try:
            if User.is_valid_login(email, password):
                session['email'] = email
                return email
        except UserErrors.UserError as ex:
            return ex.message
    
    return render_template("users/login.html")