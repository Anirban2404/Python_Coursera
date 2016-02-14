# Exploring the HyperText Transport Protocol
# You are to retrieve the following document using the HTTP protocol
# in a way that you can examine the HTTP Response headers.
# http://www.pythonlearn.com/code/intro-short.txt
# There are three ways that you might retrieve this web page and look at the response headers:
# Preferred: Modify the socket1.py program to retrieve the above URL and print out the headers and data.
# Open the URL in a web browser with a developer console or FireBug and manually
# examine the headers that are returned.
# Use the telnet program as shown in lecture to retrieve the headers and content.

import socket

# Creating the socket
my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0,)
# Connecting the socket with www.pythonlearn.com
my_sock.connect(('www.pythonlearn.com',80))

# Send the GET request
my_sock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    # Recieving the data via socket
    data = my_sock.recv(512)
    if (len(data) <1): break # if received data is not empty
    print data
