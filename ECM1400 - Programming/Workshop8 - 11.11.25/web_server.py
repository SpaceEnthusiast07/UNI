# Import the web server module flask
from flask import Flask, render_template

# Create a flask app with this file as the main entry point
app = Flask(__name__)

# Define the function to be called when the someone visits the homepage
@app.route('/')
def hello():
    return render_template("homepage.html")

# Only run this app if you are running from this file
if __name__ == "__main__":
    app.run()