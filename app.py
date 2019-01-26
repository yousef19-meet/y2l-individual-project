from database import *
from flask import Flask, flash, render_template, url_for, redirect, request
from flask import session as login_session
from flask.ext.session import *
import requests,json
app = Flask(__name__)
app.secret_key = "VERY SECRET."
 


########################### HOME ###########################


def search(data):
	return session.query(Post).filter(Post.description.contains(data)).all()
def search(data):
    


############################################################
response = requests.get("https://api-v3.igdb.com/games/4563?fields=url",
  headers={
    "user-key": "f0843654863c9bc9fa6a02e2cd479048"

  }
)

# print(response.content)
parsed_content = json.loads(response.content)
print(parsed_content[0]['url'])

resp = requests.get(parsed_content[0]['url'])
# print(resp.text)

Sresult = resp.text.find('https://images.igdb.com/igdb/image/upload/t_cover_big/')

imgsrc = resp.text[Sresult:Sresult + 78]
######################################################################################

@app.route('/', methods=['GET', 'POST'])
@app.route('/<string:if_post>' ,methods= ['GET','POST'])
def home(if_post="false"):
    if('username' in login_session):
        log = "true"
    else:
        log = "false"

    if request.method == 'GET':
        if if_post == "true":
            return render_template('home.html', if_post = "true",log=log, imgsrc = imgsrc)
        else:
            return render_template('home.html', if_post = "false", log=log, imgsrc = imgsrc)
    else:
        return redirect(url_for('display_result'))
#####################################################################################33

@app.route('/searchResult',methods= ['GET','POST'])
def display_result():
    if('username' in login_session):
        log = "true"
    else:
        log = "false"

    if request.method == 'POST':

        result = request.form['data']  

        matches = search(result)
        if len(matches) == 0:

            flash('No matching results for: '+result)
            return redirect(url_for('home'))
            return render_template('searchResult.html',matches=matches,log=log)
        else:
            no_matches = False
        return render_template('searchResult.html',matches=matches, no_matches=no_matches,log=log)
    else:
        return redirect(url_for('home'))



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
        return redirect(url_for('Login'))
@app.route('/logout')
def logout():
    login_session.clear()
    return redirect(url_for('home'))


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



########################### LOGOUT ###########################


@app.route('/logout')
def logout():
    login_session.clear()
    return redirect(url_for('home'))







##############################################################



