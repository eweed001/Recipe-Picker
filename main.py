# Main method for interacting with GUI

import PySimpleGUI as sg
import pandas as pd
from random import randint
import pyperclip
import webbrowser


data = pd.read_csv("recipes.txt")
choices = len(data.index)

sg.theme('Light Purple')

inner_layout = [[sg.Text("Ttitle:"),
                 sg.Text(key="-Title-", justification='left',
                         auto_size_text=True, size=(50, 1),
                         font=('Helvetica', 10))],
                [sg.Button('open', font=('Helvetica', 10), key='-but-', visible=False)]]
# inner_layout2 = [[sg.Button(
#     'Open Webpage', 'center', auto_size_button=True, font=('Helvetica', 10), enable_events=True)]]

layout = [[sg.Text("Random Recipe Picker", size=(500, 1), font=("Helvetica", 25),
                   justification='center')],
          [sg.Button("Generate", auto_size_button=True, font=(
              'Helvetica', 15)), sg.Button("Cancel", auto_size_button=True, font=(
                  'Helvetica', 15))],
          [sg.Text("URL:"), sg.Text(key="-URL-", auto_size_text=True)],
          [sg.Column(inner_layout, justification='left')]
          #   [sg.Column(inner_layout2, justification='center', visible=False,
          #              key='-button-')]
          ]

window = sg.Window("Title", layout, size=(500, 500), element_justification='c')
# window['-DISPLAY-'].set_size((45, 45))

while True:
    event, values = window.read()
    print(event, values)
    if event == "Cancel" or event == sg.WIN_CLOSED:
        # print("hello")
        break
    if event == "Generate":
        val = randint(0, choices-1)
        url = data.loc[val, 'URL']
        title = data.loc[val, 'Title']
        pyperclip.copy(url)
        # window["-URL-"].update(url)
        window["-Title-"].update(title)
        window['-but-'].update(visible=True)

    if event == "-but-":
        webbrowser.open(url)
        break

window.close()
