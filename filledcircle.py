import pygame
pygame.init()

screen = pygame.display.set_mode((400,400))
run = True
class Circle():
    def __init__(self,color,pos,radius,width):
        self.color = color
        self.pos = pos
        self.radius = radius
        self.width = width
        self.surface = screen
    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius, self.width)

Blue_circle = Circle("Blue",(300,300), 25, 0)

while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    pygame.draw.rect(screen,"Red", pygame.Rect(30,30,60,60))
    pygame.draw.rect(screen,"Purple", pygame.Rect(150,150,80,80))
    pygame.draw.circle(screen,"Blue", (100,100), 50,0,)
    Blue_circle.draw()
    pygame.display.update()
   
pygame.quit()
