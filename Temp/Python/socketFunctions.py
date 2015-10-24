'''
Created on 23 de out de 2015

@author: Spyri
'''
import socket
import os

def clientFunction():
    print 'clientFunction'
#     print socket.gethostbyname(socket.gethostname())
    HOST = '192.168.1.32'               # Endereco IP do Servidor
    PORT = 4000                         # Porta que o Servidor esta
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    tcp.connect(dest)
    print 'Para sair digite ^C\n'
    msg = raw_input()
    while msg != '^C':
        tcp.send (msg)
        msg = raw_input()
    tcp.close()
    
    
def serverFunction():
    print 'serverFunction'
    HOST = '192.168.1.30'               # Endereco IP do Servidor
    PORT = 5000                         # Porta que o Servidor esta
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (HOST, PORT)
    tcp.bind(orig)
    tcp.listen(1)
    
    con, cliente = tcp.accept()
    print ('Conexao de: ', cliente)
    while True:
        #Espera nova mensagem do cliente com tamanho maximo 1024
        msg = con.recv(1024)
        #Caso nao a mensagem seja null, sai do while
        if not msg: break
        #Caso ExecutarComandoShell: seja parte da mensagem, pega qual comando
        #devera ser executado e envia ele para o sistema
        if ("ExecutarComandoShell:" not in msg):
            startPosition = "ExecutarComandoShell:" in msg
            msg = msg[startPosition:]           
            print (cliente, msg)
        else:
            os.system(msg)
    print ('Finalizando conexao do cliente', cliente)
    con.close()
