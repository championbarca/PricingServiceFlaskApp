import os
from typing import List
from requests import Response, post


class MailgunException(Exception):
    def __init__(self, message: str):
        self.message = message

class Mailgun:
    MAILGUN_API_KEY = "6d94224bb487de1f8518cfecf73f5c99-1831c31e-19dfe769" #os.environ.get("MAILGUN_API_KEY", None)
    MAILGUN_DOMAIN = "https://api.mailgun.net/v3/sandbox4dc5a208821a47d29fd8b47cdca9ffbe.mailgun.org" #os.environ.get("MAILGUN_DOMAIN", None)

    FROM_TITLE = "Pricing Service"
    FROM_EMAIL= "do-not-reply@sandbox4dc5a208821a47d29fd8b47cdca9ffbe.mailgun.org"
    @classmethod
    def send_mail(cls, email:List[str], subject:str, text:str, html:str)->Response:
        if cls.MAILGUN_API_KEY is None:
            raise MailgunException("Failed to load Mailgun API Key")
        
        if cls.MAILGUN_DOMAIN is None:
            raise MailgunException("Failed to load Mailgin domain")

        res = post(f"{cls.MAILGUN_DOMAIN}/messages",
        auth=("api", f"{cls.MAILGUN_API_KEY}"),
        data={"from": f"{cls.FROM_TITLE} <{cls.FROM_EMAIL}>",
        "to": email, 
        "subject": subject, 
        "text": text,
        "html": html})

        if res.status_code != 200:
            print(res.json())
            raise MailgunException("An error occurred while sending e-mail.")
        return res

# Mailgun.send_mail(
#     ["admin@tradingwheel.in"],
#     "Hello",
#     "This is a test",
#     "<p>This is a HTML test.</p>"
# )