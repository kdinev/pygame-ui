#!/usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
from random import randint
from UIComponentCollection import UIComponentCollection
from BaseUIComponent import *
from Button import Button
from TextLabel import TextLabel
from ConfigurationManager import ConfigurationManager

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height), 0, 32)
clock = pygame.time.Clock()
screen.fill((255, 255, 255))
pygame.display.set_caption('Configuration Manager Test')

conf = ConfigurationManager('game.pyconfig')
button = Button('Button1', parentSurface=screen, config=conf)
label = TextLabel('Label1', parentSurface=screen, config=conf)
collection = UIComponentCollection()
collection += button
collection += label

collection.Render()
pygame.display.update()

while True:
    
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		elif event.type == CLICK:
			print(event.component.id)
			label.text = 'CLICK on component with ID=' + event.component.id
		else:
			collection.Update(event)
	
	screen.fill((255, 255, 255))
	collection.Render()
	pygame.display.update()
	clock.tick(70)

