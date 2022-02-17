#-----posts-----
import json

import requests

class PostDict():
    def __init__(self,d):
        self.__dict__=d

    def __str__(self):
        result=""
        for keys,val in self.__dict__.items():
            result+=f'{keys} ={val} \n'
        return result

def getPost():
    response=requests.get("http://jsonplaceholder.typicode.com/posts")
    if response.status_code//100==2:
        return dict(json.loads(response.content))
    else:
        print(response.status_code,"error \n-please check your connection-")

def findPost(id,post):
    for id in post:
        temp=PostDict(post)
        if temp.id==id:
            return temp
    return 'the id was not found'

user_input=input("please type the post ID:")

post=getPost()
post=findPost(user_input,post)
print(post)

#-----shape-----
class Shape:
    def __init__(self,area,helef):
        self.__area=area
        self.__helef=helef
    def __str__(self):
        return ""

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self,s):
        #if...
        self.__shapes=s

