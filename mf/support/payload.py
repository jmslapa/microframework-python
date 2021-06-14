class ResponsePayload:
    __body = None
    __status = None
    __headers = None

    def __init__(self, body: bytes, status: str, headers: "list[tuple(str, str)]"):
        self.__body = body
        self.__status = status
        self.__headers = headers

    @property
    def body(self):
        return self.__body

    @property
    def status(self):
        return self.__status

    @property
    def headers(self):
        return self.__headers