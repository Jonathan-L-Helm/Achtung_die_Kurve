import pygame
import math
import dataclasses

width = 1000
height = 500
background_colour = (255, 255, 255)

color = (0,0,0)
center_point = (50,50)

pygame.display.set_caption('Achtung die Kurve')
screen = pygame.display.set_mode((width, height))

screen.fill(background_colour)

pygame.display.flip()

clock = pygame.time.Clock()

#pygame.draw.circle(screen, color, center_point,  20)

pygame.display.update()

running = True

class Wurm():
    def __init__(self):
        self.breite = 8
        self.farbe = (167,16,16)
        self.x = 50
        self.y = 50
        self.y_pixel_per_frame = 0
        self.x_pixel_per_frame = 0
        self.winkel = 0
        self.speed = 2

    def move(self):
        self.x = self.x + self.x_pixel_per_frame
        self.y = self.y + self.y_pixel_per_frame

    def draw(self):
        pygame.draw.circle(screen,self.farbe,(self.x,self.y),self.breite//2)

    def turn(self, change):
        print("chang")

        self.winkel = self.winkel - change
        """
        if self.winkel > 360:
            self.winkel -= 360
        if self.winkel < 0:
            self.winkeld += 350
        """

        self.x_pixel_per_frame = math.cos(self.winkel/180)*self.speed
        self.y_pixel_per_frame = math.sin(self.winkel/180) * self.speed
        print(self.y_pixel_per_frame)



#if pygame.key.get_pressed()[pygame.K_RIGHT]:



wurm = Wurm()






change = 30

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            #print(event)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            elif event.key == pygame.K_k:
                pass
            """
            elif event.key == pygame.K_a:
                #print ("a")
                wurm.turn(change)
            elif event.key == pygame.K_d:
                wurm.turn(-change)
            """

    wurm.move()
    wurm.draw()




    pygame.display.update()
    clock.tick(60)









