# from flask import Flask
# from learning import learning_blueprint

# app = Flask(__name__)

# app.register_blueprint(learning_blueprint, url_prefix='/greetings')


# if __name__ == "__main__":
#     app.run()

from models.item import Item

URL = f"https://www.johnlewis.com/2021-apple-ipad-pro-12-9-inch-m1-processor-ios-wi-fi-256gb/p5551833"
TAG_NAME = "p"
QUERY = {"class": "price price--large"}

item = Item(URL, TAG_NAME, QUERY)
print(item.load_price())
