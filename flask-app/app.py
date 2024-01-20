from flask import Flask, render_template, jsonify

app = Flask(
 __name__,
 template_folder="./templates",
 static_folder="./static",
)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/json")
def json_response():
    response = {"name": "Pratap", "age": 24}
    return jsonify([response])

if __name__ == "__main__":
    app.run(port=8000, debug=True)