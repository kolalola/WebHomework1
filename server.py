import socket
import os

TCP_IP = 'localhost'
TCP_PORT = 8000
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    #request = data.decode("utf-8").split("\r\n", 1)
    requestSplit=data.decode('utf-8').split(" ")
    print (requestSplit)
    response=data
    address=""
    if(len(requestSplit)>1):
        address = requestSplit[1][1:]

    if(os.path.exists(address)):
        file=open(address,mode='r')
        response="""HTTP/1.1 200 OK \n Content type:text HTML\n\n\n """ + file.read()
    print(response)
    conn.send(response.encode('utf-8'))  # echo
    conn.close()
