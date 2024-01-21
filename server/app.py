from flask import Flask, render_template, jsonify, request

app = Flask(
 __name__,
 template_folder="../build/",
 static_folder="../build/static",
)

@app.route("/")
def login():
    return render_template('index.html')

@app.route("/login", methods=["POST"])
def handle_login_get():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(username, password)
        
        if username.isalnum():
            return "<h1>success</h1>"
        return "<h1>invalid login</h1>"

if __name__ == "__main__":
    app.run(port=8000, debug=True)