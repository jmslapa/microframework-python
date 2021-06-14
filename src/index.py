from mf.router.route import Route
from mf.bootstrap.app import Application

routes = [
    Route.group([
        Route.get('/', 'TestController', 'index'),
        Route.get('/show', 'TestController', 'show')
    ])
    .prefix('api')
    .namespace('src.controllers.test')
    .middleware([
        ('src.middlewares.test', 'TesteMiddleware')
    ])
]

def application(environ, start_response):
    response = Application(environ, routes).run()
    start_response(response.status, response.headers)
    return [response.body]