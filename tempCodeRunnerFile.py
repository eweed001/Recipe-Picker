from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests



url = "https://food.ndtv.com/recipe-chawal-ki-kheer-951891"
html_doc = requests.get(url).content
soup = BeautifulSoup(html_doc, 'html.parser')
recipe_container = soup.find("div", {"class": "recp-det-cont"})
name = recipe_container.find('h1').get_text().strip()

recipe_ingredients = recipe_container.find('div', {"class": "ingredients"})
ingredients = [x.get_text().strip()
               for x in recipe_ingredients.find_all('li')]
recipe_method = recipe_container.find('div', {"class": "method"})
instructions = [x.get_text().strip()
                for x in recipe_method.find_all('li')]

print(instructions)