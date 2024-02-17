import requests_and_beautiful_soup_utils as rq_soup
import re

fetch_url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
response = rq_soup.fetch_html_data(fetch_url)
soup = rq_soup.convert_web_data_to_beautiful_soup_obj(response)

