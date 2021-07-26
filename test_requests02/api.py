import requests
import yaml

class Api():
    env=yaml.safe_load(open("env.yaml"))
    def send_02(self,data:dict):
        data["url"] = str(data["url"]).replace("host",self.env["host"][self.env["default"]])
        res = requests.request(method=data["method"],url=data["url"],headers=data["headers"])
        print(res.text)
        return res.text