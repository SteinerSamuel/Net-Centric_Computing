"""
Name: Simple Server
Version 1
Dependencies: socket
Author: Samuel Steiner
Description: A simple single threaded server which feeds files to a client based on the uri. This program uses port 8080
             to host read TCP requests.
"""
from socket import *
import mimetypes


def main():
    server_port = 8080
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('localhost', server_port))
    server_socket.listen(0)  # number of backlogged connections
    print('server ready')
    while True:

        try:
            connection_socket, addr = server_socket.accept()
            make_connection(connection_socket)
        except IOError:
            print("Server Socket Accept Error")

        pass


def make_connection(connection_socket):
    try:
        request = connection_socket.recv(1024).decode('utf-8')
        print(request)
    except IOError:
        print("Server Socket Recv Error")

    if request:
        # https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html
        try:
            [method, request_uri, http_version] = request.split(' ', 2)
            print(method)
            print(request_uri)
            print(http_version)
        except ValueError:
            print("Request Parse Error:" + request)

        try:
            # https://www.ietf.org/rfc/rfc2396.txt
            [scheme, hier_part] = request_uri.split(":", 1)
            print(scheme)
            print(hier_part)
        except ValueError:
            print("No Scheme")
            scheme = None
            hier_part = request_uri

        # more parsing is required but assuming the request_uri is a path
        print("Request URI is: " + hier_part)

        # see if the file is present
        if hier_part != "/":
            try:
                print("Request File is: " + hier_part)
                fo = open('static' + hier_part, "rb")
            except IOError:
                # here need to send a 404 error
                http_status = 'HTTP/1.1 404 Not Found\n'
                http_content = 'Content-Type: text/html charset=utf-8\n\n'
                outputdata = 'Bad File'
            else:
                # right now only file we have is the icon
                outputdata = fo.read()
                fo.close()
                http_status = 'HTTP/1.1 200 OK\n'
                mtype, _ = mimetypes.guess_type(hier_part)
                http_content = 'Content-Type: ' + mtype + '\n\n'
        else:
            # here we would the contents of index.html
            outputdata = '<!DOCTYPE html><head><meta charset="utf-8">' \
                            + '<title> test </title></head><body><h1>Index File</h1><p>Should be index</p></body>' \
                            + '</html>'
            http_status = 'HTTP/1.1 200 OK\n'
            http_content = 'Content-Type: text/html charset=utf-8\n\n'

        # send the response header

        connection_socket.send(http_status.encode('utf-8'))
        connection_socket.send('Connection: close\n'.encode('utf-8'))
        # https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html Should
        length_string = 'Content-Length: '+str(len(outputdata))+'\n'
        # connectionSocket.send('Transfer-Encoding: identity\n')
        connection_socket.send(length_string.encode('utf-8'))
        connection_socket.send(http_content.encode('utf-8'))

        print(type(outputdata))
        try:
            outputdatae = outputdata.encode('utf-8')
        except AttributeError:
            outputdatae = outputdata

        connection_socket.send(outputdatae)

        connection_socket.shutdown(SHUT_RDWR)
        connection_socket.close()
    else:
        print("No Request")


if __name__ == '__main__':
    main()
