from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/1")
def main():
    return render_template("../templates/screens/main.html")

@app.route("/2")
def color():
    return render_template("color.html")

if __name__ == "__main__":
    app.run(debug=True)