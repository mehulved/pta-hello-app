import falcon
import json
import platform

class Hello:
    def on_get(self, req, resp):
        resp.body = "Hello from " + platform.uname().node


api = falcon.API()
api.add_route('/', Hello())
