# Import Flask modules
from flask import Flask
import flask
from flask.templating import render_template
# Create an object named app
app=flask(__name__)
# Create a function named `index` which uses template file named `index.html` 
# send three numbers as template variable to the app.py and assign route of no path ('/') 
@app.route('/')
def index():
    
# calculate sum of them using inline function in app.py, then sent the result to the 
# "number.hmtl" file and assign route of path ('/total'). 
# When the user comes directly "/total" path, "Since this is GET 
# request, Total hasn't been calculated" string returns to them with "number.html" file


# Add a statement to run the Flask application which can be debugged.
if __name__=="__main__":
    app.run(debug=True)