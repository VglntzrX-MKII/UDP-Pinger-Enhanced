import time
import sys
from socket import *

# Check command line arguments
if len(sys.argv) != 3:
    print ("Launch Parameter : python UDPPingerClient.py IP_ADDR PORT_NUM")
    print ("Example : python UDPPingerServer.py 127.0.0.1 6969") 
    sys.exit()
        
    
# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)

# To set waiting time of one second for reponse from server
clientSocket.settimeout(1)

# Declare server's socket address
remoteAddr = (sys.argv[1], int(sys.argv[2]))

# Query Keyboard Input From Client Side
typed = input("Enter a message: ")
print ("'" + typed + "'" + " will be capitalised and displayed alongside ping statistics when message is recieved.")

# Ping ten times
for i in range(10):
    
    sendTime = time.time()
    message = (typed + ' PING #' + str(i + 1) + " @ " + str(time.strftime("%H:%M:%S")))
    clientSocket.sendto(message.encode('utf-8'), remoteAddr)


    
    try:
        data, server = clientSocket.recvfrom(1024)
        # Decode UTF-8 Data before being printed onto Console
        data = data.decode()
        recdTime = time.time()
        rtt = (recdTime - sendTime)
        print ("Message Received --> ", data)
        print ("Round Trip Time = ", rtt)
        print
    
    except timeout:
        print ('Request Timed Out.')
        print
