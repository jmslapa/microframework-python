from mf.support import response
from mf.support.payload import ResponsePayload
from mf.http.middleware import Middleware
from json import loads, dumps
class TesteMiddleware(Middleware):
    
    def _before(self):
        self._request.body['example'] = 'Micro-' + self._request.body['example']
    
    def _after(self, resource: ResponsePayload):
        json = loads(resource.body.decode('utf-8'))
        json['message'] = json['message'] + ' construído em Python'
        return response.json(json)
