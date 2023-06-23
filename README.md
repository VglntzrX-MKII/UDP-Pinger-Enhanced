A UDP Pinger in Python where the packet drop rate is simulated to be 40% and
the client can ping the server, the server echos the message as a response and the client
can calculate Round Trip Time on response.

Please look at the screenshot (will be added soon) to know what the Pinger output looks like.

EXECUTE:
========

To run the server:
`python UDPPingerServer.py PORT_NUM`

Example: `python UDPPingerServer.py 6969`

To run the client:
`python UDPPingerClient.py IP_ADDR PORT_NUM`

Example: `python UDPPingerClient.py 127.0.0.1 6969`
