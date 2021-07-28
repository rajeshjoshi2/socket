import socket
s = socket.socket()
print ("Socket successfully created")

port = 9000
s.bind(('192.168.2.6',port))
print(f"socket binded to {port}")

s.listen(5)
print("waiting for connection...")

while True:
    c,addr = s.accept()
    print ('Got connection from', addr )
    c.send(bytes('Thank you for connecting','utf-8')) 
    c.close() 

