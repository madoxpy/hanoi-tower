from pygame import *
import gameclass

def main():
	res=[1040,300]
	init()
	window=display.set_mode(res)
	clock=time.Clock()
	
	end=False
	game=gameclass.Game()
	
	while not end:
		for z in event.get():
			if z.type==QUIT:
				end=True
			if z.type==KEYDOWN:
				if z.key==K_1:
					game.event(1)
			if z.type==KEYDOWN:
				if z.key==K_2:
					game.event(2)
			if z.type==KEYDOWN:
				if z.key==K_3:
					game.event(3)

				
		game.draw(window)
		clock.tick(20)
		display.flip()
		

		

if __name__=="__main__":
	main()
