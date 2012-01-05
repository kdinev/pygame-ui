#!/usr/bin/env python

import pygame, os
from pygame.locals import *
from sys import exit
from UIComponentCollection import UIComponentCollection
from Button import Button
from ConfigurationManager import ConfigurationManager

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height), 0, 32)
opening_background = pygame.image.load(os.path.join('images', 'Pygame-UI-Background.jpg')).convert()
clock = pygame.time.Clock()
config = ConfigurationManager('showcase.pyconfig')
collection = UIComponentCollection()
button = Button('Button1', parentSurface = screen, config = config, imagePath = os.path.join('images', 'button-normal-transparent.png'), hoveredImagePath = os.path.join('images', 'button-hover-transparent.png'), clickedImagePath = os.path.join('images', 'button-clicked-transparent.png'))
button.text = 'Testing'
collection += button

def OpeningScreen(screen, collection):
	screen.blit(opening_background, (0, 0))
	collection.Render()
	pygame.display.update()
	
OpeningScreen(screen, collection)

while 1:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
		else:
			collection.Update(event)
	
	OpeningScreen(screen, collection)
	clock.tick(70)
