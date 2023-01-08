import pygame, pymunk, math
from random import randint

# class Vector():
#     def __init__(self, x: float, y:float):
#         self.x = x
#         self.y = y


class Ball():
    def __init__(self, x, y, size):
        self.size=size
        mass = self.size**2
        self.color = bodyColor
        angle = randint(0,359)
        coeff= 40000/mass
        self.body=pymunk.Body(mass)
        self.body.position=(x, y)
        self.body.velocity=(coeff*math.cos(angle*math.pi/180), coeff*math.sin(angle*math.pi/100))
        self.shape=pymunk.Circle(self.body, self.size)
        self.shape.elasticity = 0.97#non elastic collision, interval[0, 1]
        self.shape.density = 1
        space.add(self.body, self.shape)
    def draw(self):
        x=int(self.body.position.x)
        y=int(self.body.position.y)
        pygame.draw.circle(wn, self.color, (x,y), self.size)
    def drawVector(self):
        startx=int(self.body.position.x)
        starty=int(self.body.position.y)
        endx=(self.body.velocity.x)+startx
        endy=(self.body.velocity.y)+starty
        pygame.draw.line(wn, cterm2, (startx,starty), (endx,endy),2)
        #arrow vector could be a pygame polygon
    def drawVectorY(self):
        startx=int(self.body.position.x)
        starty=int(self.body.position.y)
        endx=startx 
        endy=(self.body.velocity.y)+starty
        pygame.draw.line(wn, cterm2, (startx,starty), (endx,endy),2)
    def drawVectorX(self):
        startx=int(self.body.position.x)
        starty=int(self.body.position.y)
        endx=(self.body.velocity.x)+startx
        endy=starty
        pygame.draw.line(wn, cterm2, (startx,starty), (endx,endy),2)



def create_segment(pos1, pos2):
    segment_body = pymunk.Body(body_type = pymunk.Body.STATIC)
    segment_shape = pymunk.Segment(segment_body, pos1, pos2, 10)
    segment_shape.elasticity=0.97 #1 for perfect bounce
    space.add(segment_body, segment_shape)

#variables
pygame.init()
wn=pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
space = pymunk.Space()

cterm1=(249,126,67)
cterm2=(107, 156, 153)
cterm3=(169,91,120)

purple=(127, 0, 255) 
bodyColor= (217, 211, 234)
FPS = 100
WHITE = (255, 255, 255, 255)
GOLD =((255,215,0))
amber = (255, 191, 0)
RED = (255, 160, 122)
BLACK = (0, 0, 0)
bg = (11, 13, 28)
balls = [Ball(randint(0,600), randint(0,600), randint(10,30)) for i in range(4)]


#Walls with 1 as elasticity value (can be changed in create_segment parameters)
pos_tl=(0,0)
pos_tr=(600, 0)
pos_bl=(0, 600)
pos_br=(600, 600)
segment1=create_segment(pos_tl, pos_tr)
segment2=create_segment(pos_tr, pos_br)
segment3=create_segment(pos_br, pos_bl)
segment4=create_segment(pos_bl, pos_tl)


#Loop for window
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False 

    wn.fill(bg)
    [ball.draw() for ball in balls]
    [ball.drawVector() for ball in balls]
    [ball.drawVectorY() for ball in balls]
    [ball.drawVectorX() for ball in balls]
    pygame.draw.line(wn, BLACK, pos_tl, pos_tr, 10)
    pygame.draw.line(wn, BLACK, pos_tr, pos_br, 10)
    pygame.draw.line(wn, BLACK, pos_br, pos_bl, 10)
    pygame.draw.line(wn, BLACK, pos_bl, pos_tl, 10)
    pygame.display.flip()
    clock.tick(FPS)
    space.step(1/FPS)
pygame.quit()


