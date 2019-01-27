from model import *
from flask import Flask, flash, render_template, url_for, redirect, request
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

# print([a.username for a in session.query(User).all()])



# response = requests.get("https://api-v3.igdb.com",userkey="f0843654863c9bc9fa6a02e2cd479048")
##################################################################################################
import requests,json


############################################## name ####################################################
# response = requests.get("https://api-v3.igdb.com/games/1942?fields=name",
#   headers={
#     "user-key": "f0843654863c9bc9fa6a02e2cd479048"

#   }
# )
# print (response.content)
# ############################################## slug/keyword ####################################################
# SLUG_response = requests.get("https://api-v3.igdb.com/games/1942?fields=slug",
#   headers={
#     "user-key": "f0843654863c9bc9fa6a02e2cd479048"
#   }
# )
# print (SLUG_response.content)4

# ############################################## sotryline ####################################################
# STORYLINE_response = requests.get("https://api-v3.igdb.com/games/1942?fields=storyline",
#   headers={
#     "user-key": "f0843654863c9bc9fa6a02e2cd479048"
#   }
# )
# print (STORYLINE_response.content)

# url = "https://api-v3.igdb.com/games/?search=" + "l" + "&fields=id,name"
# print("-------------------")
# print("URL",url)
# RATING_response = requests.get(url,
#   headers={
#   "user-key": "f0843654863c9bc9fa6a02e2cd479048"
#   }
# )
# final_response = RATING_response.content
# print(final_response)
# # ############################################# summary ####################################################
# SUMMARY_response = requests.get("https://api-v3.igdb.com/games/count?fields=summary",
#   headers={
#     "user-key": "f0843654863c9bc9fa6a02e2cd479048"
#   }
# )
# print (SUMMARY_response.content)

# ##############################################################################################################################
# # # print(response.content)
# parsed_content = json.loads(response.content)
# print(parsed_content[0]['url'])
# resp = requests.get(parsed_content[0]['url'])
# # print(resp.text)
# Sresult = resp.text.find('https://images.igdb.com/igdb/image/upload/t_cover_big/')
# print(resp.text[Sresult:Sresult + 78])
# print (response.content)
# from igdb_api_python.igdb import igdb
# igdb = igdb("f0843654863c9bc9fa6a02e2cd479048")
# result = igdb.games(1)
# for game in result.body:
#     print("Retrieved: " + game["name"])