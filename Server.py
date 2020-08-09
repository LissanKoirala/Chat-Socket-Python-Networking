# Creator Lissan Koirala
# Date of creating 2019/11/04

# For networking
import socket

# Indication that the server has started
print("Server Started...")

host = "0.0.0.0" # The server listens to it's all ip addresses
port = 5451 # Port where the incoming and outgoing of the data will occur

s.bind((host,port)) # Binding the socket, or creating an connection where other can join
s.listen(1) # Number of requests that it will listen for before closing
 
con, addr=s.accept() # Accepting the connection

print("Connected with : ",addr) # Printing the ip address of the connected client
while True:
    c_messg = con.recv(1024) # Recieving the message from the client
    c_messg = c_messg.decode() # Decoding the message as it is in encoded in bytes
    print("Client : ",c_messg) # Printing the client message
    messg = input("Your Message : ") # Asking what to send to the client
    messg = messg.encode() # Encoding the message to bytes
    con.send(messg) # Sending the message
s.close() # Closing the socket
