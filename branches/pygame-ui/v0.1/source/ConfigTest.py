#!/usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
from UIComponentCollection import UIComponentCollection
from Button import Button
from ConfigurationManager import ConfigurationManager

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height), 0, 32)
clock = pygame.time.Clock()
screen.fill((255, 255, 255))
pygame.display.set_caption('Configuration Manager Test')

conf = ConfigurationManager('game.pyconfig')
button = Button('Button2', parentSurface=screen, config=conf)

pygame.display.update()

while True:
    
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
	
	screen.fill((255, 255, 255))
	clock.tick(70)

