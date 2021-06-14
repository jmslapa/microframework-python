from __future__ import annotations
from abc import ABC, abstractclassmethod, abstractmethod
from mf.support.payload import ResponsePayload

class RouteComponent(ABC):
    
    @abstractmethod
    def check(self, method: str, path: str) -> bool:
        pass

    @abstractmethod
    def namespace(self, namespace: str) -> RouteComponent:
        pass

    @abstractmethod
    def prefix(self, prefix: str) -> RouteComponent:
        pass

    @abstractmethod
    def middleware(self, middlewares: "list[tuple(str, str)]") -> RouteComponent:        
        """
        Vincula middlewares

        :param list[tuple(str, str)] middlewares: Lista de tuplas (namespace, classe) que representam um middleware
        """
        pass
    
    @abstractmethod
    def handle(self) -> ResponsePayload:
        pass
