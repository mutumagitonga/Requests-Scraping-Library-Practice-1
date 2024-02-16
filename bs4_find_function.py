import requests as rq
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"


def fetch_html_data(web_address):
    try:
        print(f"Fetching data from {web_address}...")
        res = rq.get(web_address)  # Getting a webpage
        return res
    except rq.exceptions.RequestException as e:
        print('Stopped:', e)
        return None
    except TypeError as e:
        print('Stopped:', e)
        return None


def convert_web_data_to_beautiful_soup_obj(web_data):
    try:
        print("Creating BeautifulSoup object...")
        # 'lxml' is faster & more lenient HTML parser than bs4 inbuilt 'html.parser'
        soup_obj = BeautifulSoup(web_data.text, "lxml")
        print("Success! BeautifulSoup object created!")
        return soup_obj
    except Exception as e:
        print("Stopped:", e)


response = fetch_html_data(url)  # Fetch web data using requests library
soup = convert_web_data_to_beautiful_soup_obj(response)  # Web data into BeautifulSoup object


def get_price_with_soup_find_function(soup_object):
    price = soup_object.find("h4", {"class": "float-end price card-title pull-right"})
    return price.string


tablet_price_string = get_price_with_soup_find_function(soup)
print(tablet_price_string)
