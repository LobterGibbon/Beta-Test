import pygame
import math
import time
import random
pygame.init()
clock = pygame.time.Clock()
scaleUp = 50 #recommended 120 for full screen
screen_width = 16*scaleUp #1920
screen_height = 9*scaleUp #1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Name Pending")
#image = pygame.image.load("Space.png")
#size = pygame.transform.scale(image, (screen_width, screen_height))
#screen.blit(size, (0,0))

screenColours = [(250,235,215),(240,248,255)]
endScreenColour = (0,0,0)
screen.fill(screenColours[random.randint(0,1)])

#grid = 1000x1000
#we can also have this wrap around
#make a class of objects which exist at certain coordinates on that grid
#grid coordinates = normal coordinates in relation to player

#essentially, we're going to replicate the entirety of assteroids 
#except, we're also going to have a camera entity which follows the player 
#and we're going to have every entity blit in relation to that camera

entityArray = []

class Entity:
  def __init__(self,startx,starty):
    self.sprite = pygame.image.load("Blorgon.png").convert_alpha()
    self.pos = (startx , starty)
    self.angle = math.radians(0)
    #there are two methods in representing angle. 
    #1) starting at y/north and moving clockwise 
    #2) starting at x/east and moving counter-clockwise
    # in Assteroids I went with method 2, here I will use method 1
    self.speed = 0

  def positionSort(self):
    return self.pos[1]
    
    
  def collision(self):
    #each entity should have a rectangle for collisions

    #macro collisions detection

    #micro collision detection
    pass

  def manouver(self,angle,speed):
    self.angle = math.radians(angle)
    #print(angle)
    #print(self.angle)
    self.speed = speed
    #print(speed)
    #print(self.speed)
    #print("pluh")
  
  def update(self):
    self.pos = ((self.pos[0] + (self.speed*math.sin(self.angle))),
    (self.pos[1] + (self.speed*math.cos(self.angle))))
    #read calculate_new_xy from my 'Assteroids' game
    self.sprite_dimAtCent = self.sprite.get_rect(center= self.pos)
    #sprite_dimAtCent is the dimensions for a rectangle 
    #equal to the sprite size with the centre at self.pos
    #dimAtCent == Dimensions At Centre
    screen.blit(self.sprite, self.sprite_dimAtCent)
    #https://www.youtube.com/watch?v=WnIycS9Gf_c
    newAngle = math.degrees(self.angle)
    pygame.transform.rotate(pygame.image.load("Blorgon.png").convert_alpha(), newAngle)


playerAngle = 0
playerSpeed = 0
turnRight = False
turnLeft = False
Faster = False
Slower = False

PlayerObject = Entity(screen_width/2 , screen_height/2)
entityArray.append(PlayerObject)
entityArray.append(Entity(50,50))
entityArray.append(Entity(400,400))

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      screen.fill(endScreenColour)
      running=False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        Faster = True
      elif event.key == pygame.K_DOWN:
        Slower = True
      elif event.key == pygame.K_RIGHT:
        turnRight = True
      elif event.key == pygame.K_LEFT:
        turnLeft = True
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_UP:
        Faster = False
      elif event.key == pygame.K_DOWN:
        Slower = False
      elif event.key == pygame.K_RIGHT:
        turnRight = False
      elif event.key == pygame.K_LEFT:
        turnLeft = False

  if Faster:
    playerSpeed += 0.5
  if Slower:
    playerSpeed -= 0.5
  if turnLeft:
    playerAngle += 5
  if turnRight:
    playerAngle -= 5
    
  PlayerObject.manouver(playerAngle,playerSpeed) 

  #Updates VVVV
  screen.fill(screenColours[random.randint(0,1)])
  for i in sorted(entityArray,key=lambda x: x.pos[1]):
     i.update()

      


  pygame.display.flip()
  clock.tick(20)
# Game loop end------------

