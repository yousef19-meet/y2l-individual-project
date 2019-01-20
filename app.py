from database import *
from flask import Flask, flash, render_template, url_for, redirect, request
from flask import session as login_session
#from flask.ext.session import Session
app = Flask(__name__)
app.secret_key = "VERY SECRET."
 
@app.route('/')
def home():
    return render_template("home.html")



########################### SIGNUP ###########################
@app.route('/signup',methods= ['GET','POST'])
def SignUp ():
    if('username' in login_session):
        log = "true"
    else:
        log = "false"
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        print('its working')
        try:
            
            user = request.form['user']
            password = request.form['password']

        except:
            return render_template("signup.html", error="u r bad")
        print(user,password)
        add_student(user,password)
        return redirect(url_for('home'))
@app.route('/logout')
def logout():
    return "hello"



########################### LOGIN ###########################


@app.route('/login',methods= ['GET','POST'])
def Login():
    log = 0
    if('username' in login_session):
        log = "true"
    else:
        log = "false"
    print(log)
    if request.method == 'GET':
        return render_template('login.html',log=log)
    else:
        user = request.form['username']
        password = request.form['password']
        if check_account(user,password):
            login_session['logged_in'] = True
            login_session['username'] = request.form['username']

            # return redirect(url_for('show_prof',username=user))
            return redirect(url_for('home',log=log))

        else:
            return render_template('login.html', error = "username or password are not correct!")
if __name__ == '__main__':
    app.run(debug=True)