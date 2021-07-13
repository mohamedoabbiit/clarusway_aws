from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def head():
    return render_template ("index.html", number1=12,number2=15)

@app.route("/sum")    

def sum():
    n1,n2 =12,13
    return render_template ("body.html", val1=n1,val2=n2, val3=n1+n2)
@app.route("/multi") 
def multi():
    n1,n2 =12,13
    return render_template ("body.html", val1=n1,val2=n2, val3=n1*n2)


if __name__==__name__:
    app.run('0.0.0.0', port=80)
   # app.run(debug=True)