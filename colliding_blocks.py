import pygame

big_body_mass = 100**2
delay = 20

class Body:
    def __init__(self, x, y, width, height, color, mass, velocity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.mass = mass
        self.velocity = velocity

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))


pygame.init()
screen = pygame.display.set_mode((1200, 800))

big = Body(600, 500, 100, 100, (255, 0, 0), big_body_mass, 1) 
small = Body(450, 500, 100, 100, (0, 255, 0), 1, 0) 

collisions = 0
Total_KE = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), (100, 200), (100, 600), 5)
    pygame.draw.line(screen, (255, 255, 255), (100, 600), (1000, 600), 5)


    if small.x <= 100:
        small.velocity = -1 * small.velocity
        collisions += 1
        print(collisions)
    if small.x+small.width >= big.x:
       
        temp = small.velocity
        small.velocity = ((2*big.mass*big.velocity)+(small.mass*small.velocity)-(big.mass*small.velocity))/(small.mass + big.mass)

        big.velocity = ((2*small.mass*temp)+(big.mass*big.velocity)-(small.mass*big.velocity))/(small.mass + big.mass)

        calculated_KE = 0.5 * small.mass * (small.velocity**2) + 0.5 * big.mass * (big.velocity**2)

        small.x -= 0.00000001
        collisions += 1
        print(collisions)

    small.x -= small.velocity
    big.x -= big.velocity
    pygame.time.delay(delay)
    big.draw(screen)
    small.draw(screen)



    pygame.display.update()
