import requests as req
from bs4 import BeautifulSoup


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

