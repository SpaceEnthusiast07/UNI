from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "This is the home page"

@app.route("/about")
def AboutPage():
    return "This is the about page"

if __name__ == "__main__":
    app.run()