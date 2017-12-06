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

def rosserviceFunctions(comando, brew):
	global stop_
	stop_ = False

	comandoSplit = comando.split(" ")
	if comandoSplit[1] == "list":
		data = {'comandoRos':'rosservice', 'funcao':'rosserviceList', 'acao':'enviar', 'service':'', 'args':''}
		brew.publish("Publisher", data)
		rospy.logwarn("Comando enviado = "+comando)

	elif comandoSplit[1] == "args":
		if len(comandoSplit) != 3:
			rospy.logwarn("sintaxe = rosservice args /service")
		else:
			data = {'comandoRos':'rosservice', 'funcao':'rosserviceArgs', 'acao':'enviar', 'service':comandoSplit[2], 'args':''}
			brew.publish("Publisher", data)
			rospy.logwarn("Comando enviado = "+comando)

	elif comandoSplit[1] == "call":
		if len(comandoSplit) < 3:
			rospy.logwarn("sintaxe = rosservice call /service")
		elif len(comandoSplit) == 3:
			data = {'comandoRos':'rosservice', 'funcao':'rosserviceCall', 'acao':'enviar', 'service':comandoSplit[2], 'args':''}
			brew.publish("Publisher", data)
			rospy.logwarn("Comando enviado = "+comando)
		else:
			argsSplit = comando.split('"')
			data = {'comandoRos':'rosservice', 'funcao':'rosserviceCall', 'acao':'enviar', 'service':comandoSplit[2], 'args':argsSplit[1]}
			brew.publish("Publisher", data)
			rospy.logwarn("Comando enviado = "+comando)

	elif comandoSplit[1] == "node":
		if len(comandoSplit) != 3:
			rospy.logwarn("sintaxe = rosservice node /service")
		else:
			data = {'comandoRos':'rosservice', 'funcao':'rosserviceNode', 'acao':'enviar', 'service':comandoSplit[2], 'args':''}
			brew.publish("Publisher", data)
			rospy.logwarn("Comando enviado = "+comando)

	elif comandoSplit[1] == "type":
		rospy.logwarn(comando)
		if len(comandoSplit) < 3:
			rospy.logwarn("sintaxe = rosservice node /service ( | rossrv (show | list | md5 | package | packages))")
		elif len(comandoSplit) == 3:
			data = {'comandoRos':'rosservice', 'funcao':'rosserviceType', 'acao':'enviar', 'service':comandoSplit[2], 'args':''}
			brew.publish("Publisher", data)
			rospy.logwarn("Comando enviado = "+comando)
		else:
			argsSplit = comando.split('|')
			rospy.logwarn('argssplit = '+argsSplit[1])
			data = {'comandoRos':'rosservice', 'funcao':'rosserviceType', 'acao':'enviar', 'service':comandoSplit[2], 'args':argsSplit[1]}
			brew.publish("Publisher", data)
			rospy.logwarn("Comando enviado = "+comando)

	elif comandoSplit[1] == "stop":
		stop_ = True

	else:
		rospy.logwarn("Sintaxe do comando incorreta")	
	
'''INICIO ROSSERVICE LIST'''
def rosserviceList(brew, service, args):
	proc = subprocess.Popen(["rosservice list"], stdout=subprocess.PIPE, shell=True)
	(dados, err) = proc.communicate()
	ip = ipgetter.myip()
	data = {'dados':dados, 'title':"Resultado de rosservice list do master "+ip, 'acao':'receber'}
	brew.publish("Publisher", data)
'''FIM ROSSERVICE LIST'''


'''INICIO ROSSERVICE ARGS'''
def rosserviceArgs(brew, service, args):
	proc = subprocess.Popen(["rosservice args "+service], stdout=subprocess.PIPE, shell=True)
	(dados, err) = proc.communicate()
	ip = ipgetter.myip()
	data = {'dados':dados, 'title':"Resultado de rosservice args "+service+ " do master "+ip, 'acao':'receber'}
	brew.publish("Publisher", data)
'''FIM ROSSERVICE ARGS'''


'''INICIO ROSSERVICE CALL'''
def rosserviceCall(brew, service, args):
	proc = subprocess.Popen(["rosservice call "+service+" '"+args+"'"], stdout=subprocess.PIPE, shell=True)
	(dados, err) = proc.communicate()
	ip = ipgetter.myip()
	data = {'dados':dados, 'title':"Resultado de rosservice call "+service+" "+args+ " do master "+ip, 'acao':'receber'}
	brew.publish("Publisher", data)
'''FIM ROSSERVICE CALL'''


'''INICIO ROSSERVICE NODE'''
def rosserviceNode(brew, service, args):
	proc = subprocess.Popen(["rosservice node "+service], stdout=subprocess.PIPE, shell=True)
	(dados, err) = proc.communicate()
	ip = ipgetter.myip()
	data = {'dados':dados, 'title':"Resultado de rosservice node "+service+ " do master "+ip, 'acao':'receber'}
	brew.publish("Publisher", data)
'''FIM ROSSERVICE NODE'''


'''INICIO ROSSERVICE TYPE'''
def rosserviceType(brew, service, args):
	if args=="":
		proc = subprocess.Popen(["rosservice type "+service], stdout=subprocess.PIPE, shell=True)
	else:
		rospy.logwarn("aqui = rosservice type "+service +" | "+ args)
		proc = subprocess.Popen(["rosservice type "+service +" | "+ args], stdout=subprocess.PIPE, shell=True)

	(dados, err) = proc.communicate()
	ip = ipgetter.myip()
	data = {'dados':dados, 'title':"Resultado de rosservice type "+service+ " do master "+ip, 'acao':'receber'}
	brew.publish("Publisher", data)
'''FIM ROSSERVICE TYPE'''







