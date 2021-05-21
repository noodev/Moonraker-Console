import PySimpleGUI as sg
import keyboard
from moonraker import moonraker
from config import *

sg.theme(guitheme)

layout = [[sg.Text('Enter gcode here:'), sg.InputText()], [sg.Button('Send'), sg.Button('Exit')]]

window = sg.Window('Moonraker Console', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    moonraker.sendgcode(values[0])
window.close()
