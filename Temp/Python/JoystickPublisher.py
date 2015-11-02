#!/usr/bin/env python
import sys
import atexit
import rospy
import socket
from geometry_msgs.msg import Twist

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def initConnection():
	print 'initializingConnection'
	global tcp
	HOST = '192.168.1.31'               # Endereco IP do Servidor
	PORT = 5000                         # Porta que o Servidor esta
	dest = (HOST, PORT)
	tcp.connect(dest)

def closeConnection():
	print " closingConnection"
	global tcp
	tcp.close()

def sendToQuadrotor(msg):
	print 'sendToQuadrotor'
	linearComponents = ("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
	tcp.send(linearComponents)
	angularComponents = ("Angular Components: [%f, %f, %f]"%(msg.angular.x, msg.angular.y, msg.angular.z))
	tcp.send(angularComponents)

def subscribeToJoy():
	print 'subscribeToJoy'
	rospy.init_node('new', anonymous=True)
    	rospy.Subscriber("/cmd_vel", Twist, sendToQuadrotor)
    	rospy.spin()

def joystickListener():
	print "joystickListener"

if __name__ == "__main__":
	initConnection()
	subscribeToJoy()
	atexit.register(closeConnection)

