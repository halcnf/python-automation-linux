import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(('18.136.197.3', 111))
    print ("Port 80 reachable")
except socket.error as e:
    print ("Error on connect: ", e)
s.close()



