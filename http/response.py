from http.payload import ResponsePayload
from json import dumps as encode 

def json(body, status: int = 200, headers: "list[tuple(str, str)]" = []):
    headers.extend([('Content-type', 'application/json')])
    body = bytes(encode(body), 'utf-8')
    return ResponsePayload(body, str(status), headers)

def html(body: str, status: int = 200, headers: "list[tuple(str, str)]" = []):
    headers.extend([('Content-type', 'text/html')])
    body = bytes(body, 'utf-8')
    return ResponsePayload(body, str(status), headers)
