import os
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import csv
import food


def write(title, time, ingredients, instructions):
    data = {'Title': title, 'Time': time,
            'Ingredients': ingredients, 'Instructions': instructions}
    fields = ['Title', 'Time', 'Ingredients', 'Instructions']
    df_new = pd.DataFrame(
        data, columns=['Title', 'Time', 'Ingredients', 'Instructions'])

    flag = os.path.exists("recipes.txt")

    with open("recipes.txt", 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fields)
        if not flag:
            csv_writer.writeheader()
        csv_writer.writerow(data)


url = input("Recipe URL: ")
host = input("Website host: ")

if (host == "Food"):
    obj = food.Food(url, host)

write(obj.title(), obj.time(), obj.ingredients(), obj.instructions())
