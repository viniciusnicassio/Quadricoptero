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
#  * @brief Controle
#  ****************************************************************************
#  Program to execute the Controle process
# ****************************************************************************

#import parser for arguments
import numpy as np #Matematico
import pandas as pd #Manipulação de arquivos
import os.path #Checar a existencia
import time #tempo
import os #Para escrever no shell
import getch #Para usar a função getchar --> getch.getche()

#Constantes

min_PWM=1062 #Valor minimo para motores girar
max_PWM=2399 #Valor maximo para motores girar
time_alarme=1 #Tempo até o ESC começar a apitar

# Funções de correções
def correcaoX(Potencia_motores,cor_x):
    Potencia_motores += np.matrix([
        [-cor_x],
        [+cor_x],
        [+cor_x],
        [-cor_x],
    ])
    if (min(Potencia_motores)<min_PWM):
        print(str(min_PWM-min(Potencia_motores))+" abaixo em x")
        Potencia_motores += min_PWM-min(Potencia_motores)
    if (max(Potencia_motores)>max_PWM):
        print(str(max(Potencia_motores)-max_PWM)+" a cima em x")
        Potencia_motores -= max(Potencia_motores)-max_PWM
    return(Potencia_motores)

def correcaoY(Potencia_motores,cor_y):
    Potencia_motores += np.matrix([
        [+cor_y],
        [+cor_y],
        [-cor_y],
        [-cor_y],
    ])
    if (min(Potencia_motores)<min_PWM):
        print(str(min_PWM-min(Potencia_motores))+" abaixo em y")
        Potencia_motores += min_PWM-min(Potencia_motores)
    if (max(Potencia_motores)>max_PWM):
        print(str(max(Potencia_motores)-max_PWM)+" a cima em y")
        Potencia_motores -= max(Potencia_motores)-max_PWM
    return(Potencia_motores)

def correcaoGiro(Potencia_motores,giro):
    Potencia_motores += np.matrix([
        [-giro],
        [+giro],
        [-giro],
        [+giro],
    ])
    if (min(Potencia_motores)<min_PWM):
        print(str(min_PWM-min(Potencia_motores))+" abaixo em giro")
        Potencia_motores += min_PWM-min(Potencia_motores)
    if (max(Potencia_motores)>max_PWM):
        print(str(max(Potencia_motores)-max_PWM)+" a cima em abaixo em giro")
        Potencia_motores -= max(Potencia_motores)-max_PWM
    return(Potencia_motores)
#--------------------------------------------------------------------------------------------------------------------------------------------

# Funções dos motores
def motorMovimento(Potencia, cor_x, cor_y, giro):
    if Potencia>=min_PWM:
        offset_motores=np.matrix([
        [motores['Dif PWM']['Motor 1']],
        [motores['Dif PWM']['Motor 2']],
        [motores['Dif PWM']['Motor 3']],
        [motores['Dif PWM']['Motor 4']],
        ])
        Potencia_motores=Potencia+offset_motores
        #Corringindo em X
        Potencia_motores=correcaoX(Potencia_motores,cor_x)
        #Corringindo em y
        Potencia_motores=correcaoY(Potencia_motores,cor_y)
        #Corringindo em giro
        Potencia_motores=correcaoGiro(Potencia_motores,giro)
        
    else:
        Potencia_motores=np.matrix([
        [500],
        [500],
        [500],
        [500],
        ])
    
    return(Potencia_motores)

def motorParado(Potencia, cor_x, cor_y, giro):
    if Potencia>=min_PWM:
        motores['Dif PWM']['Motor 1'] += -cor_x +cor_y -giro
        motores['Dif PWM']['Motor 2'] += +cor_x +cor_y +giro
        motores['Dif PWM']['Motor 3'] += +cor_x -cor_y -giro
        motores['Dif PWM']['Motor 4'] += -cor_x -cor_y +giro
        offset_motores=np.matrix([
        [motores['Dif PWM']['Motor 1']],
        [motores['Dif PWM']['Motor 2']],
        [motores['Dif PWM']['Motor 3']],
        [motores['Dif PWM']['Motor 4']],
        ])
        Potencia_motores=Potencia+offset_motores
        #Corringindo valores
        Potencia_motores=correcaoX(Potencia_motores,0)
    else:
        Potencia_motores=np.matrix([
        [500],
        [500],
        [500],
        [500],
        ])
    
    return(Potencia_motores)
#--------------------------------------------------------------------------------------------------------------------------------------------



# Inicio do programa:

# Lendo arquivos
#PWM
os.system("clear")
print("\033[1;34mLendo arquivos de offset\033[0m")
if os.path.exists('./data/Dif_motores.txt'):
  motores=pd.read_csv('./data/Dif_motores.txt', sep='\t',index_col=0)
  print('Arquivo localizado')
else:
  motores=pd.DataFrame([0,0,0,0],columns=['Dif PWM'],index=['Motor 1','Motor 2','Motor 3','Motor 4'],dtype=int)
  print('Arquivo não localizado, criando valores iniciais')
print(motores)
raw_input()
#--------------------------------------------------------------------------------------------------------------------------------------------

#Iniciando serviços
os.system("clear")
print("\033[1;34mIniciando serviços\033[0m")

os.system("sudo pigpiod -s 2") #Iniciando serviço PWM

os.system("pigs pfs 2 50") #Configurando por 2 do Raspberry
os.system("pigs pfs 3 50") #Configurando por 3 do Raspberry
os.system("pigs pfs 4 50") #Configurando por 4 do Raspberry
os.system("pigs pfs 5 50") #Configurando por 5 do Raspberry
raw_input()
#--------------------------------------------------------------------------------------------------------------------------------------------

# Teste e calibração
# Checando ESC
#Zerando
os.system("clear")
print("\033[1;34mTestando ESC\033[0m")
print("Zerando valores do ESC")
os.system("pigs SERVO 2 500")
os.system("pigs SERVO 3 500")
os.system("pigs SERVO 4 500")
os.system("pigs SERVO 5 500")

# Confirmando Sinais
time.sleep(time_alarme)
conf=raw_input('Algum ESC está apitando [S/N]: ')
if conf=="s":
    print("Checar entrada do(s) ESC('s) que estão apitando")
    os._exit(1)
elif conf=="S":
    print("Checar entrada do(s) ESC('s') que estão apitando")
    os._exit(1)
#--------------------------------------------------------------------------------------------------------------------------------------------


# Testando entradas
for i in xrange(2,6):
    os.system("pigs SERVO "+str(i)+" 0")
    time.sleep(time_alarme)
    conf=raw_input("O ESC de numero "+str(i-1)+" está apitando [S/N]: ")
    if conf=="N":
        print("Corrigir entrada do ESC "+str(i-1))
        os._exit(1)
    elif conf=="n":
        print("Corrigir entrada do ESC "+str(i-1))
        os._exit(1)
    os.system("pigs SERVO "+str(i)+" 500")
print("Entradas e ordens verificas")
#--------------------------------------------------------------------------------------------------------------------------------------------

#Calibrando
print("Calibrando aqui")

#--------------------------------------------------------------------------------------------------------------------------------------------

# Controle
print("Controle aqui")
#--------------------------------------------------------------------------------------------------------------------------------------------

# Salvando arquivos
#PWM
motores.to_csv('./data/Dif_motores.txt', sep='\t')
#--------------------------------------------------------------------------------------------------------------------------------------------
'''print("sudo pigpiod -s 2") #Iniciando serviço PWM

print("pigs pfs 2 50") #Configurando por 2 do Raspberry
print("pigs pfs 3 50") #Configurando por 3 do Raspberry
print("pigs pfs 4 50") #Configurando por 4 do Raspberry
print("pigs pfs 5 50") #Configurando por 5 do Raspberry

print("pigs p 2 128") #Usando PWM puro  0-->255  14=Valor minimo  30=Valor maximo
print("pigs SERVO 2 128") # Usando bib SERVO 0= Desligado 500-->2500  1062=Valor minimo  2399=Valor maximo'''
