from tornado.web import RequestHandler
from tornado.escape import json_encode


class FiltersHandler(RequestHandler):
    def get(self):
        return self.write(json_encode({'status': 'SUCCESS'}))


class ScenariosHandler(RequestHandler):
    def get(self):
        return self.write(json_encode({'status': 'SUCCESS'}))
