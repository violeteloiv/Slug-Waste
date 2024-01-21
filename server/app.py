from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

# Import table definitions + SQLAlchemy instance
from tables import *

# Import random library for dummy data
import random

app = Flask(
 __name__,
 template_folder="../build/",
 static_folder="../build/static",
)

# Standard messages
error_header = "<h1>something went wrong :(\n"
error_text = "<p>Please try again!</p>"


# Creating a database file if it does not exist
db_name = 'database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

# Test if database connection is working
def test_database():
    try:
        db.session.query(text("1")).from_statement(text("SELECT 1")).all()
        return True
    except Exception as e:
        return False

def dummy_data():
    times = ['B', 'L', 'D'] # meal time options

    all_loc_elements = DiningHalls.query.all()
    loc = [e.dh_name for e in all_loc_elements]
    print(loc)

    all_meal_elements = Meals.query.all()
    all_meals = [e.meal_name for e in all_meal_elements]
    print(all_meals)

    # randomize user meals and dining hall waste
    num_random_data = 150
    last_meal_id = UserMeals.query.count()
    for i in range(last_meal_id + 1, last_meal_id + 1 + num_random_data):
        dh = random.choice(loc)
        db.session.add(UserMeals(
            user_id=1,
            meal_id=i,      # increments as UserMeals instance
            location=dh,
            meal_time=random.choice(times),
            meal_served= random.choice(all_meals)
        ))

    # put into the database
    db.session.commit()

@app.route("/")
def login():
    if not test_database():
        return error_header + error_text

    # One-time create all tables (internally will not duplicate)
    with app.app_context():
        db.create_all()
    initalize_dim_tables()

    return render_template('index.html')

# POST from login
@app.route("/login", methods=["POST"])
def handle_login_get():
    if request.method == "POST":
        try_username = request.form["username"]
        try_password = request.form["password"]

        print(try_username, try_password)

        user = Users.query.filter_by(username=try_username).first()
        if user is not None:
            if not user.password == try_password:
                return error_header + error_text
        else:
            # user did not exist, should lead to a registration page>
            return "<h1>pls register:))</h1>"
        
        if try_username.isalnum():
            dummy_data()
            return "<h1>success</h1>"
        
        return "<h1>invalid login</h1>"

if __name__ == "__main__":
    app.run(port=8000, debug=True)