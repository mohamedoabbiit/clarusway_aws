from flask import Flask, render_template

app=Flask(__name__)
@app.route("/")
def home():
    abbi="my name is mohamed abbi im doing the AWS classeed to get very nice job soon incha alah "
    return render_template ("index.html", message=abbi)

@app.route("/abbi")
def body():  
    name = ["serdar","Abbi","Mohamed"]
    return render_template ("body.html", object=name)





if __name__==__name__:
    app.run(debug=True)