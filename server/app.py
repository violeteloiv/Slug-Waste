from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(
 __name__,
 template_folder="../build/",
 static_folder="../build/static",
)

# Standard messages
error_header = "<h1>something went wrong :("
error_text = "The following error was produced:"

# Creating a database file if it does not exist
db = SQLAlchemy()
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

    return render_template('index.html')

# POST from login
@app.route("/login", methods=["POST"])
def handle_login_get():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(username, password)
        return "<h1>success</h1>"

if __name__ == "__main__":
    app.run(port=8000, debug=True)