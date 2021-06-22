# Import Flask modules
from os import name
from flask import Flask
from flask.templating import render_template
# Create an object named app 
app=Flask(__name__)
# Create a function named head which shows the massage as "This is my first conditions experience" in `index.html` 
# and assign to the route of ('/')
@app.route('/')
def head():
    first="this is my first condition experience"
    return render_template('index.html', message=first)

# Create a function named header which prints numbers from 1 to 10 one by one in `index.html` 
# and assign to the route of ('/')
app.route('/mohamed')
def header():
    names =['abbi','hiba','omer','mohamed','aicha']
    return render_template('body.html', object=names)
# run this app in debug mode on your local.
if __name__=="__main__":
    app.run(debug=True)