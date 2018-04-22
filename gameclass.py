from pygame import *

black=(0,0,0)
brown=(102,51,0)
red=(255,5,5)
white=(255,255,255)
#Font=font.SysFont("arial",32)

class Game(object):
	def __init__(self):
		self.tab = [ [5,4,3,2,1], [], [] ]
		self.start = 0
		self.endgame = False
		self.counter = 0
	
	def event(self,num):
		if not self.endgame:
			if self.start==0:
				if len(self.tab[num-1])>0:
					self.start=num
			elif self.start!=0:

				if len(self.tab[num-1])>0:
					brick=self.tab[self.start-1][-1]
					if self.tab[num-1][-1]>brick:
						self.tab[self.start-1].remove(brick)
						self.tab[num-1].append(brick)
						if self.start!=num:
							self.counter=self.counter+1
				elif len(self.tab[num-1])==0:
					brick=self.tab[self.start-1][-1]
					self.tab[self.start-1].remove(brick)
					self.tab[num-1].append(brick)
					if self.start!=num:
						self.counter=self.counter+1
				

				self.start=0
			
			if self.tab[2]==[5,4,3,2,1]:
				self.endgame=True

			
		
	def draw(self,window):
		window.fill(black)
		draw.rect(window,brown,Rect(20,260,1000,50),3)
		draw.rect(window,brown,Rect(190,80,20,180),3)
		draw.rect(window,brown,Rect(510,80,20,180),3)
		draw.rect(window,brown,Rect(830,80,20,180),3)
		
		for t in self.tab:
			for i in range(len(t)):
				draw.rect(window,black,Rect(self.tab.index(t)*320+200-30*t[i],30*(5-i)+80,t[i]*60,30),0)
				if self.start-1==self.tab.index(t) and i == len(t)-1:
					draw.rect(window,red,Rect(self.tab.index(t)*320+200-30*t[i],30*(5-i)+80,t[i]*60,30),0)
				draw.rect(window,red,Rect(self.tab.index(t)*320+200-30*t[i],30*(5-i)+80,t[i]*60,30),1)
		Font=font.SysFont("arial",32)
		text = Font.render(str(self.counter),True,white)
		window.blit(text,(950,260))		
		if self.endgame:
			Font=font.SysFont("arial",32)
			text = Font.render("YOU WIN",True,white)
			window.blit(text,(450,100))