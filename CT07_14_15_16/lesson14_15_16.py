print("Hello from lesson 14_15_16")

import pygame


pygame.init

screen_wid = 800
screen_hei = 800
screen = pygame.display.set_mode(screen_wid, screen_hei)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.QUIT()