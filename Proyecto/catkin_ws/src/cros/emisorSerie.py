#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
import sys

def talker():
    pub = rospy.Publisher('chatter_vel', Twist, queue_size=10)	# defino que va a publicar un twist en el canal "chatter_vel"
    rospy.init_node('move_control', anonymous=True)			# se inicializa el nodo con nombre "move_control"
    rate = rospy.Rate(1) # 1hz					# defino la frecuencia a la que envio los datos
    while not rospy.is_shutdown():
        #quiero que la velocidad la ingrese por teclado
        vel_linear='a'
        while (vel_linear.isdigit() == False):
            vel_linear=raw_input('Ingresar la velocidad lineal en numero [m/s]: ')#pido que ingrese la velocidad en teclado

        print ('Velocidad lineal %s [m/s] \n ' % (vel_linear))
    
        vel_angular='a'
        while (vel_angular.isdigit() == False):
            vel_angular=raw_input('Ingresar la velocidad angular en numero [m/s]: ')#pido que ingrese la velocidad en teclado

        print ('Velocidad angular %s [m/s] \n ' % (vel_angular))
    
        # HABRIA QUE HACER CALCULO MEDIANTE EL DARIO DE LAS RUEDAS PARA TRANSFORMAR LA VELOCIDAD EN METROS POR SEGUNDO A EL VALOR DE TWIST
        new_vel = Twist()
        new_vel.linear.x = int(vel_linear)
        new_vel.angular.z = int(vel_angular)
    
        rospy.loginfo(new_vel)					# cargo e imprimo el mensaje
        pub.publish(new_vel)					# publico el mensaje
        rate.sleep()						# espero la frecuencia que defini

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
