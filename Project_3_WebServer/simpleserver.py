#-------------------------------------------------------------------------------
# Name:        Hello World Server
# Purpose:
#
# Author:      rosienej
#
# Created:     20/09/2013
# Copyright:   (c) rosienej 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from socket import *



def main():
    serverPort = 8080
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('localhost',serverPort))
    serverSocket.listen(0) # number of backlogged connections
    print('server ready')
    while 1:

        try:
            connectionSocket,addr = serverSocket.accept()
        except IOError:
            print("Server Socket Accept Error")

        try:
            request = connectionSocket.recv(1024).decode('utf-8')
            print(request)
        except IOError:
            print("Server Socket Recv Error")

        if request:
            # https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html
            try:

                [Method,Request_URI,HHTP_Version] = request.split(' ',2)
                print(Method)
                print(Request_URI)
                print(HHTP_Version)
            except ValueError:
                print("Request Parse Error:" + request)

            try:
            # https://www.ietf.org/rfc/rfc2396.txt
                [scheme,hier_part]=Request_URI.split(":",1)
                print(scheme)
                print(hier_part)
            except ValueError:
                print("No Scheme")
                scheme = None
                hier_part = Request_URI

            # more parsing is required but assuming the Request_URI is a path
            print("Request URI is: "+hier_part)


            # see if the file is present
            if hier_part != "/":
                try:
                    print("Request File is: "+hier_part)
                    fo = open('.'+hier_part,"rb")
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
                    http_content = 'Content-Type: image/x-icon\n\n'
            else:
                # here we would the contents of index.html
                outputdata = '<!DOCTYPE html><head><meta charset="utf-8">' \
                             +'<title> test </title></head><body><h1>Index File</h1><p>Should be index</p></body></html>'
                http_status = 'HTTP/1.1 200 OK\n'
                http_content = 'Content-Type: text/html charset=utf-8\n\n'

            # send the response header

            connectionSocket.send(http_status.encode('utf-8'))
            connectionSocket.send('Connection: close\n'.encode('utf-8'))
            # https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html Should
            LengthString = 'Content-Length: '+str(len(outputdata))+'\n'
            #connectionSocket.send('Transfer-Encoding: identity\n')
            connectionSocket.send(LengthString.encode('utf-8'))
            connectionSocket.send(http_content.encode('utf-8'))

            print(type(outputdata))
            try:
                outputdatae = outputdata.encode('utf-8')
            except AttributeError:
                outputdatae = outputdata

            connectionSocket.send(outputdatae)

            connectionSocket.shutdown(SHUT_RDWR)
            connectionSocket.close()
        else:
            print("No Request")

    pass

if __name__ == '__main__':
    main()