import socket
HOST = '10.201.52.221'
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	s.sendall("admin".encode('utf-8'))
	wordlist = open("test.txt", "r")
	#print(wordlist.read())
	for i in wordlist:
		print(i)
		s.sendall(i.encode('utf-8'))
		print(s.recv(1024).decode('utf-8'))

#for i in wordlist.read():
	#	print(i)
