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
        print("\nCreating BeautifulSoup object...")
        # 'lxml' is faster & more lenient HTML parser than bs4 inbuilt 'html.parser'
        soup_obj = BeautifulSoup(web_data.text, "lxml")
        print("Success! BeautifulSoup object created!")
        return soup_obj
    except Exception as e:
        print("Stopped:", e)


response = fetch_html_data(url)  # Fetch web data using requests library
soup = convert_web_data_to_beautiful_soup_obj(response)  # Web data into BeautifulSoup object


def get_item_title_with_soup_find_function(soup_object):
    print("\nGetting item title...")
    try:
        item_name = soup_object.find("a", class_="title")
        return item_name.string
    except Exception as e:
        print("Stopped: ", e)


item_name_string = get_item_title_with_soup_find_function(soup)
print(f"Item name: {item_name_string}")


def get_item_price_with_soup_find_function(soup_object):
    print("\nGetting item price...")
    try:
        item_price = soup_object.find("h4", {"class": "float-end price card-title pull-right"})
        return item_price.string
    except Exception as e:
        print("Stopped: ", e)


item_price_string = get_item_price_with_soup_find_function(soup)  # Return item price as str
print(f"Item price: {item_price_string}")


def get_item_description_with_soup_find_function(soup_object):
    print("\nGetting item description...")
    try:
        item_description = soup_object.find("p", {"class": "description card-text"})
        return item_description.string
    except Exception as e:
        print("Stopped: ", e)


item_description_string = get_item_description_with_soup_find_function(soup)
print(f"Item description: {item_description_string}")


# BeautifulSoup find() only finds the data from the first tags it encounters...
# ...Leaving tags with similar tags ignored. Hence can't scrape all items with similar tags
