# Main mehtod for scraping recipes

import os
from bs4 import BeautifulSoup
import csv
import food
import foodnetwork
import delish


# Opens 'recipes.txt' (creates file and adds header if it does not exist already)
# and writes new recipe to it
def write(title, time, ingredients, instructions, url):
    data = {'Title': title, 'Time': time,
            'Ingredients': ingredients, 'Instructions': instructions, "URL": url}
    fields = ['Title', 'Time', 'Ingredients', 'Instructions', 'URL']

    flag = os.path.exists("recipes.txt")

    with open("recipes.txt", 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fields)
        if not flag:
            csv_writer.writeheader()
        csv_writer.writerow(data)


url = input("Recipe URL: ")
host = input("Website host: ")

# Rework this here, create dictionary and search for key??
if (host == "Food"):
    obj = food.Food(url, host)
if (host == "Foodnetwork"):
    obj = foodnetwork.Foodnetwork(url, host)
if (host == "Delish"):
    obj = delish.Delish(url, host)

# add error handling here

write(obj.title(), obj.time(), obj.ingredients(), obj.instructions(), obj.link())
