#!/usr/bin/env python

# Nodo para ROS que recibe un mensaje geometrico y en funsion de estos adecua el valor a los motores del dreamster 
# Envia los nuevos valores por serial al dreamster 

import rospy, serial, time
from geometry_msgs.msg import Twist

base_diameter = 0.105 #In meters
wheel_radius = 0.038  #In meters
header = 255 #Defino el header para indicarle al dreamster que inicia la comunicacion
###############################################################################
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", str(data.linear))	# escribe: I heard "lo que recibio"

###############################################################################
def receiver:
	rospy.init_node('Velocity_serial', anonymous=True)			# se inicializa el nodo con nombre "Velocity_serial"
	rospy.Subscriber("chatter_vel", Twist, callback)	# se subscribe al canal "chatter_vel" y tiene que recibir un String y llama a callback
	

# Se calcula la velocidad de cada rueda indep, con la posicion lineal y anguular
# Lo que recibo lo leo como data y si quiero velocidad deberia poner data.linear 
def get_wheels_vel(data.linear_vel_x, data.ang_vel_z):
    if data.linear_vel_x < 0:
        data.ang_vel_z = -data.ang_vel_z
    aux_r_wheel_vel = 0.5*(((2*data.linear_vel_x)/wheel_radius) - ((data.ang_vel_z*base_diameter)/wheel_radius))
    aux_l_wheel_vel = 0.5*(((2*data.linear_vel_x)/wheel_radius) + ((data.ang_vel_z*base_diameter)/wheel_radius))
    l_wheel_vel = int(2.5*aux_l_wheel_vel)
    r_wheel_vel = int(2.5*aux_r_wheel_vel)
    return l_wheel_vel, r_wheel_vel
###############################################################################
def Serial_send:
    import serial
    ser = serial.Serial()  # open first serial port
    ser.port = "/dev/ttyACM0" # indica el puerto del dreamster
    ser.open()
    ser.write(header)
    ser.write(l_wheel_vel)
    ser.write(r_wheel_vel)      # escribe en el puerto los dos valores de velocidad
    ser.close()             # close port
###############################################################################
def Velocity_control_node():
	global base_diameter
    global wheel_radius

    while not rospy.is_shutdown():
		receiver()			# Recibe info de otro nodo
		data.linear_vel,data.angular_vel=get_wheels_vel() #genera los nuevos valores para las velocidades 
		Serial_send()			# Envia por serie al dreamster
    rospy.spin()		# evita que se cierre el nodo
    file.close()		# se cierra el archivo al salir del nodo

if __name__ == '__main__':
	#try:
		#PWM_control_node()
    #except rospy.ROSInterruptException:
    #    stop_motors()
    #    PWM.cleanup()


