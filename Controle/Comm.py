import os
import socket
import time
import numpy
from threading import Thread

#PARADO = 0
#RODANDO = 1

class Comm(Thread):
	#Variaveis da classe
	exe = 0
	HOST = '192.168.0.102'               	# Endereco IP do Servidor
	PORT = 5000                         	# Porta que o Servidor esta
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connected = False

	#Variaveis de sensoriamento
	accelX = 0 			# Eixo x do acelerometro
	accelY = 0 			# Eixo y do acelerometro
	accelZ = 0 			# Eixo z do acelerometro
	gyroX = 0 			# Eixo x do giroscopio
	gyroY = 0 			# Eixo y do giroscopio
	gyroZ = 0 			# Eixo z do giroscopio
	sharpFrente = 0 	# Sharp da frente
	sharpTras = 0 		# Sharp de traz
	sharpEsq = 0 		# Sharp da esquerda
	sharpDir = 0 		# Sharp da direta

	#Variaveis controle interno
	potMotoresTotal = numpy.matrix([[0],[0],[0],[0]]) 	# Potencia total dos motores
	offsetMotores = numpy.matrix([[0],[0],[0],[0]]) 	# Offset dos motores 	
	potMotores = numpy.matrix([[0],[0],[0],[0]]) 		# Potencia dos motores

	#Variaveis anteriores para deteccao de atualizacao
	accelX_old = 0 			# Eixo x do acelerometro
	accelY_old = 0 			# Eixo y do acelerometro
	accelZ_old = 0 			# Eixo z do acelerometro
	gyroX_old = 0 			# Eixo x do giroscopio
	gyroY_old = 0 			# Eixo y do giroscopio
	gyroZ_old = 0 			# Eixo z do giroscopio
	sharpFrente_old = 0 	# Sharp da frente
	sharpTras_old = 0 		# Sharp de traz
	sharpEsq_old = 0 		# Sharp da esquerda
	sharpDir_old = 0 		# Sharp da direta
	potMotoresTotal_old = numpy.matrix([[0],[0],[0],[0]]) 	# Potencia total dos motores
	offsetMotores_old = numpy.matrix([[0],[0],[0],[0]]) 	# Offset dos motores 	
	potMotores_old = numpy.matrix([[0],[0],[0],[0]]) 		# Potencia dos motores

	def initComm(self):
		dest = (self.HOST, self.PORT)
		self.tcp.connect(dest)
		connected = True
 	
	def __init__ (self):
		self.initComm();
	
#--------------------------- Controle interno ---------------------------------#
	def set_exe(self, auxExe):
		self.exe = auxExe
        
	def check(self):
		return(self.exe)

#------------------------------- Sensores -------------------------------------#

	def set_AccelX(self, auxAccelX):
		self.accelX = auxAccelX
		
	def set_AccelY(self, auxAccelY):
		self.accelY = auxAccelY

	def set_AccelZ(self, auxAccelZ):
		self.accelZ = auxAccelZ

	def set_GiroX(self, auxGyroX):
		self.gyroX = auxGyroX
		      
	def set_GiroY(self, auxGyroY):
		self.gyroY = auxGyroY

	def set_GiroZ(self, auxGyroZ):
		self.gyroZ = auxGyroZ

	def set_SharpFrente(self, auxSharpFrente):
		self.sharpFrente = auxSharpFrente

	def set_SharpTraz(self, auxSharpAtras):
		self.sharpTras = auxSharpAtras

	def set_SharpEsq(self, auxSharpEsq):
		self.sharpEsq = auxSharpEsq

	def set_SharpDir(self, auxSharpDir):
		self.sharpDir = auxSharpDir

#-------------------------------- Motores -------------------------------------#

	def set_PotMotoresTotal(self, auxPotMotoresTotal):
		self.potMotoresTotal = auxPotMotoresTotal

	def set_OffsetMotores(self, auxOffsetMotores):
		self.offsetMotores = auxOffsetMotores

	def set_PotMotores(self, auxPotMotores):
		self.potMotores = auxPotMotores

#---------------------------- Funcoes internas --------------------------------#
	def hasBeenUpdated(self):
		return True

#------------------------------ Main Loop -------------------------------------#
	def run(self):
		while self.exe == 1:
			if self.hasBeenUpdated():
				paramMsg = "[INICIO]"
				paramMsg.append("\n\tMotor1: ")
				paramMsg.append(self.potMotores[0,0])
				paramMsg.append("\n\tMotor2: ")
				paramMsg.append(self.potMotores[1,0])
				paramMsg.append("\n\tMotor3: ")
				paramMsg.append(self.potMotores[2,0])
				paramMsg.append("\n\tMotor4: ")
				paramMsg.append(self.potMotores[3,0])
				paramMsg.append("\n\tAccelX: ")
				paramMsg.append(self.accelX)
				paramMsg.append("[FIM]")
				self.tcp.send(paramMsg)
		self.tcp.close()
