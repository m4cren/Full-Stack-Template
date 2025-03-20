


from .extensions import db
from dotenv import load_dotenv
import urllib
import os

load_dotenv()

host = os.getenv('HOST')
schema = os.getenv('SCHEMA')
username = os.getenv('USERNAME_DB')
password = urllib.parse.quote(os.getenv("PASSWORD", ""))
port = os.getenv('PORT')

print(password, username)


def save_data(data):

    try:
        db.session.add(data)
        db.session.commit()

        return "success"
    except:
        db.session.rollback()
        return "failed"



def delete_data(data):

    try:
        db.session.delete(data)
        db.session.commit()

        return "success"
    except:
        db.session.rollback()
        return "failed"



def delete_all_data(data):

    try:
        for x in data:
            db.session.delete(x)
        db.session.commit()

        return "success"
    except:
        db.session.rollback()
        return "failed"
