from support.request import Request
from bootstrap.app import Application

def application(environ, start_response):
    request = Request.getInstance()
    request.setEnv(environ)
    payload = Application().run(environ.get('REQUEST_METHOD'), environ.get('PATH_INFO'))
    start_response(payload.status, payload.headers)
    return [payload.body]