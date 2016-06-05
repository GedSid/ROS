#!/usr/bin/env python
import rospy, sys, traceback
from geometry_msgs.msg import Twist

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", str(data.linear))	# escribe: I heard "lo que recibio"
    
def main():
    #Recive:
    rospy.init_node('nodo3', anonymous=True)		# se inicializa el nodo con nombre "nodo3"
    rospy.Subscriber("chatter_vel", Twist, callback)	# se subscribe al canal "chatter_vel" y tiene que recibir un String y llama a callback
    
    
    #Pone el PWM en el pin:
    try
	PWM_Salida = open(/dev/pi-blaster, w)		# se abre en la variable PWM_Salida el archivo /dev/pi-blaster en modo escritura
    except
        print "No se a ejecutado pi-blaster"		# se puede cambiar por un mensaje de error de ros
	sys.exit()
    #To set pin1 to a PWM of 20%
    #echo "PIN=DUTY_CICLE" > /dev/pi-blaster
    PWM_Salida.write("PIN=DUTY_CICLE")			# se escribe "PIN=DUTY_CICLE" en PWM_Salida

    rospy.spin()					# evita que se cierre el nodo
    file.close()					# se cierra el archivo al salir del nodo

if __name__ == '__main__':
    main()
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
