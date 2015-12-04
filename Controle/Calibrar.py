from threading import Thread
import sys
import time
import os #Para escrever no shell
import getch

class Calibrar(Thread):
    #variaveis
    #defines
    MIN_PWM=0 #Valor minimo para motores girar
    MAX_PWM=0 #Valor maximo para motores girar
    
    def set_MinPWM (self, MIN_PWM):
        self.MIN_PWM=MIN_PWM
        
    def set_MaxPWM (self, MAX_PWM):
        self.MAX_PWM=MAX_PWM
    
    exe=0
    
    Potencia=0
    passo=1
    kp=0.1
    ki=0.0
    kd=0.0
    
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
        
    #Valores atuais no motor
    antigo_motor_1=-1
    antigo_motor_2=-1
    antigo_motor_3=-1
    antigo_motor_4=-1
    
    def set_Motor1(self,antigo_motor_1):
        self.antigo_motor_1=antigo_motor_1
        
    def set_Motor2(self,antigo_motor_2):
        self.antigo_motor_2=antigo_motor_2
        
    def set_Motor3(self,antigo_motor_3):
        self.antigo_motor_3=antigo_motor_3
        
    def set_Motor4(self,antigo_motor_4):
        self.antigo_motor_4=antigo_motor_4

    conf="a"
    
    # Funcoes get e set
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

    #Funcoes de controle de potencia
    def aumentarPotencia(self,Potencia,passo):
        Potencia+=passo
        if Potencia>self.MAX_PWM:
            Potencia=self.MAX_PWM
        if Potencia<self.MIN_PWM:
            Potencia=self.MIN_PWM
        return (Potencia)

    def diminuirPotencia(self,Potencia,passo):
        if Potencia>self.MIN_PWM:
            Potencia-=passo
            if Potencia>self.MAX_PWM:
                Potencia=self.MAX_PWM
            if Potencia<self.MIN_PWM:
                Potencia=self.MIN_PWM
        return (Potencia)

    def parar(self):
        return (500)

    def desligar(self):
        return (0)
#--------------------------------------------------------------------------------------------------------------------------------------------
    
    def printf(self,a):
        sys.stdout.write(a)
        sys.stdout.flush()
        
    def check(self):
        return(self.exe)
    
    def __init__ (self):
        Thread.__init__(self)

    def run(self):
        self.exe=1
        
        while self.conf!="b" and self.conf!="B":
            os.system("clear") #Limpando
            self.printf("\033[1;34mCalibracao\033[0m\n\n\033[0;32mPotencia atual: "+str(self.Potencia)+"\nKp atual: "+str(self.kp)+"\nKi atual: "+str(self.ki)+"\nKd atual: "+str(self.kd)+"\033[0m\n\nw -->\tSubir\ns -->\tDescer\nd -->\tDesligar\np -->\tParar\no -->\tAjustar passo, passo atual: 1\nk -->\tAjustar ganhos\nb -->\tSair\n\nDigite a funcao desejada: ")
            self.conf=raw_input()
            if self.conf=="w":
                self.Potencia=self.aumentarPotencia(self.Potencia,self.passo)
            elif self.conf=="s":
                self.Potencia=self.diminuirPotencia(self.Potencia,self.passo)
            elif self.conf=="d":
                self.Potencia=self.desligar()
            elif self.conf=="p":
                self.Potencia=self.parar()
            elif self.conf=="o":
                self.passo=input("Digite o novo passo: ")
                while self.passo<=0:
                    self.passo=input("Valor incoerente, digite um novo passo: ")
            elif self.conf=="k":
                self.printf("p -->\tAlterar ganho proporcional\ni -->\tAlterar ganho integral\nd -->\tAlterar ganho derivativo\n\nQual ganho deseja alterar: ")
                self.conf=raw_input()
                if self.conf=="p":
                    self.kp=input("Digite o novo Kp: ")
                    while self.kp<0:
                        self.kp=input("Valor incoerente, digite um novo Kp: ")
                if self.conf=="i":
                    self.ki=input("Digite o novo Ki: ")
                    while self.ki<0:
                        self.ki=input("Valor incoerente, digite um novo Ki: ")
                if self.conf=="d":
                    self.kd=input("Digite o novo Kd: ")
                    while self.kd<0:
                        self.kd=input("Valor incoerente, digite um novo Kd: ")
            elif self.conf!="b":
                self.printf("Comando invalido")    
        
        self.exe=0
