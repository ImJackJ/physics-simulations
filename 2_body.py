import pygame
import math

small_mass = 6*10**24
big_mass = 6*10**30

initial_velocity_small = [-7, 5]
initial_velocity_big = [0, 0]
distance_multiplier = 1500000000
delay = 25


G = 6.67408e-11

class Body:
    def __init__(self, pos, radius, color, mass, velocity):
        self.pos = pos
        self.radius = radius
        self.color = color
        self.mass = mass
        self.velocity = velocity
        self.acceleration = [0, 0]

    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)


small = Body([800, 600], 10, (255, 255, 255), small_mass, initial_velocity_small)
big = Body([600, 400], 20, (255, 0, 0), big_mass, initial_velocity_big)

pygame.init()
screen = pygame.display.set_mode((1200, 800))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill((0, 0, 0))


    # Calculate the distance between the two bodies, multiplied by a really big number
    distance = math.sqrt((small.pos[0] - big.pos[0])**2 + (small.pos[1] - big.pos[1])**2) * distance_multiplier

    # Calculate the force between the two bodies
    force = (G * small.mass * big.mass) / distance**2

    # Calculate the acceleration of the smaller body
    small.acceleration[0] = force * (big.pos[0] - small.pos[0]) / small.mass
    small.acceleration[1] = force * (big.pos[1] - small.pos[1]) / small.mass

    print(small.acceleration, distance)
    small.velocity[0] += small.acceleration[0]
    small.velocity[1] += small.acceleration[1]

    small.pos[0] += small.velocity[0]
    small.pos[1] += small.velocity[1]

    big.acceleration[0] = force * (small.pos[0] - big.pos[0]) / big.mass
    big.acceleration[1] = force * (small.pos[1] - big.pos[1]) / big.mass
    big.velocity[0] += big.acceleration[0]
    big.velocity[1] += big.acceleration[1]
    big.pos[0] += big.velocity[0]
    big.pos[1] += big.velocity[1]

    small.draw(screen)
    big.draw(screen)
    pygame.time.delay(delay)

    pygame.display.update()