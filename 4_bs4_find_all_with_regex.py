import requests_and_beautiful_soup_utils as rq_soup
import re

fetch_url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
response = rq_soup.fetch_html_data(fetch_url)
soup = rq_soup.convert_web_data_to_beautiful_soup_obj(response)


def get_data_from_several_tags_once(soup_obj):
    print("\nGetting data from several tags at once...")
    mixed_tag_data = soup_obj.find_all(['h4', 'p', 'a'])
    return mixed_tag_data


several_tags_data = get_data_from_several_tags_once(soup)
print(several_tags_data)


def get_all_items_sharing_same_word_in_fullname(soup_obj):
    print("\nGetting data from items sharing a word in their fullname...")
    galaxy_tabs = soup_obj.find_all(string=re.compile("Galaxy"))  # Return all tabs with "Galaxy" as part of their names
    return galaxy_tabs


all_galaxy_tabs = get_all_items_sharing_same_word_in_fullname(soup)
print(all_galaxy_tabs)
