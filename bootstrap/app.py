from support.request import Request
from http.response import html
from router.route import Route

class Application():

    routes = [
        Route.get('/', 'IndexController', 'index').namespace('controllers.index'),
        Route.get('/show', 'IndexController', 'show').namespace('controllers.index')
    ]

    def run(self, method, path):
        for route in self.routes:
            if route.check(method, path):
                return route.handle()
        return html('<h2>404: Sorry, endpoint not found.</h2>', 404)
        
        