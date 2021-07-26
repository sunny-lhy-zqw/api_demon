from unittest import TestCase
from test_requests02 import api

class TestApi(TestCase):
    data={
        "url":"http://host:9999/demon.txt",
        "method":"get",
        "encoding":"base64",
        "headers":None
    }
    def test_send_02(self,data=data):
        self.api = api.Api()
        self.api.send_02(data)
