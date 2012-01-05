#!/usr/bin/env python
import pygame, os
from pygame.locals import *
from sys import exit
from random import randint
from UIComponentCollection import UIComponentCollection
from BaseUIComponent import *
from Button import Button
from TextLabel import TextLabel
from ImageBox import ImageBox
from MessageBox import MessageBox
from ConfigurationManager import ConfigurationManager

pygame.init()

width = 1024
height = 768

screen = pygame.display.set_mode((width, height), 0, 32)
clock = pygame.time.Clock()
screen.fill((0, 0, 0))
pygame.display.set_caption('Configuration Manager Test')

conf = ConfigurationManager('game.pyconfig')
button = Button('Button1', parentSurface=screen, config=conf)
button.text = 'Press Me'
label = TextLabel('Label1', parentSurface=screen, config=conf)
dialog = MessageBox('Dialog1', parentSurface=screen, config=conf)
collection = UIComponentCollection()
collection += button
collection += label
collection += dialog

collection.Render()
pygame.display.update()

while True:
    
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
		elif event.type == CLICK:
			label.text = 'CLICK on component with ID=' + event.component.id
		else:
			collection.Update(event)
	
	screen.fill((0, 0, 0))
	collection.Render()
	pygame.display.update()
	clock.tick(70)

