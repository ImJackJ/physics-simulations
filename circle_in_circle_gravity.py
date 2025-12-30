import pygame as pg
import math
import random

pg.init()
screen = pg.display.set_mode((1200, 800))
border_radius = 350
border = pg.draw.circle(screen, (255, 255, 255), (600, 400), border_radius, 2)

g = 0.01

vel_multiplier = math.e

class Body:
    def __init__(self, color = (255, 255, 255), radius = 20, center = [600, 400], acceleration = [0,0], angle = 0, placeholder=0):
        self.color = color
        self.radius = radius
        self.center = center # x,y   
        self.acceleration = acceleration
        self.angle = angle
        self.placeholder = placeholder
        # y velocity is negative because the origin is not (0, 0)
        self.velocity = [math.cos(angle*(math.pi/180)), -math.sin(angle*(math.pi/180))] 
    
    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.center, self.radius)
    
    def move(self):
        distance = math.sqrt(((600-self.center[0])**2) + ((400-self.center[1])**2))
        if distance >= border_radius-self.radius and self.placeholder == 0:
            # bounce
            self.placeholder = 1
            coords = [(self.center[0]-600) + math.cos(self.angle)*self.radius, -((self.center[1]-400) + math.sin(self.angle)*self.radius)] # at the center
            slope = -coords[0]/coords[1]
            self.angle =  360 + 2*(math.atan(slope)*(180/math.pi)) - self.angle
            # self.velocity = [vel_multiplier*(math.cos(self.angle*(math.pi/180))*self.velocity[0]), vel_multiplier*(-math.sin(self.angle*(math.pi/180))*self.velocity[1])]
            self.velocity = [vel_multiplier*(math.cos(self.angle*(math.pi/180))), vel_multiplier*(-math.sin(self.angle*(math.pi/180)))]

        else:
            vx, vy = self.velocity[1], -self.velocity[0]
            if vx >= 0 and vy <= 0:
                self.angle = 360 + math.atan(vx/vy) * (180/math.pi)

            elif vx <= 0 and vy >= 0:
                self.angle = 180 + math.atan(vx/vy) * (180/math.pi)

            elif vx >= 0 and vy >= 0:
                self.angle = 180+math.atan(vx/vy) * (180/math.pi)

            elif vx <= 0 and vy <= 0:
                self.angle = math.atan(vx/vy) * (180/math.pi)

            self.placeholder = 0
            self.velocity[0] += self.acceleration[0]
            self.velocity[1] += self.acceleration[1]
            


        self.center[0] += self.velocity[0]
        self.center[1] += self.velocity[1]




c = Body(angle=270, center = [600, 400], acceleration=[0, g])
circles = []
for i in range(1, 5):
    circles.append(Body(angle=i, center = [600, 400], acceleration=[0, g]))


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
    screen.fill((0, 0, 0))
    pg.draw.circle(screen, (255, 255, 255), (600, 400), 350, 2)
    # c.draw(screen)
    # c.move()
    for i in circles:
        i.draw(screen)
        i.move()

    pg.time.delay(10)


    pg.display.update()