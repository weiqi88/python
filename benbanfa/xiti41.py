#coding=utf-8
from sys import exit
form random import randint

def death():
	quips = ["You died.You kinda suck at this",	
			 "Nice job,you died...jackss.",
			 "Such a luser.",
			 "I have a small puppy that's better at this."
			]
	print quips[randint(0,len(quips)-1]
	exit(1)