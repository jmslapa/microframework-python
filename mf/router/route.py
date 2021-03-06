from importlib import import_module
from mf.router.group import RouteGroup
from mf.support.payload import ResponsePayload
from mf.router.interfaces import RouteComponent

class Route(RouteComponent):
    __method = None
    __path = None
    __controller = None
    __action = None
    __namespace = None
    __middlewares = None

    def __init__(self, method:str, path:str, controller:str, action:str):
        self.__method = method
        self.__setPath(path)
        self.__controller = controller
        self.__action = action

    def __setPath(self, path: str):
        self.__path = (path if path != '' and path[0] == '/' else f'/{path}')
        self.__path = self.__path[:-1] if self.__path[-1] == '/' else self.__path

    @classmethod
    def get(self, path: str, controller: str, action: str):
        return self('GET', path, controller, action)
    
    @classmethod
    def post(self, path: str, controller: str, action: str):
        return self('POST', path, controller, action)

    @classmethod
    def put(self, path: str, controller: str, action: str):
        return self('PUT', path, controller, action)

    @classmethod
    def patch(self, path: str, controller: str, action: str):
        return self('PATCH', path, controller, action)

    @classmethod
    def delete(self, path: str, controller: str, action: str):
        return self('DELETE', path, controller, action)

    @staticmethod
    def group(routes: "list[Route]") -> RouteComponent:
        return RouteGroup(routes)

    def check(self, method: str, path: str) -> bool:
        return method == self.__method and path == self.__path

    def namespace(self, namespace: str) -> RouteComponent:
        self.__namespace = namespace
        return self

    def prefix(self, prefix: str) -> RouteComponent:
        self.__setPath((prefix if prefix[0] == '/' else f'/{prefix}') + (self.__path if self.__path != '/' else ''))
        return self

    def middleware(self, middlewares: "list[tuple(str, str)]") -> RouteComponent:
        self.__middlewares = middlewares
        return self
    
    def handle(self) -> ResponsePayload:
        controller = None
        module = import_module(self.__namespace)
        controllerClass = getattr(module, self.__controller)
        controller = controllerClass()

        for namespace, class_ in self.__middlewares:
            module = import_module(namespace)
            middlwareClass = getattr(module, class_)
            controller = middlwareClass(controller)

        action = getattr(controller, self.__action)
        return action()
