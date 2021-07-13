from flask import Flask,redirect, url_for,render_template

app=Flask(__name__)
@app.route("/")
def home():
    return " Home page "


@app.route("/second")
def second():
    return " this the second page  "    

@app.route("/about")
def aboutme():
    return " this is about me page will give more information about mohgamed abbi   " 


@app.route("/forth/<string:id>")
def ide(id):
    return f" the page id of this page is {id} "

if __name__==__name__:
    app.run('0.0.0.0', port=80)
   # app.run(debug=True)