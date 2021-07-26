from unittest import TestCase
from test_requests import test_request01

class TestApiTest(TestCase):
    data={
        "url":"http://127.0.0.1:9999/demon.txt",
        "method":"get",
        "encoding":"base64",
        "headers":None
    }
    def test_send(self,data=data):
        res = test_request01.ApiTest().send(data)
        print(res)
