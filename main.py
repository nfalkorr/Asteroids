from constants import *
import pygame
pygame.init

def main():

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #initialize screen object

	clock = pygame.time.Clock() #defining object Clock to initialize updates
	dt = 0

	while(True): #game logic loop, updates infinitely until game is closed out by user
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black",rect=None,special_flags=0) #initializes screen
		pygame.display.flip() # displays screen
		clock.tick(60) # pauses game loop until 1/60th of a second has passed to save resources
		# print(f"Tick is {clock.tick(60)}") #debug for performance
		dt = clock.tick(60)/1000 # delta time since last time tick was called
		print(f"dt is {dt}") #debug for performance
if __name__ == "__main__": # run main
	main()
