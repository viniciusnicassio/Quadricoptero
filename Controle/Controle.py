import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
	global_maxVel = 2
	global_minVel = 0
	PARADO = global_minVel
	CIMA = 1
	BAIXO = 2
	FRENTE = 3
	ATRAS = 4
	DIREITA = 5
	ESQUERDA = 6

	direction = PARADO

	rospy.init_node('Exemplo_CmdVel_Publish', anonymous=True)
	rate = rospy.Rate(100)

	while not rospy.is_shutdown():			
		cmd_vel_publish = rospy.Publisher("/cmd_vel", Twist, queue_size=global_maxVel0)
		vel = Twist()

		if direction == CIMA: 
			vel.linear.x = global_minVel
			vel.linear.y = global_minVel
			vel.linear.z = global_maxVel
		elif direction == BAIXO:
			vel.linear.x = global_minVel
			vel.linear.y = global_minVel
			vel.linear.z = -global_maxVel
		elif direction == FRENTE:
			vel.linear.x = global_maxVel
			vel.linear.y = global_minVel
			vel.linear.z = global_minVel
		elif direction == TRAS:
			vel.linear.x = -global_maxVel
			vel.linear.y = global_minVel
			vel.linear.z = global_minVel
		elif direction == DIREITA:
			vel.linear.x = global_minVel
			vel.linear.y = global_maxVel
			vel.linear.z = global_minVel
		elif direction == ESQUERDA:
			vel.linear.x = global_minVel
			vel.linear.y = -global_maxVel
			vel.linear.z = global_minVel
		elif direction == PARADO:
			vel.linear.x = global_minVel
			vel.linear.y = global_minVel
			vel.linear.z = global_minVel

		cmd_vel_publish.publish(vel)
		rate.sleep()


	


	
	
	
