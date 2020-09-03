""" This is a basic implementation of OOP, specifically a game using
	the Turtle graphics Library
"""

# import modules
import turtle
import random
import math
import os

# set up screen
wn = turtle.Screen()
# notice that bgcolor is a method because were passing 'red' through parantheses versus
# saying wn.bgolor = red OR passing it with our instantiation of the object:
# ex: wn=turtle.Screem("red"). 
wn.bgcolor("red")
wn.title("Python Turtle Graphics Game")
wn.bgpic("bg.gif")
wn.register_shape("mush.gif")

class Border(turtle.Turtle):

		def __init__(self):
			turtle.Turtle.__init__(self)
			self.penup()
			self.hideturtle()
			# animation speed (do not animate, draw right away)
			self.speed(0)
			self.color("white")
			self.pensize(5)

		def drawBorder(self):
			self.penup()
			self.goto(-300, -300)
			self.pendown()
			self.goto(-300, 300)
			self.goto(300, 300)
			self.goto(300, -300)
			self.goto(-300, -300)
# Create Player Class: called Class Definition
# The statement below says that the Player class is a child or subclass of the
# turtle class. This means that it inherits all the attributes and methods of the 
# turtle class
class Player(turtle.Turtle):

	# define constructor
	# self refers to this particular object
	def __init__(self):
		# must define parent class
		turtle.Turtle.__init__(self)
		self.penup()
		self.shape("triangle")
		self.color("white")
		self.speed = 1

	def move(self):
		self.forward(self.speed)

		if self.xcor() > 285 or self.xcor() < -290:
			self.left(60)

		if self.ycor() > 285 or self.ycor() < -290:
			self.left(60)

	def turnleft(self):
		self.left(30)

	def turnright(self):
		self.right(30)
	
	def increasespeed(self):
		self.speed += 1

	def decreasespeed(self):
		self.speed -= 1

class Goal(turtle.Turtle):

	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.speed(0)
		self.color("green")
		self.shape("mush.gif")
		self.speed = 3
		self.goto(random.randint(-250,250), random.randint(-250,250))
		self.score = 0

	def move(self):
		self.forward(self.speed)

		if self.xcor() > 285 or self.xcor() < -290:
			self.left(60)

		if self.ycor() > 285 or self.ycor() < -290:
			self.left(60)

	def jump(self):
		self.goto(random.randint(-250,250), random.randint(-250,250))
		self.setheading(random.randint(0,360))



class isCollision():

	def __init__(self):
		pass

	def Collision(self, player, goal):
		a = player.xcor() - goal.xcor()
		b = player.ycor() - goal.ycor()

		distance = math.sqrt((a**2 + b**2))

		if distance < 20:
			return True
		else:
			return False

class Score(turtle.Turtle):
	def __init__(self, upTick):
		turtle.Turtle.__init__(self)
		self.upTick = upTick
		self.score = 0
		self.penup()
		self.hideturtle()
		self.speed(0)
		self.color("white")
		self.goto(-290, 310)
		self.write("Score: {}".format(self.score), False, align = 'left', font = ("Arial", 14, "normal"))

	def increaseScore(self):
		self.score += self.upTick
		self.clear()
		self.write("Score: {}".format(self.score), False, align = 'left', font = ("Arial", 14, "normal"))

	def playSound(self, filename):
		os.system("afplay {}&".format(filename))


player = Player()
border = Border()
checkCollision = isCollision()
updateScore = Score(10)

# create multiple goals
goals = []

for count in range(7):
	goals.append(Goal())


border.drawBorder()

# Create keyboard binds for movement
turtle.listen()
turtle.onkey(player.turnleft,"Left")
turtle.onkey(player.turnright,"Right")
turtle.onkey(player.increasespeed,"Up")
turtle.onkey(player.decreasespeed,"Down")

# stops updating the screen (0) 
wn.tracer(0)

# main loop
while True:
	wn.update() 
	player.move()

	for goal in goals:
		
		goal.move()

		if checkCollision.Collision(player, goal):
			goal.jump()
			updateScore.increaseScore()
			updateScore.playSound("score.mp3")