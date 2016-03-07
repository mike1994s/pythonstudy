import socket
import select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
selectlist = []
s.bind(('0.0.0.0', 2222))
s.listen(10)
selectlist.append(s)
while True:
	readables, writeables, exceptions = \
		select.select(selectlist, [], [])
	for sockobj in readables :
		if sockobj == s:
			sockfd, addr = s.accept()
			selectlist.append(sockfd)
		else :
			data = sockobj.recv(1024)
		
			if not data:
				sockobj.close()
				selectlist.remove(sockobj)
			else:
				if data == 'close':
					sockobj.close()
					selectlist.remove(sockobj)
				else :
					sockobj.send(data)
