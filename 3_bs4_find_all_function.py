import requests as req
from bs4 import BeautifulSoup

fetch_url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"


def fetch_html_data(web_address):
    try:
        print(f"Fetching data from {web_address}...")
        res = req.get(web_address)
        return res
    except req.exceptions.RequestException as e:
        print('Stopped:', e)
    except TypeError as e:
        print('Stopped:', e)


def convert_web_data_to_beautiful_soup_obj(web_data):
    try:
        print("\nCreating BeautifulSoup object...")
        soup_obj = BeautifulSoup(web_data.text, "lxml")
        print("Success! Object created!")
        return soup_obj
    except Exception as e:
        print("Stopped:", e)


response = fetch_html_data(fetch_url)
soup = convert_web_data_to_beautiful_soup_obj(response)


def get_all_items_prices(soup_obj):
    print("\nGetting all items' prices...")
    prices = soup.findAll("h4", class_="float-end price card-title pull-right")
    return prices


items_prices = get_all_items_prices(soup)
print(items_prices)  # Array of h4 tags with prices
items_prices_list = [x.text for x in items_prices]  # Only prices into a list (Alt: Use for-loop)
print(items_prices_list)


def get_all_items_descriptions(soup_obj):
    print("\nGetting all items' descriptions...")
    descriptions = soup.findAll("p", class_="description card-text")
    return descriptions


items_descriptions = get_all_items_descriptions(soup)
print(items_descriptions)  # Array of p tags with descriptions
items_descriptions_list = [x.text for x in items_descriptions]  # Only descriptions into a list (Alt: Use for-loop)
print(items_descriptions_list)
