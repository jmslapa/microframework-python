from http.payload import ResponsePayload
from router.interfaces import RouteComponent

class RouteGroup(RouteComponent):

    __routes: "list[RouteComponent]" = None
    __requestedRoute: RouteComponent = None

    def __init__(self, routes: "list[RouteComponent]" = []):
        self.__routes = routes

    def check(self, method: str, path: str) -> bool:
        for route in self.__routes:
            if route.check(method, path):
                self.__requestedRoute = route
                return True
        return False

    def namespace(self, namespace: str) -> RouteComponent:
        for route in self.__routes:
            route.namespace(namespace)
        return self

    def prefix(self, prefix: str) -> RouteComponent:
        for route in self.__routes:
            route.prefix(prefix)
        return self
    
    def handle(self) -> ResponsePayload:
        if self.__requestedRoute == None:
            raise RuntimeError('None requested route on routes group.')
        payload = self.__requestedRoute.handle()
        self.__requestedRoute = None
        return payload
