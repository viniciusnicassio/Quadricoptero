import sys
from threading import Thread 
from cliente.socketFunctions import clientFunction, serverFunction

#Cria as threads executando a funcao esperada
clientThread = Thread(target=clientFunction, args=[])
serverThread = Thread(target=serverFunction, args=[])

#Inicia as threads
clientThread.start()
serverThread.start()

#Espera as threads terminarem para continuar o fluxo
clientThread.join()
print 'clientThread finished'
serverThread.join()
print 'serverThread finished'

sys.exit(0)
