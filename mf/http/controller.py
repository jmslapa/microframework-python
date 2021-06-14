from mf.support.request import Request
from mf.support import response

class Controller():

    @property
    def _request(self) -> Request:
        return Request.getInstance()

    @property
    def _response(self):
        return response
