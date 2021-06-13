from http.payload import ResponsePayload
from support.request import Request
from http.response import html
from router.route import Route

class Application():

    routes = [
        Route.group([
            Route.get('/', 'IndexController', 'index'),
            Route.get('/show/', 'IndexController', 'show')
        ]).prefix('api').namespace('controllers.index')
    ]

    def run(self, method, path) -> ResponsePayload:
        path = path[:-1] if path[-1] == '/' else path
        for route in self.routes:
            if route.check(method, path):
                return route.handle()
        return html('<h2>404: Sorry, endpoint not found.</h2>', 404)
        
        