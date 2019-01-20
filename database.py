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