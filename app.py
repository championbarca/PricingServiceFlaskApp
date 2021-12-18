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

ipad = Item(URL, TAG_NAME, QUERY)
ipad.save_to_mongo()
items_loaded = Item.all()
print(items_loaded)
print(items_loaded[0].load_price())

from models.alert import Alert

alert = Alert("2702b35d761f4cbdb986f7ec73d6c77e", 1200)
alert.save_to_mongo()

