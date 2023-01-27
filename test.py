import pygame

x , y = 0 , 0
delta = 10

run = True

keys = pygame.key.get_pressed()

if keys[pygame.K_LEFT]:
    x -= delta

if keys[pygame.K_RIGHT]:
    x += delta

if keys[pygame.K_DOWN]:
    y -= delta

if keys[pygame.K_UP]:
    y += delta
