from __future__ import annotations
from abc import ABC, abstractclassmethod, abstractmethod
from http.payload import ResponsePayload

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
    def handle(self) -> ResponsePayload:
        pass
