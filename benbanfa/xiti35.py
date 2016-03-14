#coding=utf-8
from sys import exit

def gold_room(): #定义函数gold_room
	print "This room is full of gold.How much do you take?"
	
	next = raw_input("> ")#接受输入
	if "0" in next or "1" in next:#如果满足条件就执行下面的语句
		how_much = int(next)
	else:#否则执行下面的
	    dead("Man,learn to type a number")#调用自定义函数，退出程序
	
	if how_much < 50:#如果小于50
		print "Nice , you're not greedy,you win!"
		exit(0)#无错误退出
	else:
		dead("You greedy bastard!")
	
def bear_room():#定义函数bear_room
	print "There is a bear here"
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door"
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True:#循环为真，带便条件永远执行
		next = raw_input('>')
		
		if next=="take honey":
		    dead ("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door .You can go through it now"
			bear_moved = True
		elif next == "taunt bear " and bear_moved:
			dead("The bear gets pissed off and chews your len off.")
		elif next == "open door" and bear_moved:
			gold_room()#调用gold_room()函数
		else :
			print "I got no idea what that means."

def cthulhu_room():
	print "Here you see the great evil cthulhu."
	print "He,it,whatever stares at you and you go insane"
	print "Do you flee for your life or eat your head?"
	
	next = raw_input("> ")
	
	if "flee" in next:
		start()#调用start函数
	elif "head" in next:
		dead("Well taht was tasty!")
	else:
		cthulhu_room()

def dead(why):
	print why, "Good job"
	exit(0)
def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "With one do you take ?"
	
	next = raw_input(">")
	
	if next =="left":
		bear_room()
	elif next =="right":
		cthulhu_room()
	else:
		dead("You stumble around the room unntil you starve.")

start()