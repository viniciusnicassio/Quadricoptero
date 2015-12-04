#!/usr/bin/python
import serial
import syslog
import time
import os

#defining Arduino port, baudrate, timeout
baudrate=115200
ard = serial.Serial( '/dev/ttyACM0', baudrate, timeout=5)

enviar = 'a'
ard.write("z")

while (enviar != 's'):
    # Serial write section
    time.sleep(1)
    enviar = "c"
#    enviar = raw_input('Entre com o dado que deseja ler, sendo:\na\tacelerometro\ng\tgiroscopio\nc\tciclo\nOu digite s pra sair\n')
    os.system("clear")
    if (enviar != 's' and enviar != 'c'):
        print ("Enviando: " + enviar)
        #ard.write(enviar)
        ard.write(enviar)
        while (ard.inWaiting()==0):
            pass
        antigo=0
        while (ard.inWaiting()>antigo):
            antigo=ard.inWaiting()
            time.sleep(0.0010)
        #Serial read section
        msg = ard.read(ard.inWaiting())
        print ("Recebida: " + msg + "\n")
        ard.flush()
        
    elif enviar == 'c':
        collection = ["ax", "4193817", "ay"]
        for enviar in collection:
            print ("Enviando: " + enviar)
            #ard.write(enviar)
            ard.write(enviar)
            while (ard.inWaiting()==0):
                pass
            antigo=0
            while (ard.inWaiting()>antigo):
                antigo=ard.inWaiting()
                time.sleep(0.0010)
            #Serial read section
            msg = ard.read(ard.inWaiting())
            print ("Recebida: " + msg + "\n")
            ard.flush()
    else:
        print "Exiting"
ard.close()
exit()
