# from flask import Blueprint

# learning_blueprint = Blueprint("learning", __name__)


# @learning_blueprint.route('/<string:name>')
# def home(name):
#     return f"Hello, {name}!!!"

from common.Database import Database

alerts = Database.find("alerts", {})
item = Database.find_one("items", {"_id": alerts[0]["item_id"]})
print(item["url"])

