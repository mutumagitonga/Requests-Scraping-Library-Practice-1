import requests as rq
from bs4 import BeautifulSoup

url = "https://courses.wscubetech.com/"
faulty_url = "https://courses.wscubetech.comm/"
unavail_url = "our-site.webflow.io/does-not-exist"

res = None  # Initialize res in global scope (use outside try-except) with a default value

try:
    print("Fetching data from URL...")
    res = rq.get(url)  # Getting a webpage
    # print(res.status_code)  # Show HTTP Status code
    # print(res.text)  # Show webpage content (HTML of the page)
except rq.exceptions.RequestException as e:
    print('Stopped:', e)
except TypeError as e:
    print('Stopped:', e)

# Parse returned HTML resource using BeautifulSoup library
if res:
    print("Data received successfully! Creating a BeautifulSoup object...")
    # 'lxml' is faster & more lenient HTML parser than bs4 inbuilt 'html.parser'
    soup = BeautifulSoup(res.text, "lxml")
    print("Success! BeautifulSoup object created!")
else:
    print("BeautifulSoup can't run, response received:", res)
