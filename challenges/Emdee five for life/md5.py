#!/usr/bin/python
import requests
import hashlib

#Set the lab url
url="http://docker.hackthebox.eu:30229"

#Create session
s = requests.Session()

#Get the page with the token
response=s.get(url)

#Parse and obtain token
token=response.text.split("<h3 align='center'>")[1].split("</h3>")[0]

#Hash it
hasheado=hashlib.md5(token).hexdigest()

#Prepare body
preparo={"hash": hasheado}

#Send post with hashed token
response2=s.post(url,data=preparo)

#Print response with flag
print response2.text.split("<p align='center'>")[1].split("</p>")[0]


