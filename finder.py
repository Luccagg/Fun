#finder of endpoints
import socket

HOST = '10.201.22.126'
PORT = 8000
try:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		m = ["lookup", "panel" ,"admin", "administrator"]
		s.connect((HOST, PORT))
		print(f'connected to {HOST}:{PORT}')
		#i = "shell"
		for i in m:
			print(f"From {i}")
			s.sendall(i.encode('utf-8'))
			print(f"Received - {s.recv(1024).decode('utf-8')}")
		#s.close()
except ConnectionRefusedError:
	print("Connection refused")
except Exceptions as e:
	print("error total", e)
