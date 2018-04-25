#!/usr/bin/env python2
import socket
import sys

# check input and print usage if incorrect
if len(sys.argv) != 2:
	print "\n[*] Usage: " + sys.argv[0] + " <buffer>\n"
	sys.exit(0)

# setup the IP and port we're connecting to
RHOST = "10.11.4.78"
RPORT = 31337

# create a TCP connection (socket)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

# build the message
buf = ""
buf += sys.argv[1]
buf += "\n"

# send message
s.send(buf)
print "Send: {0}".format(buf)

# receive response
data = s.recv(1024)
print "Received: {0}".format(data)

