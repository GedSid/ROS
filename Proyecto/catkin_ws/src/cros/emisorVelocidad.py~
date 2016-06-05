#!/usr/bin/env python

# Nodo para ROS que recibe un mensaje geometrico y en funsion genera un PWM
# Usa pi-blaster, asi que necesita tenerlo instalado y corriendo

import rospy, sys, traceback
from geometry_msgs.msg import Twist

import numpy as np
from math import atan2, pi

base_diameter = 0.20 #In meters
wheel_radius = 0.04  #In meters

###############################################################################
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", str(data.linear))	# escribe: I heard "lo que recibio"

###############################################################################
def receiver:
	rospy.init_node('Velocity', anonymous=True)			# se inicializa el nodo con nombre "nodo3"
	rospy.Subscriber("chatter_vel", Twist, callback)	# se subscribe al canal "chatter_vel" y tiene que recibir un String y llama a callback


# Se calcula la velocidad de cada rueda indep, con la posicion lineal y anguular
def get_wheels_vel(linear_vel_x, ang_vel_z):
    if linear_vel_x < 0:
        ang_vel_z = -ang_vel_z
    aux_r_wheel_vel = 0.5*(((2*linear_vel_x)/wheel_radius) - ((ang_vel_z*base_diameter)/wheel_radius))
    aux_l_wheel_vel = 0.5*(((2*linear_vel_x)/wheel_radius) + ((ang_vel_z*base_diameter)/wheel_radius))
    l_wheel_vel = 2.5*aux_l_wheel_vel
    r_wheel_vel = 2.5*aux_r_wheel_vel
    return l_wheel_vel, r_wheel_vel
###############################################################################
def EL QUE ENVIA POR PUERTO SERIE 
    import serial
    ser = serial.Serial(0)  # open first serial port
    print ser.portstr       # check which port was really used
    ser.write("hello")      # write a string
    ser.close()             # close port
###############################################################################
def Velocity_control_node():
	global base_diameter
    global wheel_radius

    while not rospy.is_shutdown():
		receiver()			# Recibe info de otro nodo
		linear_vel,angular_vel=get_wheels_vel() #genera los nuevos valores para las velocidades 
		ENVIO POR PUERTO SERIE LO QUE RECIBI			# Carga el valor del PWM
    rospy.spin()		# evita que se cierre el nodo
    file.close()		# se cierra el archivo al salir del nodo

if __name__ == '__main__':
	#try:
		PWM_control_node()
    #except rospy.ROSInterruptException:
    #    stop_motors()
    #    PWM.cleanup()


# la formula para calcular la velocidad usada en oects_detector es vr=(2v+wL)/2R y vl=(2v-wL)/2R

#https://github.com/mwilliams03/pi-blaster
#http://ozzmaker.com/software-pwm-on-a-raspberry-pi/
#Channel number    GPIO number   Pin in P1 header
#      0               4             P1-7
#      1              17             P1-11
#      2              18             P1-12
#      3              21             P1-13
#      4              22             P1-15
#      5              23             P1-16
#      6              24             P1-18
#      7              25             P1-22
