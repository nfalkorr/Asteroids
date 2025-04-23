from constants import *
from player import Player
import pygame
pygame.init

def main():

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #initialize screen object

	clock = pygame.time.Clock() #defining object Clock to initialize updates
	dt = 0
	x = SCREEN_WIDTH/2
	y = SCREEN_HEIGHT/2	
	player = Player(x,y)


	while(True): #game logic loop, updates infinitely until game is closed out by user
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black",rect=None,special_flags=0) #initializes screen. technically i could just pass in color
		player.draw(screen) #make sure to draw player before display.flip() updates the screen
		pygame.display.flip() # displays screen
		
		
		dt = clock.tick(60)/1000 # delta time since last time tick was called, sets to 60fps
		#print(f"dt is {dt}") #debug for performance
		
	
if __name__ == "__main__": # run main
	main()
