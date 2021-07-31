import requests
from config_reader import new_settings as settings

if __name__ != "__main__":
    # assign ip and port values from
    # config.json

    ip = settings["connection"]["ip"]
    port = settings["connection"]["port"]

print(f"Connected to ip: {ip} port: {port}")

class moonraker_commands():
    def sendgcode(gcode):
        send_url = f"{ip}:{port}/printer/gcode/script?script={gcode}"
        x = requests.post(send_url)
    def restart(service):
        restart_url = f"{ip}:{port}/machine/services/restart?service={service}"
        x = requests.post(restart_url)
    def status():
        x = (f"{ip}/printer/info")
