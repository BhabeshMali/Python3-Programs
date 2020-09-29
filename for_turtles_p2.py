import turtle
wx=turtle.Screen()
wx.bgcolor("yellow")

elon=turtle.Turtle()
elon.color("green")
elon.shape("turtle")

distance=5
elon.up()

for _ in range(50) :
	elon.stamp()
	elon.forward(distance)
	elon.right(24)
	distance=distance+2
wx.exitonclick()
