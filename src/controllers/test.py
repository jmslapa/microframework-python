from mf.http.controller import Controller

class TestController(Controller):

    def index(self):
        return self._response.json({'message': self._request.body.get('example') or 'Mensagem padrão.'})

    def show(self):
        return self._response.json('show')