# -*- coding: utf-8 -*-
from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests

#Create a Connection 
client = MongoClient("182.254.154.191:27017")

# if the database exist
# print(client.database_names()) 

#Access Database Objects
db = client.local

# if the collection exist
# print(db.collection_names())

#Access Collection Objects
coll = db.test

#Start Query 
#cursor = coll.find({"borough": "Manhattan","address.zipcode": "10075"})

#set url 
url = 'http://www.mzitu.com/all'

#use requests to get the html
response = requests.get(url).content

#use BeautifulSoup to deal with it 
soup = BeautifulSoup(response, 'html.parser')

print(soup.prettify())
