from flask import Flask, render_template, jsonify, request, redirect, send_from_directory
from sqlalchemy.sql import text

import os

# Import table definitions + SQLAlchemy instance
from tables import *


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
def handle_login():
    if request.method == "POST":
        try_username = request.form["username"]
        try_password = request.form["password"]

        # these keywords need a space after them so we know it's not part of an actual password
        bad_sqls = ["drop ", "delete ", "update ", "create ", "truncate ", "insert ", "select "]
        lower_pass = try_password.lower()
        for injection in bad_sqls:
            if injection in lower_pass:
                return "<h1>sql injection is a no no! >:(</h1>"

        user = Users.query.filter_by(username=try_username).first()
        if user is not None and len(try_password):
            if len(try_password) and not user.password == try_password:
                return error_header + error_text
            else:
                dummy_data()
                return redirect("/submission")
        else:
            # user did not exist, should lead to a registration page>
            return "<h1>pls register:))</h1>"
    
    return "<h1>invalid login</h1>"

# redundancies to push back to react router for redirects
@app.route('/sub-path',  defaults={'path': 'index.html'})
@app.route('/sub-path/<path:path>')
def index(path):
    return send_from_directory('../build', path)

@app.errorhandler(404)
def not_found(e):
  return send_from_directory('../build','index.html')

if __name__ == "__main__":
    app.run(port=8000, debug=True)