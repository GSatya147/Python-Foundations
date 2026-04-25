# REQUESTS library
"""
reuirements: pip install requests
"""

import requests

r = requests.get('https://google.com/')

# print(help(r)) # attributes & methods info

print(r) # gives status code 
print(r.text) # gives html of that page, or JSON depends
print(r.content) # gives content of the r, gives byte information if r is an image or relevant content

# Use case: To save a local copy of a live png
r = requests.get('https://img.freepik.com/free-photo/closeup-shot-beautiful-butterfly-with-interesting-textures-orange-petaled-flower_181624-7640.jpg?semt=ais_hybrid&w=740&q=80')

with open('copy.jpg', 'wb') as wf: # binary write mode to handle img file
    wf.write(r.content) # r.content has bytes of jpg

"""
Status codes:
200s - success
300s - redirects
400s - client errors
500s - server errors
"""
print(r.status_code) # 200
print(r.ok) # True, for < 400 codes

print(r.headers) # useful info regarding the url

# To play with requests & response service use httpbin which was built by father of requests library
# Different queries can be tested with httpbin.org, like GET, POST, DELETE, PUT, redirects, auth etc..

# ---------------------------------------------------------------------------------------------------------------
# Use case to use GET on a url which has some parameters, hard coding them gonna be error proned
# eg url: https://httpbin,org/get?page=2&count=25, can hardcode in get but use a dict args instead

payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbin.org/get', param = payload)

print(r.text) # returns a JSON from the server with all the info
print(r.url) # https://httpbin,org/get?page=2&count=25

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Use case - To post smtg on a route or to post a form data on a route
data = {'username': 'satya', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data = data)

print(r.text) # returns a JSON like forms, headers etc...

# since a JSON is returned, we can play with JSON as we like
r_dict = r.json() # r.json() method returns a dict of the JSON returned from the url

print(r_dict['form']) # form key has our data dict

# same for pull but with requests.pull()

# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Basic auth using get and httpbin.org

"""
https://httpbin.org/baisc-auth/satya/testing, this will prompt for username and password
entering 'satya' as username, 'testing' as password will trigger basic credential check, will return True, in browser
"""

# replicating browser auth in py script using requests get
r = requests.get('https://httpbin.org/basic-auth/satya/testing/', auth = ('satya', 'testing'), timeout = 3) # check between auth tuple and url, timeout after 3 secs

print(r) # 200 is true
print(r.text) # JSON, True

# if auth fails 
print(r) # 401
print(r.text) # JSON, False

#-------------------------------------------------------------------------------------------------------------------------------------------------------
# 'httpbin.org/delay/4' gives a response after exactly 4 secs, can play with our own timeout

r = requests.get('https://httpbin.org/delay/6', timeout = 3) # since url responds after 6 secs, we are timing out before response

print(r) # exception, timeout

# useeful when a site is broken, timeout essentially just leaves after a defined time giving us an idea of url health in our own app
# uless an API is doing significant computations like an LLM response, timeout should be low to ensure UX