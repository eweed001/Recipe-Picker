# General helper functions for scraping the recipes

import html
import re


def correct_string(str):
    x = str.replace("\n", " ").replace("\t", " ").strip()
    return re.sub(" +", " ", x)
