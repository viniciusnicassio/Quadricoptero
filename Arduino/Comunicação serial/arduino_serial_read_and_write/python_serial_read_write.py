#!/usr/bin/python
import serial
import syslog
import time

#defining Arduino port, baudrate, timeout
ard = serial.Serial( '/dev/ttyACM0', 9600, timeout=5)
#time.sleep(3) #wait Arduino

enviar = 'a'

while (enviar != 's'):
    # Serial write section
    enviar = raw_input('Entre com o dado que deseja ler, sendo:\na\tacelerometro\ng\tgiroscopio\nOu digite s pra sair\n')
    if (enviar != 's'):
        ard.flush()
        print ("Enviando: " + enviar)
        ard.write(enviar)
        while (ard.inWaiting()==0):
            pass
        #Serial read section
        msg = ard.read(ard.inWaiting())
        print ("Recebida: " + msg + "\n")
else:
    print "Exiting"
ard.close()
exit()
