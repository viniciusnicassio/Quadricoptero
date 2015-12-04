#! /usr/bin/env python
#coding: utf-8
# ----------------------------------------------------------------------------
# ****************************************************************************
#  * @file Controle.py
#   *@project: TCC - FEI 😛
#  * @author Vinicius Nicassio Ferreira
#  * @version V0.0.1
#  * @created 23/11/2015
#  * @e-mail vinicius.nicassio@gmail.com
#  * @brief main
#  ****************************************************************************
#  Program to execute the Controle process
# ****************************************************************************

#import parser for arguments
import time
from threading import Thread
from Controle import *
from Calibrar import *
import socket

## Iniciando Comunicacao com servidor
#HOST='192.168.0.102'
#PORT=5000
#tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#dest = (HOST, PORT)
#tcp.connect(dest)
#------------------------------------------------------------------------------------------------------------------------------------------------

threads = []
threads.insert(0, Controle()) #Iniciado thread Controle

conf= raw_input("Deseja testar os ESC [S/N]?: ")

if conf=="s"or conf=="S":
    threads[0].teste()
    time.sleep(1)
    
while threads[0].check():
    pass
#------------------------------------------------------------------------------------------------------------------------------------------------
#Iniciado Calibracao
threads.insert(1, Calibrar()) #Iniciado threads

#Pegando Valores iniciais
threads[1].set_Potencia(threads[0].get_Potencia())

threads[1].set_kp(threads[0].get_kp())
threads[1].set_ki(threads[0].get_ki())
threads[1].set_kd(threads[0].get_kd())

threads[1].set_MaxPWM(threads[0].get_MaxPWM())
threads[1].set_MinPWM(threads[0].get_MinPWM())


threads[0].start()
threads[1].start()

while threads[1].check()==0:
    pass

while threads[1].check():
    #Atualizando dados para controle
    threads[0].set_kp(threads[1].get_kp())
    threads[0].set_ki(threads[1].get_ki())
    threads[0].set_kd(threads[1].get_kd())
    threads[0].set_Potencia(threads[1].get_Potencia())

#    tcp.send("[INICIO]\033[1;34mCalibracao\033[0m\n\n\033[0;32mPotencia atual: "+str(threads[1].get_Potencia())+"\033[0m \t\tMotor 1: "+str(threads[0].get_Motor1())+"\t\tMotor 2: "+str(threads[0].get_Motor2())+"\t\t\tAcc X: "+str(threads[0].get_AccX())+"\t\tAcc Y: "+str(threads[0].get_AccY())+"\t\tGiroscopio Z: "+str(threads[0].get_GiroZ())+"\n\033[0;32mKp atual: "+str(threads[1].get_kp())+"\033[0m\n\033[0;32mKi atual: "+str(threads[1].get_ki())+"\033[0m	\t\t\t\tMotor 3: "+str(threads[0].get_Motor3())+"\t\tMotor 4: "+str(threads[0].get_Motor4())+"\n\033[0;32mKd atual: "+str(threads[1].get_kd())+"\033[0m\n\nw -->\tSubir\ns -->\tDescer\nd -->\tDesligar\np -->\tParar\no -->\tAjustar passo, passo atual: 1\nk -->\tAjustar ganhos\nb -->\tSair\n\nDigite a funcao desejada: [FIM]")
    
#Finalizando controle
threads[0].set_Potencia(500)
time.sleep(1)
threads[0].set_exe(0)

threads[0].join()
threads[1].join()
#------------------------------------------------------------------------------------------------------------------------------------------------

#Finalizando controle e salvando valores
threads[0].finalizar()

##Finalizando Comunicacao
#tcp.close()

#--------------------------------------------------------------------------------------------------------------------------------------------
'''print("sudo pigpiod -s 2") #Iniciando serviço PWM

print("pigs pfs 2 50") #Configurando por 2 do Raspberry
print("pigs pfs 3 50") #Configurando por 3 do Raspberry
print("pigs pfs 4 50") #Configurando por 4 do Raspberry
print("pigs pfs 5 50") #Configurando por 5 do Raspberry

print("pigs p 2 128") #Usando PWM puro  0-->255  14=Valor minimo  30=Valor maximo
print("pigs SERVO 2 128") # Usando bib SERVO 0= Desligado 500-->2500  1062=Valor minimo  2399=Valor maximo'''
