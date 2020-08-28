from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from pip._vendor import requests
import os
import sys


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

instructions_str = ','.join(instructions).encode()
# print(instructions)

data = [{'Title': name, 'Ingredients': ingredients, 'Instructions': instructions}]
df = pd.DataFrame(data, columns=['Title', 'Ingredients', 'Instructions'])

fd = os.open("test.txt", os.O_RDWR | os.O_CREAT)
os.write(fd, instructions_str)
os.close(fd)
print("closed file")

np.savetxt('df.txt', df.values, fmt='%s', delimiter=',')
