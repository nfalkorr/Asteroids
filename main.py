import sys
from constants import *
from player import Player
import pygame
from asteroidfield import *
import asteroid
pygame.init()

def main():

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #initialize screen object

	clock = pygame.time.Clock() #defining object Clock to initialize updates
	dt = 0

	#create groups before defining player position
	group_updatable = pygame.sprite.Group()
	group_drawable = pygame.sprite.Group()	
	Player.containers = (group_updatable, group_drawable)


	AsteroidField.containers = (group_updatable)
	asteroid_field = AsteroidField()
	
	#asteroids
	group_asteroids = pygame.sprite.Group()
	Asteroid.containers = (group_asteroids,group_updatable,group_drawable)
	#create other starting modifications here
	
	#define player starting position
	x = SCREEN_WIDTH/2
	y = SCREEN_HEIGHT/2	
	player = Player(x,y)
	#do not make further starting modifications to player past this point

	while(True): #game logic loop, updates infinitely until game is closed out by user
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black",rect=None,special_flags=0) #initializes screen. technically i could just pass in color			
		group_updatable.update(dt)
		for asteroid in group_asteroids:
			if asteroid.collision(player):
				print("Game Over!")
				sys.exit("You Lost")
		for object in group_drawable:
			object.draw(screen) #make sure to draw player before display.flip() updates the screen
		
		pygame.display.flip() # displays screen
		
		
		dt = clock.tick(60)/1000 # delta time since last time tick was called, sets to 60fps
		#print(f"dt is {dt}") #debug for performance
		
	
if __name__ == "__main__": # run main
	main()
