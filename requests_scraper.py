import requests as rq
from bs4 import BeautifulSoup as bs

url = "https://courses.wscubetech.com/"
faulty_url = "https://courses.wscubetech.comm/"

# Getting a webpage
try:
    res = rq.get(url)
    print(res.status_code)  # Show HTTP Status code
    print(res.text)  # Show webpage content (HTML of the page)
except rq.exceptions.ConnectionError as e:
    print('An error occurred:', e)

# Parse returned HTML resource using BeautifulSoup library