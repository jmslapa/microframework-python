from router.interfaces import RouteComponent
from http.payload import ResponsePayload
from support.request import Request
from http.response import html
from router.route import Route

class Application():

    __routes = None
    __request = None

    def __init__(self, environ: dict, routes: "list[RouteComponent]") -> None:
        self.__request = Request.getInstance().setEnv(environ)
        self.__routes = routes

    def run(self) -> ResponsePayload:

        path = self.__request.path[:-1] if self.__request.path[-1] == '/' else self.__request.path
        for route in self.__routes:
            if route.check(self.__request.method, path):
                return route.handle()
        return html('<h2>404: Sorry, endpoint not found.</h2>', 404)
        
        