from router.route import Route
from support.request import Request
from bootstrap.app import Application

routes = [
    Route.group([
        Route.get('/', 'IndexController', 'index'),
        Route.get('/show/', 'IndexController', 'show')
    ]).prefix('api').namespace('controllers.index')
]

def application(environ, start_response):
    response = Application(environ, routes).run()
    start_response(response.status, response.headers)
    return [response.body]