import turtle


def init_screen(width=800, height=600, bgcolor='white', title='Window', tracer=0):
	screen = turtle.Screen()
	screen.setup(width=width, height=height)
	screen.title(title)
	screen.bgcolor(bgcolor)
	screen.tracer(tracer)
	return screen



def create_sprite(shape='square', color='black', penup=True, stretch_len=1, stretch_wid=1, goto=(0,0)):
	sprite = turtle.Turtle()
	sprite.shape(shape)
	sprite.color(color)
	sprite.shapesize(stretch_len=stretch_len, stretch_wid=stretch_wid)
	if penup:
		sprite.penup()
	sprite.goto(goto)


	return sprite