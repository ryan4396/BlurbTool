import PySimpleGUI as sg, configparser, clipboard, math

# Read the config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the blurb values in ini file
blurbs = {key: value for key, value in config['Blurb'].items()}

# Create the PySimpleGUI window
layout = []
layoutbefore = []
for key, value in blurbs.items():
    layoutbefore.append(sg.Button(key, size=(10, 2), key=key))

# Building out the 2D array for the layout
layout = [[] for i in range(0, math.floor(len(layoutbefore)/2+1))]

# Formatting it so that the layout has 2 columns of buttons per row
count = 0
for num, i in enumerate(layoutbefore):
    if num%2 == 0 and num>0:
        count+=1
    layout[count].append(i)

window = sg.Window('Blurb Copy', layout)

while True:
    event, values = window.read()

    if event in blurbs:
        # Copy the selected blurb to the clipboard
        clipboard.copy(blurbs[event])

    if event == sg.WINDOW_CLOSED:
        break

window.close()
