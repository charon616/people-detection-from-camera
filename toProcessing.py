#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import socket
from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder

IP = 'localhost'
PORT = 6700
# UDPのクライアントを作る
client = udp_client.UDPClient(IP, PORT)

def startPort():
	print('osc starting..')

def deleteObject(pID):
	# /addに送信するメッセージを作って送信する
	msg = OscMessageBuilder(address='/delete')
	msg.add_arg('object Added!')
	m = msg.build()
	client.send(m)

def addObject():
	# /addに送信するメッセージを作って送信する
	msg = OscMessageBuilder(address='/add')
	msg.add_arg('object Added!')
	m = msg.build()
	client.send(m)

def sendPosition(pID, posx, posy):
	# /personに送信するメッセージを作って送信する
	p = OscMessageBuilder(address='/person')
	p.add_arg(int(pID))
	p.add_arg(int(posx))
	p.add_arg(int(posy))
	m = p.build()
	client.send(m)

if __name__ == '__main__':
	# VideoCapture オブジェクトを取得します
	capture = cv2.VideoCapture(0)
	while(True):
		ret, frame = capture.read()
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	capture.release()
	cv2.destroyAllWindows()

'''
python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input videos/example_01.mp4 --output output/output_01.avi
python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --output output/webcam_output.avi
'''