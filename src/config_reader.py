import json, os

default_config_content = '{ "gui-theme": "Material1", "connection": { "ip": "http://192.168.1.70", "port": 7125 } }'

class configreader():
    def __init__(self):
        pass
    def read_file(self, file_name):
        if os.path.exists(file_name):

            # Finds 'file_name' in the previous directory
            f = open(file_name)
            file_content = str(f.read())
            f.close()
            loaded_file = json.loads(str(file_content))

            return loaded_file
        else:
            t_f = open(file_name, "a")
            t_f.write(str(default_config_content))
            t_f.close()

if __name__ != '__main__':
    config_file = configreader()

    new_settings = config_file.read_file("config.json")
