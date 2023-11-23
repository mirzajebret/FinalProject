import os
from config import db
from models import Wish
from app import connex_app

# Data to initialize database with
WISHLIST = [
    {'title': 'FoodTrip', 'desc': '1'},
    {'title': 'WebDev', 'desc': '2'},
    {'title': 'Own A House','desc': '3'},
    {'title': 'Japan Trip','desc': '4'}
]

if os.path.exists('wishlist.db'):
    os.remove('wishlist.db')


with connex_app.app.app_context():
    db.create_all()

    for wish in WISHLIST:
        p = Wish(desc=wish['desc'], title=wish['title'])
        db.session.add(p)

    db.session.commit() 