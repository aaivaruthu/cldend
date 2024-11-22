import socket,threading
cleints=[]
def handle_client(client,addr):
    print(f'mad new connecrtiom {addr}')
    while True:
        msg=client.recv(1024)
        if msg:
            try:
                broadcast(client,msg)
            except:
                print(f'error occured with{clleint}')    
                break
        else:
            print('eroor')    
            break
    cleints.remove(client)
    client.close()
def broadcast(sender,msg):
    for cleint in cleints:
        if cleint!=sender:
            try:
                cleint.send(msg)
            except:
                print('error')

server_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_sock.bind(('localhost',5000))
server_sock.listen()
while True:
    clleint,addr=server_sock.accept()
    cleints.append(clleint)
    threading.Thread(target=handle_client,args=(clleint,addr)).start()