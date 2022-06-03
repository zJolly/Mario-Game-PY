#!/usr/bin/python

import pygame
import random
import time

pygame.init()
finestra = pygame.display.set_mode((900,500))
pygame.display.set_caption("PyGame")
immagine = pygame.image.load("sfondomario.png")
immagine = pygame.transform.scale(immagine, (900, 500))
finestra.blit(immagine, (0, 0))
pygame.display.update()
ciclo = pygame.time.Clock()
FPS = 144
y = 417
x = 0
y1 = 0
dx = 0
sx = 0
up = 0
dw = 0
anima = 0
jump = 0

personaggio = pygame.image.load("mario/mario.png")
personaggio1 = pygame.image.load("mario/mario1.png")
personaggio2 = pygame.image.load("mario/mario2.png")
personaggio3 = pygame.image.load("mario/mario3.png")
personaggio4 = pygame.image.load("mario/mario4.png")
personaggio5 = pygame.image.load("mario/mario5.png")
personaggioJump = pygame.image.load("mario/mario7.png")
personaggio8 = pygame.image.load("mario/mario8.png")
marioinizio = pygame.image.load("mario/intro.png")
personaggioDown = pygame.image.load("mario/mario10.png")
personaggio = pygame.transform.scale(personaggio, (26, 36))
personaggio1 = pygame.transform.scale(personaggio1, (30, 36))
finestra.blit(personaggio, (x, y))

#def spostamento(x, y, x1, y1):

while True:
    ciclo.tick(FPS)
    for evento in pygame.event.get():
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        pygame.display.update()
        if evento.type == pygame.QUIT:
            quit()
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_ESCAPE:
            quit()
        elif evento.key == pygame.K_LEFT:
            if x > 0:
                if anima >= 0 and anima <= 5:
                    x=x-1
                    finestra.blit(immagine, (0, 0))
                    finestra.blit(pygame.transform.flip(personaggio, True, False), (x, y))
                    anima = anima + 1
                if anima > 5 and anima <= 10:
                    x=x-1
                    finestra.blit(immagine, (0, 0))
                    finestra.blit(pygame.transform.flip(personaggio1, True, False), (x, y))
                    anima = anima + 1
                if anima > 10 and anima <= 15:
                    x=x-1
                    finestra.blit(immagine, (0, 0))
                    finestra.blit(pygame.transform.flip(personaggio2, True, False), (x, y))
                    anima = anima + 1
                if anima > 15 and anima <= 20:
                    x=x-1
                    finestra.blit(immagine, (0, 0))
                    finestra.blit(pygame.transform.flip(personaggio3, True, False), (x, y))
                    anima = anima + 1
                if anima > 20 and anima <= 25:
                    x=x-1
                    finestra.blit(immagine, (0, 0))
                    finestra.blit(pygame.transform.flip(personaggio4, True, False), (x, y))
                    anima = anima + 1
                if anima > 25 and anima <= 30:
                    x=x-1
                    finestra.blit(immagine, (0, 0))
                    finestra.blit(pygame.transform.flip(personaggio5, True, False), (x, y))
                    anima = 0
            sx = 1
        elif evento.key == pygame.K_RIGHT:
            if x < 872:
                if anima >= 0 and anima <= 5:
                    x=x+1
                    finestra.blit(immagine, (0, 0))
                    finestra.blit(personaggio, (x, y))
                    anima = anima + 1
                if anima > 5 and anima <= 10:
                    x=x+1
                    finestra.blit(immagine, (0, 0))
                    finestra.blit(personaggio1, (x, y))
                    anima = anima + 1
                if anima > 10 and anima <= 15:
                    x=x+1
                    finestra.blit(immagine, (0, 0))
                    finestra.blit(personaggio2, (x, y))
                    anima = anima + 1
                if anima > 15 and anima <= 20:
                    x=x+1
                    finestra.blit(immagine, (0, 0))
                    finestra.blit(personaggio3, (x, y))
                    anima = anima + 1
                if anima > 20 and anima <= 25:
                    x=x+1
                    finestra.blit(immagine, (0, 0))
                    finestra.blit(personaggio4, (x, y))
                    anima = anima + 1
                if anima > 25 and anima <= 30:
                    x=x+1
                    finestra.blit(immagine, (0, 0))
                    finestra.blit(personaggio5, (x, y))
                    anima = 0
            dx = 1

        elif evento.key == pygame.K_DOWN:
            if y < 417:
                y=y+1
            if y == 417:
                y1 = y + 10
                finestra.blit(immagine, (0, 0))
                finestra.blit(personaggioDown, (x, y1 ))
            dw = 1

        elif evento.key == pygame.K_UP:
            if y > 0:
                y=y-1
                finestra.blit(immagine, (0, 0))
                finestra.blit(personaggioJump, (x, y ))
            up = 1




        elif evento.type == pygame.MOUSEBUTTONDOWN:
            premuto = pygame.mouse.get_pressed()
            if premuto[0] == 1:
                imma = pygame.image.load("foro.png")
                x = pygame.mouse.get_pos(0)
                y = pygame.mouse.get_pos(1)

                finestra.blit(imma, (x, y))
                pygame.display.update()
    


     #spostamento(x, y, x1, y1)
    pygame.display.update()
