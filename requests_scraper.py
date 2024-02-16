import requests as rq

url = "https://courses.wscubetech.com/"
faulty_url = "https://courses.wscubetech.comm/"

# Getting a webpage
try:
    res = rq.get(faulty_url)
    print(res.status_code)
except rq.exceptions.ConnectionError as e:
    print('An error occurred:', e)

