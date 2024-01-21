from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, String, CHAR

db = SQLAlchemy()

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String)

class DiningHalls(db.Model):
    dh_name = db.Column(db.String, primary_key=True)
    num_compost = db.Column(db.Integer)
    num_trash = db.Column(db.Integer)

# One-dimensional list of dining hall options
class Meals(db.Model):
    meal_name = db.Column(db.String, primary_key=True)

# Table of user meals with id, location, and meal ate
class UserMeals(db.Model):
    user_id = db.Column(db.Integer, ForeignKey("users.user_id"))
    meal_id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String, ForeignKey("dining_halls.dh_name"))
    meal_time = db.Column(db.CHAR)  # 'B', 'L', 'D'
    meal_served = db.Column(db.String, ForeignKey("meals.meal_name"))

# Populate known data, but only once
def initalize_dim_tables():
    if not Users.query.get(1):
        db.session.add(Users(user_id=1, username="debug", password="123"))

    dhs = ["9/10", "Co/St", "Cr/Me", "Po/Kr", "Oa/RCC"]
    for dh in dhs:
        if not DiningHalls.query.get(dh):
            db.session.add(DiningHalls(dh_name=dh, num_compost=3, num_trash=3))

    meal_options = ["French Toast Sticks", "Mac and Cheese Bar", "Baked Potato Bar", "Taqueria Bar", "Baja Taco Bar",
                    "Cajun Bayou Bar", "Scrambled Eggs", "Bacon", "Buttermilk Pancakes", "Pho Noodle Bar"]
    for meal in meal_options:
        if not Meals.query.get(meal):
            db.session.add(Meals(meal_name=meal))

    db.session.commit()
