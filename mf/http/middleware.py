from typing import Any, final
from mf.http.controller import Controller

class Middleware(Controller):

    __controller: Controller = None

    def __init__(self, controller: Controller) -> None:
        self.__controller = controller

    def __getattr__(self, attr: str) -> Any:
        self._before()
        if hasattr(self.__controller, attr):
            def wrapper(*args, **kw):
                resource = getattr(self.__controller, attr)(*args, **kw)
                resource = self._after(resource) or resource
                return resource
        return wrapper

    def _before(self):
        pass

    def _after(self, resource):
        pass

    

