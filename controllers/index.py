from http import response
from support.request import Request

class IndexController:

    def index(self):        
        return response.json('index')

    def show(self):
        return response.json('show')
