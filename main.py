import PySimpleGUI as sg
import pandas as pd
from random import randint
import pyperclip


data = pd.read_csv("recipes.txt")
choices = len(data.index)


layout = [[sg.Text("Random Recipe Picker")],
          [sg.Button("Generate"), sg.Button("Cancel")],
          [sg.Text("URL:"), sg.Text(key="-URL-", size=(70, 1))]]

window = sg.Window("Title", layout)

while True:
    event, values = window.read()
    if event == "Cancel" or event == sg.WIN_CLOSED:
        break
    if event == "Generate":
        val = randint(0, choices-1)
        url = data.loc[val, 'URL']
        pyperclip.copy(url)
        # print(url)
        window["-URL-"].update(url)
        # print("hello")

window.close()
