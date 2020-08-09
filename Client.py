# Creator Lissan Koirala
# Date of creating 2019/11/04

# For networking
import socket

# If it is connecting in the localhost
host = socket.gethostbyname(socket.gethostname()) 

# If it is connecting in the local area network or throughout the internet
# host = "IP Address of the Server" or host = socket.gethostbyname("HOSTNAME OF THE COMPUTER CONNECTING TO")

port = 5451 # Same port where the server is listening to

s.connect((host,port)) # Connecting to the server

while True:
    c_messg=input("Message to server: ") # Message to the server
    c_messg = c_messg.encode() # Encoding the message to bytes
    s.send(c_messg) # Sending bytes
    s_messg = s.recv(1024) # Receving the server messsage
    s_messg = s_messg.decode() # Decoding the message
    print("Message from Server: ", s_messg) # Printing the message
s.close() # Closing the connection