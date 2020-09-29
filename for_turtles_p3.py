from turtle import Turtle,Screen

wn=Screen()

elon=Turtle()
elon.shape("turtle")
elon.penup()

for _ in range(10) :
	elon.forward(50)
	elon.stamp()
	elon.forward(-50)
	elon.right(36)
wn.exitonclick()
