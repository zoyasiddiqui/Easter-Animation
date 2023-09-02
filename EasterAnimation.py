import pygame, random
pygame.init()
SIZE = (500, 500)
screen = pygame.display.set_mode(SIZE)
GREEN = (177, 252, 230)
PINK = (255, 194, 229)
YELLOW = (255, 231, 196)
BLUE = (189, 206, 255)
BLACK = (0,0,0)

choices = [GREEN, PINK, YELLOW, BLUE]
count = 0

while count in range(0,500):
    count += 5
    colorChoice = random.choice(choices)
    pygame.draw.rect(screen, colorChoice, (0, count, 500, 5))
    pygame.display.flip()
    pygame.time.wait(10)
    pygame.draw.rect(screen, colorChoice, (count, 0, 5, 500))
    pygame.display.flip()
    pygame.time.wait(10)  
    pygame.font.init()
    myFont = pygame.font.SysFont('Times New Roman',30)
    textSurface = myFont.render("Happy Easter!", False, (0,0,0))
    screen.blit(textSurface,(150,200))
    pygame.display.flip()
    pygame.time.wait(10)
    
    

pygame.quit()