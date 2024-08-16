# imported the Flask class; instance of this class will be the app
from flask import Flask
from flask import render_template
from utils import calculate_sir_model
app = Flask(__name__)

#Decorate a view function to register it with the given URL rule and options.


# this will take to the main page
@app.route("/")
def hello_world():
  return render_template('model.html')


@app.route("/about")
def about_page():
  return "<h1>This is my about page<h1>"
