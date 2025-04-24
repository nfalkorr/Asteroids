from constants import *
from circleshape import CircleShape
import pygame

class Player(CircleShape):
	def __init__(self,x,y):
		super().__init__(x,y,PLAYER_RADIUS) #pass in from CircleShape
			
		self.rotation = 0 # initialize player stationary
		self.timer = 0
		
		
	def triangle(self): #points relative to each other, draw in next method
	    forward = pygame.Vector2(0, 1).rotate(self.rotation) # calculating forwardmost point of triangle
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
		self.timer -= dt
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			self.rotate(-dt) #rotate left based on A - keypress
		if keys[pygame.K_d]:
			self.rotate(dt) #rotate right based on D - keypress
		if keys[pygame.K_w]:
			self.move(dt) #move up based on W - keypress
		if keys[pygame.K_s]:
			self.move(-dt) #move down based on S - keypress
		if keys[pygame.K_SPACE]:
			if self.timer > 0:
				return False
			else:
				self.shoot()

	def move(self,dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation) #update 
		self.position += forward * PLAYER_SPEED * dt # move forward based on previous position modified by speed and clock update
	def shoot(self):
		shot = Shot(self.position.x,self.position.y,SHOT_RADIUS)
		
		shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * SHOOT_SPEED
		#group_shots.add(shot)
		self.timer = SHOOT_COOLDOWN

class Shot(CircleShape):
	def __init__(self,x,y,radius):
		super().__init__(x,y,radius)
		self.radius = radius
		self.velocity = pygame.Vector2(0,0)

	def draw(self,screen):
		pygame.draw.circle(screen,"white",self.position,self.radius)

	def update(self,dt):
		self.position += self.velocity * dt
