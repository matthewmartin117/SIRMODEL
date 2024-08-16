# imported the Flask class; instance of this class will be the app
from flask import Flask,render_template,request,jsonify,send_file
from .utils import calculate_sir_model
from io import BytesIO
app = Flask(__name__)

#Decorate a view function to register it with the given URL rule and options.


# this will take to the main page
@app.route("/")
def hello_world():
  return render_template('model.html')

# submit url
@app.route("/submit", methods=['POST'])
def handle_form():
   data = request.get_json()  # Get JSON data from the request
    # Process the data (for example, print it to the console)
   print('Received data:', data)

   # assign the data to variables
   S = float(data.get('S'))
   I = float(data.get('I'))
   R = float(data.get('R'))

   img_io = calculate_sir_model(S, I, R, 0.0001786, 14, 60, 30)

  # Save the plot to a BytesIO object and send it as a response
  #

   return send_file(img_io, mimetype='image/png')



@app.route("/about")
def about_page():
  return "<h1>This is my about page<h1>"


if __name__ == "__main__":
    app.run(debug=True)