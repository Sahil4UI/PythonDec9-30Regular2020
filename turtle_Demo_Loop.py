Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.Screen()
<turtle._Screen object at 0x00000235157046D0>
>>> turtle.pen()
{'shown': True, 'pendown': True, 'pencolor': 'black', 'fillcolor': 'black', 'pensize': 1, 'speed': 3, 'resizemode': 'noresize', 'stretchfactor': (1.0, 1.0), 'shearfactor': 0.0, 'outline': 1, 'tilt': 0.0}
>>> turtle.shape('turtle')
>>> turtle.forward(200)
>>> turtle.left(90)
>>> turtle.forward(200)
>>> turtle.left(90)
>>> turtle.forward(200)
>>> turtle.left(90)
>>> turtle.forward(200)
>>> turtle.left(90)
>>> turtle.clear()
>>> 
>>> for i in range(4):
	turtle.forward(200)
	turtle.left(90)

>>> 