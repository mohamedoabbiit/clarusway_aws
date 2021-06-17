from flask import Flask
from flask.templating import render_template
app= Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html", number1=12, number2=15)


@app.route('/sum')
def sum():
    num1,num2=20,15
    return render_template ("body.html", val1=num1, val2=num2, val3=num2+num1)


if __name__ == "__main__":

    app.run(host='0.0.0.0',port=80)

    #app.run(debug=True)