import requests as rq
from bs4 import BeautifulSoup

url = "https://courses.wscubetech.com/"
faulty_url = "https://courses.wscubetech.comm/"
unavail_url = "our-site.webflow.io/does-not-exist"

url_test_commerce_site_1 = "https://webscraper.io/test-sites/e-commerce/allinone/computers"

res = None  # Initialize res in global scope (use outside try-except) with a default value

try:
    print(f"Fetching data from:\n{url_test_commerce_site_1}...")
    res = rq.get(url_test_commerce_site_1)  # Getting a webpage
    # print(res.status_code)  # Show HTTP Status code
    # print(res.text)  # Show webpage content (HTML of the page)
except rq.exceptions.RequestException as e:
    print('Stopped:', e)
except TypeError as e:
    print('Stopped:', e)
# READ MORE ON EMPLOYING THESE EXCEPTIONS


# Parse returned HTML resource using BeautifulSoup library
soup = None  # Declare & initialize BeautifulSoup object variable in global scope
if res:
    print("Data received successfully! Creating a BeautifulSoup object...")
    # 'lxml' is faster & more lenient HTML parser than bs4 inbuilt 'html.parser'
    soup = BeautifulSoup(res.text, "lxml")
    print("Success! BeautifulSoup object created!")
else:
    print("BeautifulSoup can't run, response received:", res)

# Understanding HTML attributes within tags
header_tag = soup.header  # Access header tag
header_tag_attrs = header_tag.attrs  # Access header tag attributes
print(header_tag_attrs['role'])


