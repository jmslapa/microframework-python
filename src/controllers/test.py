from mf.http.controller import Controller

class TestController(Controller):

    def index(self):
        return self._response.json('index')

    def show(self):
        return self._response.json('show')