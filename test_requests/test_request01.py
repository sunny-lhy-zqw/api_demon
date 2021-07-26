import base64
import requests
import json

class ApiTest:
    data={
        "url":"http://127.0.0.1:9999/demon.txt",
        "method":"get",
        "encoding":"base64",
        "headers":None
    }
    def send(self,data:dict):
       res = requests.request(url=data["url"],method=data["method"],headers=data["headers"])
       if data["encoding"]=="base64":
           rsp = base64.b64decode(res.text)
           return json.loads(rsp)
       elif data["encoding"]=="private":
           return "123"

# if __name__ == '__main__':
#     data={
#         "url":"http://127.0.0.1:9999/demon.txt",
#         "method":"get",
#         "encoding":"base64",
#         "headers":None,
#     }
#     print(ApiTest().send(data))