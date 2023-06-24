import random
import sys
import urllib.request
import http.client as httplib
from socket import *

# Check command line arguments
if len(sys.argv) != 2:
    print ("Launch Parameter : python UDPPingerServer.py PORT_NUM")
    print ("Example : python UDPPingerServer.py 6969") 
    sys.exit()

# Check for Internet Connection

def internet() -> bool:
    conn = httplib.HTTPSConnection("8.8.8.8", timeout=5)
    try:
        conn.request("HEAD", "/")
        return True
    except Exception:
        return False
    finally:
        conn.close()

# Retrieve host system's IP and Hostname (for creating launch command for the client program)
hostname=gethostname()   
IPAddr=gethostbyname(hostname)
if internet():
    PubIPAddr= urllib.request.urlopen('https://ipv4.seeip.org').read().decode('utf8')

print("Server's Hostname: "+hostname)   
print("Server's Private IP Address: "+IPAddr)
if internet():
    print("Server's Public IP Address: " +PubIPAddr)
print("Server's Port: "+sys.argv[1])
print("Use these as launch parameters to launch the client program.")
print("You can copy the following command(s) and run in a seperate Command Shell / Terminal Session")
print ("LAN Access: " + "python UDPPingerClient.py " + IPAddr + " " + sys.argv[1])

if internet():
    print ("WAN Access (limited): " + "python UDPPingerClient.py " + PubIPAddr + " " + sys.argv[1])
else:
    print ("Internet Access Unavailable.")

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', int(sys.argv[1])))

while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    # Capitalize the message from the client
    message = message.upper()

    # If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 4:
                print ("Simulated Packet Loss")
                continue
    # Otherwise, the server responds
    serverSocket.sendto(message, address)

    #Navindren Debug Params
    # Decode UTF-8 message received from Client Side
    message = message.decode()
    print (message)
