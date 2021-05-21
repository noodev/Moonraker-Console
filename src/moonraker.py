import requests
from config import *

print('connected to ' + ip + ':' + port)

class moonraker():
    def sendgcode(gcode):
        x = requests.post(f'' + ip + ':' + port + '/printer/gcode/script?script=' + gcode)
    def restart(service):
        x = requests.post(f'' + ip + ':' + port + '/machine/services/restart?service=' + service)
    def status():
        x = ('192.168.1.70:7125/printer/info')
