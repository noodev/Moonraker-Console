# Moonraker-Console
Simple moonraker console from computer to raspberry pi

![Screenshot_21](https://user-images.githubusercontent.com/79491496/119207135-1d80d880-ba52-11eb-95d3-eea7fc0d2f50.png)

# Downloads

please check https://github.com/MrNoob0/Moonraker-Console/releases/

Windows only supported at the moment

# Configuration

The config file looks like this:
```json
{
    "gui-theme": "Material1",

    "connection": {
        "ip": "http://192.168.1.70",
        "port": "7125"
    }
}
```
gui-theme: theme of the app (you can find the themes here: https://media.geeksforgeeks.org/wp-content/uploads/20200511200254/f19.jpg

ip: ip to your moonraker instance

port: port to your moonraker instance (You dont need to change it unless you manualy changed it)
