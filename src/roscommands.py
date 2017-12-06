#!/usr/bin/env python

import roslib; roslib.load_manifest('cloud_ros')
import rospy
from cloud_ros.srv import *
from pySpacebrew.spacebrew import Spacebrew
from std_msgs.msg import String
import rosgraph.masterapi
import time
import os
import subprocess
import threading
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

def rosCommandsFunctions(comando, brew):

	#implementar rospack list "nome"

	comandoSplit = comando.split(" ")
	if len(comandoSplit) == 1:
		data = {'comandoRos':'roscommands', 'funcao':'roscommands', 'acao':'enviar', 'commands':comandoSplit[0]}
		brew.publish("Publisher", data)
		rospy.logwarn("Comando enviado = "+comando)
	elif (comandoSplit[1] == "set_robot"):
		data = {'comandoRos':'roscommands', 'funcao':'set_robot', 'acao':'enviar', 'commands':comandoSplit[2]}
		brew.publish("Publisher", data)
		rospy.logwarn("Comando enviado = "+comando)
	else:
		rospy.logwarn("Sintaxe do comando incorreta")	
	
'''INICIO ROSCOMMANDS'''
def set_robot(brew, commands):
	global robot 
	robot = commands

def roscommands(brew, commands):
	global robot
	rospy.logwarn(robot)

	vel = Twist()
	global proc
	if(commands == "up"): 
		vel.linear.x = 2
		vel.linear.y = 0
		vel.linear.z = 0

		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = 0
	elif(commands == "down"):
		vel.linear.x = -2
		vel.linear.y = 0
		vel.linear.z = 0

		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = 0
	elif(commands == "right"):
		vel.linear.x = 0
		vel.linear.y = 0
		vel.linear.z = 0

		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = -2
	elif(commands == "left"):
		vel.linear.x = 0
		vel.linear.y = 0
		vel.linear.z = 0

		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = 2

	robots = robot.split(":")

	for rob in robots:
		pub = rospy.Publisher(rob+'/cmd_vel', Twist, queue_size=10)
		pub.publish(vel)

		vel.linear.x = 0
		vel.linear.y = 0
		vel.linear.z = 0

		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = 0
	
		time.sleep(0.5)

		pub = rospy.Publisher(rob+'/cmd_vel', Twist, queue_size=10)
		pub.publish(vel)

'''FIM ROSCOMMANDS'''


