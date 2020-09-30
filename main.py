import socket
from view import *


URLS = {
    '/': index,
    '/blog': blog
}


def parse_request(request):
    parsed = request.split(' ')
    method = parsed[0]
    url = parsed[1]
    return (method, url)


def generate_headers(method, url):
    if not method == 'GET':
        return ('HTTP/1.1 405 Method not allowed\n\n, 405')
    if not url in URLS:
        return ('HTTP/1.1 404 Not found\n\n, 405')
    return ('HTTP/1.1 200 OK\n\n, 405')


def generate_content(code, url):
    if code == 403:
        return '<h1>404</h1>'
    if code == 405:
        return '<h1>404</h1>'
    return URLS[url]


def generate_response(request):
    method, url = parse_request(request)
    header, code = generate_headers(method, url)
    body = generate_content(code, url)

    return (headers + body).encode()


def run():
    server_socet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socet.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socet.bind(('localhost', 5000))
    server_socet.listen()

    while True:
        clint_socket, addr = server_socet.accept()
        request = clint_socket.recv(1024)
        print(request)
        print()
        print(addr)

        response = generate_response(request.decode('utf-8'))

        clint_socket.sendall(response)
        clint_socket.close()




if __name__ == '__main__':
    run()