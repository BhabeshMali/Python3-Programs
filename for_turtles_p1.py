import turtle
wx=turtle.Screen()

elon=turtle.Turtle()

distance=50
angle=90

for _ in range(50) :
	elon.forward(distance)
	elon.right(angle)
	distance=distance+10
	angle=angle+1
wx.exitonclick()
