import os, socket

print(os.getlogin())
print(os.getuid())
print(os.getloadavg())
print(os.uname())

node_name = os.uname()
print(node_name[1])

print(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('google.com', 0))
print(s.getsockname()[0])
