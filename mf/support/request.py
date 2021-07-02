from __future__ import annotations
import cgi
from json import dumps, loads

class Request:
    __env = None
    __instance = None
    __body = None

    @classmethod
    def getInstance(cls) -> Request:
        if cls.__instance == None:
            cls.__instance = cls()
        return cls.__instance

    def setEnv(self, env) -> Request:
        self.__env = env
        self.setBody(self.__extractBody())
        return self

    def setBody(self, body: dict) -> Request:
        self.__body = body
        return self

    @property
    def method(self) -> str:
        return self.__env.get('REQUEST_METHOD')

    @property
    def path(self) -> str:
        return self.__env.get('PATH_INFO')

    @property
    def contentType(self) -> str:
        return self.__env.get('CONTENT_TYPE')

    @property
    def contentLengh(self):
        return self.__env.get('CONTENT_LENGTH') or 0

    @property
    def query(self) -> dict:
        result = {}
        query = self.__env.get('QUERY_STRING').split('&')
        for attr in query:
            key, value = attr.split('=')
            result.update({key: value})
        return result

    @property
    def body(self) -> dict:
        return self.__body

    @property
    def files(self) -> dict:
        formData = cgi.FieldStorage(environ=self.__env, fp=self.__env['wsgi.input'], keep_blank_values=True)
        files = {}
        for key in formData.keys():
            if type(formData[key].value) == bytes:
                files[key] = formData[key]

        return files

    def __extractBody(self) -> dict:
        if self.contentType is None:
            return {}
        elif 'multipart/form-data' in self.contentType:
            return self.__parseFormData()
        elif 'x-www-form-urlencoded' in self.contentType:
            return self.__parseUrlEncoded()
        elif ('application/json' in self.contentType):
            return loads(self.__env.get('wsgi.input').read().decode('utf-8'))

    def __parseUrlEncoded(self):
        body = {}
        tuples = str(self.__env.get('wsgi.input').read().decode('utf-8')).split('&')
        for tuple in tuples:
            key, value = tuple.split('=')
            body[key] = value
        return body

    def __parseFormData(self):
        formData = cgi.FieldStorage(environ=self.__env, fp=self.__env['wsgi.input'], keep_blank_values=True)
        data = {}
        for key in formData.keys():
            val = formData[key].value
            if(type(val) != bytes):
                data[key] = formData[key].value
        return data
