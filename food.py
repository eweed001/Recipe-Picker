# Scraper for Food.com

import requests
from bs4 import BeautifulSoup
from _helpers import correct_string


class Food():

    def __init__(self, url, host):
        data = requests.get(url).content
        self.soup = BeautifulSoup(data, "html.parser")
        self.url = url
        self.host = host

    # Returns link to recipe
    def link(self):
        return self.url

    # Returns host website of recipe    def host(self):
    def host(self):
        return "food.com"

    # Returns title of recipe
    def title(self):
        return self.soup.find("h1").get_text()

    # Returns time required for recipe, Unimplemented right now
    def time(self):
        return "0"
        # return self.soup.find("div", {"class":
        #                               "recipe-facts__time"})

    # Returns list of ingredients for recipe
    def ingredients(self):
        ingredients = self.soup.findAll(
            "li", {"class": "recipe-ingredients__item"})
        return [correct_string(x.get_text()) for x in ingredients]

    # Returns list of instructions for recipe
    def instructions(self):
        instructions = self.soup.findAll(
            "li", {"class": "recipe-directions__step"})
        return ",".join([correct_string(x.get_text()) for x in instructions])
