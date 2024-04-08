<h1 align="center">UDP Pinger Enhanced</h1>
  <p align="center">
    An enhanced version of UDP-Pinger recompiled in Python 3 as a part of an assignment on my NMJ41403 - Network Programming course.
  </p>
<br>

> This is a UDP Pinger written in Python which simulates a 40% packet drop rate. The client sends pings to the server, which echoes the message back. The client then calculates the Round Trip Time (RTT) based on the response.

 **Please look at the screenshots to know what the UDP Pinger output looks like.**

# ✨ Launch Parameters:


To run the server:
`python UDPPingerServer.py PORT_NUM`

Example: `python UDPPingerServer.py 6969`

To run the client in Windows:
`python UDPPingerClient.py IP_ADDR PORT_NUM`

To run the client in Linux:
`python3 UDPPingerClient.py IP_ADDR PORT_NUM`

Example: `python UDPPingerClient.py 127.0.0.1 6969`

# Screenshots

### Server-Side (UDPPingerServer.py) - with port 6969 😜
![Server Execution in Debian 10](/Screenshots/UDP-Pinger-Server-Side.png)

### Client-Side (UDPPingerClient.py) - using python3 command to launch explicitly on Python v3
![Client Execution in Debian 10](/Screenshots/UDP-Pinger-Client-Local-Hello-Github.png)





