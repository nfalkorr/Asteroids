from constants import PLAYER_RADIUS
from constants import ROTATION_SPEED
from circleshape import CircleShape
import pygame

class Player(CircleShape):
	def __init__(self,x,y):
		super().__init__(x,y,PLAYER_RADIUS) #pass in from CircleShape
	
		self.rotation = 0 # initialize player stationary

	def triangle(self): #points relative to each other, draw in next method
	    forward = pygame.Vector2(0, 1).rotate(self.rotation) # calculating highest/forwardmost point of triangle
	    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5 #calculate rightmost side of triangle
	    a = self.position + forward * self.radius # point a is the center of the triangle (self.position) + the forwardmost point * the defined radius of the player passed in from CircleShape
	    b = self.position - forward * self.radius - right #leftmost point calculation
	    c = self.position - forward * self.radius + right #rightmost point calculation
	    return [a, b, c] #return updated position

	def draw(self,screen):
		pygame.draw.polygon(screen, "white", self.triangle(),2) #show player on screen
		#print("Player drawn at:",self.position)		#debug statement
	
	def rotate(self, dt):
		self.rotation = self.rotation + (ROTATION_SPEED * dt) # calculate rotation based on current + speed constant * delta value

	def update(self, dt):
	    keys = pygame.key.get_pressed()

	    if keys[pygame.K_a]:
	        self.rotate(-dt) #rotate left based on A - key press
	    if keys[pygame.K_d]:
	        self.rotate(dt) #rotate right based on D - key press
