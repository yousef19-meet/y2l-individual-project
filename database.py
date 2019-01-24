from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db', connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def function(parameter):
    pass

def check_account(user,password):
    if session.query(User).filter_by(username=user).first() != None and session.query(User).filter_by(username=user).first().password == password:
        return True
    else:
        return False

def add_student(user,password):
    new_user= User(username = user, password= password) 
    session.add(new_user)
    session.commit()

print([a.username for a in session.query(User).all()])


import requests
# response = requests.get("https://api-v3.igdb.com",userkey="f0843654863c9bc9fa6a02e2cd479048")

response = requests.get("https://api-v3.igdb.com/games/",
  headers={
    "user-key": "f0843654863c9bc9fa6a02e2cd479048"
  }
)
print (response.content)

# from igdb_api_python.igdb import igdb

# igdb = igdb("f0843654863c9bc9fa6a02e2cd479048")
# result = igdb.games(1)

# for game in result.body:
#     print("Retrieved: " + game["name"])