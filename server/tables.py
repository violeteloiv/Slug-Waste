from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, String, CHAR

db = SQLAlchemy()

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String)

# One-dimensional list of dining hall options
class Meals(db.Model):
    meal_name = db.Column(db.String, primary_key=True)

# Table of user meals with id, location, and meal ate
class UserMeals(db.Model):
    user_id = db.Column(db.Integer, ForeignKey("users.user_id"))
    meal_id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String)
    meal_time = db.Column(db.CHAR)  # 'B', 'L', 'D'
    meal_served = db.Column(db.String, ForeignKey("meals.meal_name"))

class DiningHalls(db.Model):
    dh_name = db.Column(db.Integer, primary_key=True)


# Populate known data
def initalize_dim_tables():
    if not Users.query.get(1):
        db.session.add(Users(user_id=1, username="debug", password="123"))


    db.session.commit()
