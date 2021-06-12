from importlib import import_module

class Route:
    _method = None
    _path = None
    _controller = None
    _action = None
    _namespace = None

    def __init__(self, method:str, path:str, controller:str, action:str):
        self._method = method
        self._path = path
        self._controller = controller
        self._action = action

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

    def check(self, method: str, path: str):
        return method == self._method and path == self._path

    def namespace(self, namespace: str):
        self._namespace = namespace
        return self
    
    def handle(self):
        module = import_module(self._namespace)
        class_ = getattr(module, self._controller)
        controller = class_()
        action = getattr(controller, self._action)
        return action()
