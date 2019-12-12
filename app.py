from flask import Flask, render_template, request, redirect, url_for

import os

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/manager')
def manager():
    return render_template("manager.html")

@app.route('/inventory')
def inventory():
    return render_template("inventory.html")

@app.route('/joblist')
def jobList():
    return render_template("jobList.html")

@app.route('/newUser')
def newUser():
    return render_template("newUser.html")



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
