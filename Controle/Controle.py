from threading import Thread
import serial
import random
import sys
import time
import os #Para escrever no shell
import pandas as pd #Manipulacao de arquivos
import numpy as np #Matematico

class Controle(Thread):
    #Variaveis
    #Execucao e controle
    exe=0 # Rodando Controle --> 1 Controle Parado --> 0
    ard=0 # Comunicacao serial com arduino
    
    def set_exe(self,exe):
        self.exe=exe
        
    def check(self):
        return(self.exe)
#-----------------------------------------------------------------------------------------------------------------------------------------------
    #Sensores
    ax=0 # Eixo x do acelerometro
    ay=0 # Eixo y do acelerometro
    az=0 # Eixo z do acelerometro
    
    def set_AccX(self,ax):
        self.ax=ax
        
    def get_AccX(self):
        return self.ax
            
    def set_AccY(self,ay):
        self.ay=ay
        
    def get_AccY(self):
        return self.ay
        
    def set_AccZ(self,az):
        self.az=az
        
    def get_AccZ(self):
        return self.az
#-----------------------------------------------------------------------------------------------------------------------------------------------
    gx=0 # Eixo x do giroscopio
    gy=0 # Eixo y do giroscopio
    gz=0 # Eixo z do giroscopio
    
    def set_GiroX(self,gx):
        self.gx=gx
        
    def get_GiroX(self):
        return self.gx
            
    def set_GiroY(self,gy):
        self.gy=gy
        
    def get_GiroY(self):
        return self.gy
        
    def set_GiroZ(self,gz):
        self.gz=gz
        
    def get_GiroZ(self):
        return self.gz
#-----------------------------------------------------------------------------------------------------------------------------------------------
    sf=0 # Sharp da frente
    st=0 # Sharp de traz
    se=0 # Sharp da esquerda
    sd=0 # Sharp da direta
    
    def set_SharpFrente(self,sf):
        self.sf=sf
        
    def get_SharpFrente(self):
        return self.sf
        
    def set_SharpTraz(self,st):
        self.st=st
        
    def get_SharpTraz(self):
        return self.st
        
    def set_SharpEsq(self,se):
        self.se=se
        
    def get_SharpEsq(self):
        return self.se
        
    def set_SharpDir(self,sd):
        self.sd=sd
        
    def get_SharpDir(self):
        return self.sd
#-----------------------------------------------------------------------------------------------------------------------------------------------
    pf=0 # PIR da frente
    pt=0 # PIR de traz
    pe=0 # PIR da esquerda
    pd=0 # PIR da direta
    
    def set_PirFrente(self,pf):
        self.pf=pf
        
    def get_PirFrente(self):
        return self.pf
        
    def set_PirTraz(self,pt):
        self.pt=pt
        
    def get_PirTraz(self):
        return self.pt
        
    def set_PirEsq(self,pe):
        self.pe=pe
        
    def get_PirEsq(self):
        return self.pe
        
    def set_PirDir(self,pd):
        self.pd=pd
        
    def get_PirDir(self):
        return self.pd
#-----------------------------------------------------------------------------------------------------------------------------------------------
    #Ganhos e potencia dos motores
    kp=0 
    ki=0
    kd=0
    Potencia=500
    
    def set_kp(self,kp):
        self.kp=kp
        
    def get_kp(self):
        return self.kp
        
    def set_ki(self,ki):
        self.ki=ki
        
    def get_ki(self):
        return self.ki
        
    def set_kd(self,kd):
        self.kd=kd
        
    def get_kd(self):
        return self.kd
        
    def set_Potencia(self,Potencia):
        self.Potencia=Potencia
        
    def get_Potencia(self):
        return self.Potencia
#-----------------------------------------------------------------------------------------------------------------------------------------------
    #Valores atuais no motor
    antigo_motor_1=-1
    antigo_motor_2=-1
    antigo_motor_3=-1
    antigo_motor_4=-1
    
    def get_Motor1(self):
        return self.antigo_motor_1
        
    def get_Motor2(self):
        return self.antigo_motor_2
        
    def get_Motor3(self):
        return self.antigo_motor_3
        
    def get_Motor4(self):
        return self.antigo_motor_4
        
    def get_Motores(self):
        return np.matrix([[self.antigo_motor_1],[self.antigo_motor_2],[self.antigo_motor_3],[self.antigo_motor_4]])
#-----------------------------------------------------------------------------------------------------------------------------------------------
    #Referencia
    r_x=0
    r_y=0
    r_giro_z=0
    
    def set_RefX(self,r_x):
        self.r_x=r_x

    def set_RefY(self,r_y):
        self.r_y=r_y
        
    def set_RefGiroZ(self,r_giro_z):
        self.r_giro_z=r_giro_z
#-----------------------------------------------------------------------------------------------------------------------------------------------
    #Offset dos motores
    ganhos=0
    motores=0
    
    def get_offset_Motor_1(self):
        return self.motores['Dif PWM']['Motor 1']
    
    def get_offset_Motor_2(self):
        return self.motores['Dif PWM']['Motor 2']
    
    def get_offset_Motor_3(self):
        return self.motores['Dif PWM']['Motor 3']
    
    def get_offset_Motor_4(self):
        return self.motores['Dif PWM']['Motor 4']
        
    def get_offset_Motores(self):
        return self.motores
    
#-----------------------------------------------------------------------------------------------------------------------------------------------
    #defines
#    MIN_PWM=1062 #Valor minimo para motores girar
#    MAX_PWM=2399 #Valor maximo para motores girar

    MIN_PWM=1061 #Valor minimo para motores girar
    MAX_PWM=1065 #Valor maximo para motores girar
    
    def get_MinPWM(self):
        return(self.MIN_PWM)
        
    def get_MaxPWM(self):
        return(self.MAX_PWM)
    
    FREQ_ESC=50
    PORTA_MOTOR_1=2 #Porta do motor 1
    PORTA_MOTOR_2=3 #Porta do motor 2
    PORTA_MOTOR_3=4 #Porta do motor 3
    PORTA_MOTOR_4=5 #Porta do motor 4
    
    TIME_ALARME=8 #Tempo ate o ESC comecar a apitar
#-----------------------------------------------------------------------------------------------------------------------------------------------
    def finalizar(self):
        os.system("pigs SERVO "+str(self.PORTA_MOTOR_1)+" 500 && "+"pigs SERVO "+str(self.PORTA_MOTOR_2)+" 500 && "+"pigs SERVO "+str(self.PORTA_MOTOR_3)+" 500 && "+"pigs SERVO "+str(self.PORTA_MOTOR_4)+" 500")
#        self.ard.close()
        self.salvaPWM()
        self.salvaGanhos()
        
        
    def salvaPWM(self):
        self.motores.to_csv('./data/Dif_motores.txt', sep='\t')
        
    def salvaGanhos(self):
        self.ganhos['Ganhos']['kp']=self.kp
        self.ganhos['Ganhos']['ki']=self.ki
        self.ganhos['Ganhos']['kd']=self.kd
        self.ganhos.to_csv('./data/Ganhos.txt', sep='\t')

    def printf(self,a):
        sys.stdout.write(a)
        sys.stdout.write("\n")
        sys.stdout.flush()
#-----------------------------------------------------------------------------------------------------------------------------------------------
    def __init__ (self):
        os.system("sudo pigpiod -s 2") #Iniciando servico PWM

        os.system("pigs pfs "+str(self.PORTA_MOTOR_1)+" "+str(self.FREQ_ESC)) #Configurando porta do motor 1 no Raspberry
        os.system("pigs pfs "+str(self.PORTA_MOTOR_2)+" "+str(self.FREQ_ESC)) #Configurando porta do motor 2 no Raspberry
        os.system("pigs pfs "+str(self.PORTA_MOTOR_3)+" "+str(self.FREQ_ESC)) #Configurando porta do motor 3 no Raspberry
        os.system("pigs pfs "+str(self.PORTA_MOTOR_4)+" "+str(self.FREQ_ESC)) #Configurando porta do motor 4 no Raspberry
        os.system("pigs SERVO "+str(self.PORTA_MOTOR_1)+" 500 && "+"pigs SERVO "+str(self.PORTA_MOTOR_2)+" 500 && "+"pigs SERVO "+str(self.PORTA_MOTOR_3)+" 500 && "+"pigs SERVO "+str(self.PORTA_MOTOR_4)+" 500")
        
        os.system("clear")
        self.printf("\033[1;34mAbrindo comunicacao com arduino\033[0m")
        self.printf("Qual das portas ACM abixo esta ativada ?")
        os.system("ls /dev/ttyACM*")
        self.ard = serial.Serial( '/dev/ttyACM'+raw_input("A porta ACM"), 9600, timeout=5) # Iniciando comunicacao com arduino
        
        #Refenciando
        raw_input("Coloque o drone na posicao de referencia e precione ENTER")
        self.ard.flush()
        self.ard.write("z") # Envinado arduino
        while (self.ard.inWaiting()==0):
            pass
        antigo=0
        while (self.ard.inWaiting()>antigo):
            antigo=self.ard.inWaiting()
            time.sleep(0.0050)
        serialArdFloat = float(self.ard.read(self.ard.inWaiting()))
        
        os.system("clear")
        self.printf("\033[1;34mLendo arquivos de offset\033[0m")
        if os.path.exists('./data/Dif_motores.txt'):
          self.motores=pd.read_csv('./data/Dif_motores.txt', sep='\t',index_col=0)
          self.printf('Arquivo de PWM localizado')
        else:
          self.motores=pd.DataFrame([0,0,0,0],columns=['Dif PWM'],index=['Motor 1','Motor 2','Motor 3','Motor 4'],dtype=int)
          self.printf('Arquivo de PWM nao localizado, criando valores iniciais')
        print(self.motores)
        raw_input("Precione qualquer tecla pra continuar...")
        
        os.system("clear")
        self.printf("\033[1;34mLendo arquivos de ganho\033[0m")
        if os.path.exists('./data/Ganhos.txt'):
          self.ganhos=pd.read_csv('./data/Ganhos.txt', sep='\t',index_col=0)
          self.printf('Arquivo de Ganhos localizado')
        else:
          self.ganhos=pd.DataFrame([0,0,0],columns=['Ganhos'],index=['kp','ki','kd'],dtype=float)
          self.printf('Arquivo de ganhos nao localizado, criando valores iniciais')
        print(self.ganhos)
        self.kp=self.ganhos['Ganhos']['kp']
        self.ki=self.ganhos['Ganhos']['ki']
        self.kd=self.ganhos['Ganhos']['kd']
        
        raw_input("Controle iniciado, precione qualquer tecla pra continuar...")

        Thread.__init__(self)
#-----------------------------------------------------------------------------------------------------------------------------------------------
    def teste(self):
        # Teste e calibracao
        # Checando ESC
        #Zerando
        self.exe=1
        conf=raw_input('Deseja testar todas as entradas [S/N]: ')
        if conf== "s" or conf== "S":
            os.system("clear")
            self.printf("\033[1;34mTestando ESC\033[0m")
            self.printf("Zerando valores do ESC")
            os.system("pigs SERVO "+str(self.PORTA_MOTOR_1)+" 500"+" && "+"pigs SERVO "+str(self.PORTA_MOTOR_2)+" 500"+" && "+"pigs SERVO "+str(self.PORTA_MOTOR_3)+" 500"+" && "+"pigs SERVO "+str(self.PORTA_MOTOR_4)+" 500")

            # Confirmando Sinais
            time.sleep(self.TIME_ALARME)
            conf=raw_input('Algum ESC esta apitando [S/N]: ')
            if conf=="s" or conf=="S":
                self.printf("Checar entrada do(s) ESC('s) que estao apitando")
                os._exit(1)
            self.printf("Entradas OK")
        #--------------------------------------------------------------------------------------------------------------------------------------------

        # Testando entradas
        conf=raw_input('Deseja testar a ordem dos motores [S/N]: ')
        if conf== "s" or conf== "S":
            for i in xrange(2,6):
                os.system("pigs SERVO "+str(i)+" 0")
                time.sleep(self.TIME_ALARME)
                conf=raw_input("O ESC de numero "+str(i-1)+" esta apitando [S/N]: ")
                if conf=="N"or conf=="n":
                    print("Corrigir entrada do ESC "+str(i-1))
                    os._exit(1)
                os.system("pigs SERVO "+str(i)+" 500")
#-----------------------------------------------------------------------------------------------------------------------------------------------
        conf=raw_input('Deseja o sentido de giro dos motores [S/N]: ')
        if conf== "s" or conf== "S":
            raw_input("\033[1;31mAVISO: AS HELICES IRAM GIRAR AGORA\033[0m")
            #Testando Giro
            for i in xrange(2,6):
                os.system("pigs SERVO "+str(i)+" 1063")
                conf=raw_input("O ESC de numero "+str(i-1)+" esta girando para o sentido corretamente [S/N]: ")
                if conf=="N"or conf=="n":
                    print("Corrigir entrada do ESC "+str(i-1))
                    os.system("pigs SERVO "+str(i)+" 500")
                    os._exit(1)
                os.system("pigs SERVO "+str(i)+" 500")
            conf=raw_input('Deseja girar todos [S/N]: ')
            if conf== "s" or conf== "S":
                os.system("pigs SERVO "+str(self.PORTA_MOTOR_1)+" "+str(self.MIN_PWM)+" && "+"pigs SERVO "+str(self.PORTA_MOTOR_2)+" "+str(self.MIN_PWM)+" && "+"pigs SERVO "+str(self.PORTA_MOTOR_3)+" "+str(self.MIN_PWM)+" && "+"pigs SERVO "+str(self.PORTA_MOTOR_4)+" "+str(self.MIN_PWM))
                raw_input("Precione ENTER para desligar")
                os.system("pigs SERVO "+str(self.PORTA_MOTOR_1)+" 500"+" && "+"pigs SERVO "+str(self.PORTA_MOTOR_2)+" 500"+" && "+"pigs SERVO "+str(self.PORTA_MOTOR_3)+" 500"+" && "+"pigs SERVO "+str(self.PORTA_MOTOR_4)+" 500")
                
        self.exe=0
            #-----------------------------------------------------------------------------------------------------------------------------------------------
    def run(self):
        # Funcoes de correcoes motores
        def correcaoX(Potencia_motores,cor_x):
            Potencia_motores += np.matrix([
                [-cor_x],
                [+cor_x],
                [-cor_x],
                [+cor_x],
            ])
            if (min(Potencia_motores)<self.MIN_PWM):
                Potencia_motores += self.MIN_PWM-min(Potencia_motores)
            if (max(Potencia_motores)>self.MAX_PWM):
                Potencia_motores -= max(Potencia_motores)-self.MAX_PWM
            return(Potencia_motores)

        def correcaoY(Potencia_motores,cor_y):
            Potencia_motores += np.matrix([
                [+cor_y],
                [+cor_y],
                [-cor_y],
                [-cor_y],
            ])
            if (min(Potencia_motores)<self.MIN_PWM):
                Potencia_motores += self.MIN_PWM-min(Potencia_motores)
            if (max(Potencia_motores)>self.MAX_PWM):
                Potencia_motores -= max(Potencia_motores)-self.MAX_PWM
            return(Potencia_motores)

        def correcaoGiro(Potencia_motores,cor_giro_z):
            Potencia_motores += np.matrix([
                [-cor_giro_z],
                [+cor_giro_z],
                [-cor_giro_z],
                [+cor_giro_z],
            ])            
            if (min(Potencia_motores)<MIN_PWM):
                Potencia_motores += MIN_PWM-min(Potencia_motores)
            if (max(Potencia_motores)>MAX_PWM):
                Potencia_motores -= max(Potencia_motores)-MAX_PWM
            return(Potencia_motores)
#---------------------------------------------------------------------------------------------------------------------------------------------    
        #Leitura Arduino
        def lerSensores(a,ard):
            ard.flush()
            ard.write(a) # Envinado arduino
            while (ard.inWaiting()==0):
                pass
            antigo=0
            while (ard.inWaiting()>antigo):
                antigo=ard.inWaiting()
                time.sleep(0.0050)
            serialArdFloat = float(ard.read(ard.inWaiting()))
            varA = float(serialArdFloat) - (float(serialArdFloat) - int(serialArdFloat))
            return int(varA) # gravando resposta
#---------------------------------------------------------------------------------------------------------------------------------------------            
        # Funcoes dos motores
        def motorMovimento(Potencia, cor_x, cor_y, cor_giro_z):
            if Potencia>=self.MIN_PWM:
                offset_motores=np.matrix([
                [self.motores['Dif PWM']['Motor 1']],
                [self.motores['Dif PWM']['Motor 2']],
                [self.motores['Dif PWM']['Motor 3']],
                [self.motores['Dif PWM']['Motor 4']],
                ])
                Potencia_motores=Potencia+offset_motores
                #Corringindo em X
                Potencia_motores=correcaoX(Potencia_motores,cor_x)
                #Corringindo em y
                Potencia_motores=correcaoY(Potencia_motores,cor_y)
                #Corringindo em giro
                Potencia_motores=correcaoGiro(Potencia_motores,cor_giro_z)
                
            elif Potencia==0:
                Potencia_motores=np.matrix([
                [0],
                [0],
                [0],
                [0],
                ])
            
            else:
                Potencia_motores=np.matrix([
                [500],
                [500],
                [500],
                [500],
                ])
            if self.antigo_motor_1!=Potencia_motores[0,0] or self.antigo_motor_2!=Potencia_motores[1,0] or self.antigo_motor_3!=Potencia_motores[2,0] or self.antigo_motor_4!=Potencia_motores[3,0]:
                os.system("pigs SERVO 2 "+ str(Potencia_motores[0,0])+" && "+"pigs SERVO 3 "+ str(Potencia_motores[1,0])+" && "+"pigs SERVO 4 "+ str(Potencia_motores[2,0])+" && "+"pigs SERVO 5 "+ str(Potencia_motores[3,0]))
                self.antigo_motor_1=Potencia_motores[0,0]
                self.antigo_motor_2=Potencia_motores[1,0]
                self.antigo_motor_3=Potencia_motores[2,0]
                self.antigo_motor_4=Potencia_motores[3,0]
            return(Potencia_motores)

        def motorParado(Potencia, cor_x, cor_y, cor_giro_z):
            if Potencia>=self.MIN_PWM:
                self.motores['Dif PWM']['Motor 1'] += +cor_x -cor_y +cor_giro_z
                self.motores['Dif PWM']['Motor 2'] += -cor_x +cor_y -cor_giro_z
                self.motores['Dif PWM']['Motor 3'] += +cor_x -cor_y +cor_giro_z
                self.motores['Dif PWM']['Motor 4'] += -cor_x +cor_y -cor_giro_z
                print(self.motores)
                #print(-cor_x +cor_y -cor_giro_z)
                offset_motores=np.matrix([
                [self.motores['Dif PWM']['Motor 1']],
                [self.motores['Dif PWM']['Motor 2']],
                [self.motores['Dif PWM']['Motor 3']],
                [self.motores['Dif PWM']['Motor 4']],
                ])
                Potencia_motores=Potencia+offset_motores
                #Corringindo valores
                Potencia_motores=correcaoX(Potencia_motores,0)
                
            elif Potencia==0:
                Potencia_motores=np.matrix([
                [0],
                [0],
                [0],
                [0],
                ])
                
            else:
                Potencia_motores=np.matrix([
                [500],
                [500],
                [500],
                [500],
                ])
            if self.antigo_motor_1!=Potencia_motores[0,0] or self.antigo_motor_2!=Potencia_motores[1,0] or self.antigo_motor_3!=Potencia_motores.item((2,0)) or self.antigo_motor_4!=Potencia_motores.item((3,0)):
                os.system("pigs SERVO 2 "+ str(Potencia_motores[0,0])+" && "+"pigs SERVO 3 "+ str(Potencia_motores[1,0])+" && "+"pigs SERVO 4 "+ str(Potencia_motores[2,0])+" && "+"pigs SERVO 5 "+ str(Potencia_motores[3,0]))
                self.antigo_motor_1=Potencia_motores[0,0]
                self.antigo_motor_2=Potencia_motores[1,0]
                self.antigo_motor_3=Potencia_motores[2,0]
                self.antigo_motor_4=Potencia_motores[3,0]
            return(Potencia_motores)
#---------------------------------------------------------------------------------------------------------------------------------------------
        def correcao(erro, somaErro, d_erro, kp, ki, kd):
            return int(kp*erro + somaErro*ki + d_erro*kd)
#---------------------------------------------------------------------------------------------------------------------------------------------                
        # Inicio programa
        self.exe=1
        lerSensores("z",self.ard)
        while self.exe==1:
            #Atualizando valores
            # Acelerometro
            self.ax = lerSensores("ax",self.ard) # Lendo valor x do acc
            self.ay = lerSensores("ay",self.ard) # Lendo valor y do acc
            #print(self.ay)
            self.az = lerSensores("az",self.ard) # Lendo valor z do acc
            
            # Giroscopio
            self.gx = lerSensores("gx",self.ard) # Lendo valor x do giro
            self.gy = lerSensores("gy",self.ard) # Lendo valor y do giro
            self.gz = lerSensores("gz",self.ard) # Lendo valor z do giro
                    
            # Pir
#            self.pf = lerSensores("pf",self.ard) # Lendo valor Pir frente
#            self.pt = lerSensores("pt",self.ard) # Lendo valor Pir traz
#            self.pe = lerSensores("pe",self.ard) # Lendo valor Pir esquerda
#            self.pd = lerSensores("pd",self.ard) # Lendo valor Pir direita
#            
#            # Sharp
#            self.sf = lerSensores("sf",self.ard) # Lendo valor sharp frente
#            self.st = lerSensores("st",self.ard) # Lendo valor sharp traz
#            self.se = lerSensores("se",self.ard) # Lendo valor sharp esquerda
#            self.sd = lerSensores("sd",self.ard) # Lendo valor sharp direita
        
            # Calulando erros
            erro_x=self.r_x-self.ax
            erro_y=self.r_y-self.ay
            erro_giro_z=self.r_giro_z-self.gz

            #Calculando correcoes
            cor_x = correcao(erro_x, 0, 0, self.kp, self.ki, self.kd)
            cor_y = correcao(erro_y, 0, 0, self.kp, self.ki, self.kd)
            cor_giro_z = correcao(erro_giro_z, 0, 0, self.kp, self.ki, self.kd)
            
            #Calculando correcoes
#            cor_x = correcao(erro_x, somaErro_x, d_erro_x, kp, ki, kd)
#            cor_y = correcao(erro_y, somaErro_y, d_erro_y, kp, ki, kd)
#            cor_z = correcao(erro_z, somaErro_z, d_erro_z, kp, ki, kd)
        
            #Calulando erros
#            erro_x=self.r_x-0
#            erro_y=self.r_y-0
#            erro_giro_z=self.r_giro_z-0
    #        erro_x=self.r_x-ax
    #        erro_y=self.r_y-ay
    #        erro_giro_z=self.r_giro_z-gz
        
            #Calculando correcoes
#            cor_x = correcao(erro_x, 0, 0, self.kp, 0, 0)
#            cor_y = correcao(erro_y, 0, 0, self.kp, 0, 0)
#            cor_giro_z = correcao(erro_giro_z, 0, 0, self.kp, 0, 0)
            
            #Manda para motores
            if (self.r_x==0 and self.r_y==0 and self.r_giro_z==0):
                motorParado(self.Potencia, cor_x, cor_y, cor_giro_z)
            else:
                motorMovimento(self.Potencia, cor_x, cor_y, cor_giro_z)

            time.sleep(0.05)
        self.exe=0
