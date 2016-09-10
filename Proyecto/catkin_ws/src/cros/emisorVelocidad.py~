#!/usr/bin/env python

# Nodo para ROS que recibe un mensaje geometrico y en funsion de estos adecua el valor a los motores del dreamster 
# Envia los nuevos valores por serial al dreamster 

import rospy, serial, time
from geometry_msgs.msg import Twist

base_diameter = 0.105 #In meters
wheel_radius = 0.038  #In meters
header = 255 #Defino el header para indicarle al dreamster que inicia la comunicacion
###############################################################################
def procesar_mensaje(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", str(data.linear.x))	# escribe: I heard "lo que recibio"
    data_procesada = get_wheels_vel(data) #genera los nuevos valores para las velocidades 
    Serial_send(data_procesada)			# Envia por serie al dreamster

###############################################################################
def receiver():
    rospy.init_node('Velocity_serial', anonymous=True)			# se inicializa el nodo con nombre "Velocity_serial"
    rospy.Subscriber("chatter_vel", Twist, procesar_mensaje)	# se subscribe al canal "chatter_vel" y tiene que recibir un String y llama a callback
	

# Se calcula la velocidad de cada rueda indep, con la posicion lineal y anguular
# Lo que recibo lo leo como data y si quiero velocidad deberia poner data.linear 
def get_wheels_vel(data):
    if data.linear.x < 0:
        data.angular.z = -data.angular.z
    aux_r_wheel_vel = 0.5*(((2*data.linear.x)/wheel_radius) - ((data.angular.z*base_diameter)/wheel_radius))
    aux_l_wheel_vel = 0.5*(((2*data.linear.x)/wheel_radius) + ((data.angular.z*base_diameter)/wheel_radius))
    l_wheel_vel = int(1.5*aux_l_wheel_vel)
    r_wheel_vel = int(1.5*aux_r_wheel_vel)
    return (l_wheel_vel, r_wheel_vel)
###############################################################################
def Serial_send(data):
    l_wheel_vel, r_wheel_vel = data
    import serial
    ser = serial.Serial()  # open first serial port
    ser.port = "/dev/ttyACM1" # indica el puerto del dreamster
    ser.open()
    
    print("valores: ", l_wheel_vel, r_wheel_vel, " chrValores: ", str(l_wheel_vel), str(r_wheel_vel))

    ser.write(chr(header))
    ser.write(str(l_wheel_vel))
    ser.write('/')
    #ser.write(str(r_wheel_vel))      # escribe en el puerto los dos valores de velocidad
    #ser.write('/')
    ser.close()             # close port
###############################################################################
def Velocity_control_node():
    global base_diameter
    global wheel_radius

    receiver()			# Recibe info de otro nodo
    while not rospy.is_shutdown():
        time.sleep(0.1)
    rospy.spin()		# evita que se cierre el nodo
    file.close()		# se cierra el archivo al salir del nodo

if __name__ == '__main__':
    try:
        Velocity_control_node()
    except rospy.ROSInterruptException:
        pass

