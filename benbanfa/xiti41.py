#coding=utf-8
from sys import exit
from random import randint

def death():
	quips = ["You died.You kinda suck at this",	
			 "Nice job,you died...jackss.",
			 "Such a luser.",
			 "I have a small puppy that's better at this."
			]
	print quips[randint(0,len(quips)-1)]
	exit(1)

def central_corridor():
	print "The gothons of planet #25 have invaded your"
	print "your entire "
	print "mission is to get "
	print "put it in the"
	print "escape pod"
	print "\n"
	print "You're running down "
	print "a Gothon jumps "
	print "flowing around"
	print "Aromer and about"
	action = raw_input("> ")
	
	if action == "shoot!":
		print "quick on"
		print "His clown costume is"
		print "off your aim."
		print "completely ruins "
		print "makes him "
		print "you are dead."
		return "death"
		
	elif action == "dodge!":
		print "Like a "
		print "as the Gothon's"
		print "In the middle of your artful"
		print "bang your head on the "
		print "You wake up shortly"
		print "your head and"
		return 'death'
		
	elif action == "tell a joke":
		print "Lucky for "
		print "You tell the one "
		print "Lbhe zbgure vf fb"
		print "The Gothon stops"
		print "while he's laughing "
		print "putting him down"
		return 'laser_weapon_armory'
	
	else:
		print "DOES NOT "
		return "central_corridor"

def laser_weapon_armory():
	print "You do a"
	print "for more"
	print "You stand up and "
	print "neutron bobm in "
	print "and you need"
	print "wrong 10 times"
	print "get the bomb"
	code = "%d%d%d"%(randint(1,9),randint(1,9),randint(1,9))
	guess = raw_input("[keypad]> ")
	guesses = 0
	
	while guess != code and guesses < 10:
		print "Bzzzzd!"
		
		guesses +=1
		guess =raw_input("[keypad]> ")
	if guess == code:
		print "The container"
		print "You grap"
		print "brudge where"
		
		return "the_bridge"
		
	else:
	
		print "The lock buzzes"
		print "melting sound as "
		print "You decide to "
		print "ship from"
		return "death"
	
def the_bridge():
	print "You burst"
	print "under"
	print "take control"
	print "clown"
	print "weapons oue yet"
	print "arm and doe't"
	
	action = raw_input("> ")
	
	if action == "throw the bomb":
		print "In a panic"
		print "and make a leap"
		print "Gothon shoots"
		print "As you die you "
		print "the bomb .You"
		print "it goes off"
		return "death"
		
	elif action == "slowly place the bomb":
		print "You point your"
		print "and the Gothon put "
		print "You inch backward"
		print "place the bomb"
		print "You then jump"
		print "and blast the lock"
		print "now that "
		print "get off this"
		
		return "escape_pod"
	else:
		print "DOES NOT COMPUTE"
		return "the_bridge"
	
def escape_pod():
	print "You rush through"
	print "the escape pod"
	print "hardly any Gothons"
	print "interference ."
	print "now ned to "
	print "but you "
	print "do you take?"
	
	good_pod =randint(1,5)
	guess = raw_input("[pod #]> ")
	
	if int(guess) != good_pod:
		print "You jump into pod%s and"%guess
		print "the pod escape"
		print "implodes as "
		print "into jam jelly"
		return "death"
	else:
		print "You jump into pod%s and"%guess
		print "the pod easily"
		print "the planet "
		print "back and see "
		print "bright star,"
		print "time .you won!"
		
		exit(0)
		
ROOMS ={
	'death':death,
	"central_corridor":central_corridor,
	"the_bridge":the_bridge,
	"escape_pod":escape_pod
}	

def runner(map,start):
	next = start#第一次调用值为central_corridor
	
	while True:
		room = map[next]
		print "\n----"
		next =room()
		
runner(ROOMS,'central_corridor')