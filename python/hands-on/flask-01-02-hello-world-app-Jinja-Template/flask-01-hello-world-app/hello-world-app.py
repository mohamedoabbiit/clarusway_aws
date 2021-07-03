from flask import Flask


app= Flask(__name__)
@app.route('/')

def hello() :
    return "hello world"

@app.route('/second')

def second():
    return "This is second page"    

@app.route('/third/subthird')

def third():
    return "This is subpage of third page"

if __name__=="__main__":

    app.run(host='0.0.0.0',port=80)
   # app.run(debug=True)
