import socket,threading
def recv_msg(cleint_sock):
  while True:
    msg=cleint_sock.recv(1024).decode('UTF-8')
    if msg:
      print('\n')
      print(msg)
    else:
      break
def send_messa(client):
  name=input('enter the name: ')
  while True:
    msg=input('enter the message: ') 
    msg=name+msg 
    client.send(msg.encode('UTF-8'))  
cleint_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cleint_sock.connect(('localhost',5000))
threading.Thread(target=recv_msg,args=(cleint_sock,)).start()
send_messa(cleint_sock)
