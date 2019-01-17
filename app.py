#from databases import *
from flask import Flask, flash, render_template, url_for, redirect, request
from flask import session as login_session
# from flask.ext.session import Session
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)

