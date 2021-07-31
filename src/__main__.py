import sys
import PySimpleGUI as sg
from moonraker import moonraker_commands
from config_reader import new_settings

sg.theme(new_settings["gui-theme"])

layout = [[sg.Text('Enter gcode here:'), sg.InputText()], [sg.Button('Send'), sg.Button('Exit')]]

window = sg.Window('Moonraker Console', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    try:
        moonraker_commands.sendgcode(values[0])
    except Exception as e:
        sys.exit()
window.close()
