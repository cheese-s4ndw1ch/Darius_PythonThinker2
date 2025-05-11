print("Hello from lesson 14_15_16")

import pygame


pygame.init

screen_wid = 800
screen_hei = 600

white = (255,255,255)

paddle_width = 30
paddle_height = 100
paddle1_x =
paddle_y = 

running = True

screen = pygame.display.set_mode((screen_wid,screen_hei))

pygame.display.set_caption("Pong Game")


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
pygame.draw.rect(screen, white, (paddle1_x, paddle_y, paddle_width, paddle_height))

pygame.QUIT()