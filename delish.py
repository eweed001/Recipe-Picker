# Scraper for delish.com

import requests
from bs4 import BeautifulSoup
from _helpers import correct_string


class Delish():

    def __init__(self, url, host):
        data = requests.get(url).content
        self.soup = BeautifulSoup(data, "html.parser")
        self.url = url
        self.host = host

    # Returns link to recipe
    def link(self):
        return self.url

    # Returns host website of recipe
    def host(self):
        return "delish.com"

    # Returns title of recipe
    def title(self):
        return self.soup.find("h1").get_text().strip()

    # Returns time required for recipe, Unimplemented right now
    def time(self):
        return "0"
        # return self.soup.find("div", {"class":
        #                               "recipe-facts__time"})

    # Returns list of ingredients for recipe
    def ingredients(self):
        ingredients = self.soup.findAll(
            "div", {"class": "ingredient-item"})
        return [correct_string(x.get_text()) for x in ingredients]

    # Returns list of instructions for recipe
    def instructions(self):
        instructions = self.soup.find("ol").findAll("li")
        return ",".join([correct_string(x.get_text()) for x in instructions])
