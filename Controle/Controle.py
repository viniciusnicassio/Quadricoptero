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



# Lendo
#PWM
if os.path.exists('./data/Dif_motores.txt'):
  motores=pd.read_csv('./data/Dif_motores.txt', sep='\t',index_col=0)
  print('Arquivo localizado')
else:
  motores = pd.DataFrame([0,0,0,0],columns=['Dif PWM'],index=['Motor 1','Motor 2','Motor 3','Motor 4'],dtype=int)
  print('Arquivo não localizado, criando valores iniciais')

# Controle
a=1
while(a):
  print("Controle aqui")
  a=0
  print(motores)
  print(motores['Dif PWM']['Motor 2'])

# Salvando arquivos
#PWM
motores.to_csv('./data/Dif_motores.txt', sep='\t')
