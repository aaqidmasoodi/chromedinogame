import turtle
import helpers as hlp
import time


# Window 
scr = hlp.init_screen(title='Dino Game - CodeWithAaqid')


# floor
floor = hlp.create_sprite(stretch_len=40, stretch_wid=2, goto=(0,-280))



# player
player = hlp.create_sprite(stretch_wid=5, goto=(-300,-210))
player.dy = -1


GRAVITY = 1

def jump():
	if player.ycor() == -210:
		player.dy = 15



scr.listen()
scr.onkeypress(jump, 'space')




while True:


	player.sety(player.ycor() + player.dy)

	player.dy -= GRAVITY


	if player.ycor() < -210:
		player.sety(-210)
		player.dy = 0


	scr.update()
	time.sleep(1/60)






