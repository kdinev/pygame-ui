#!/usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
from UIComponentCollection import UIComponentCollection
from TextLabel import TextLabel
from Button import Button
from MessageBox import MessageBox
import random, sys

pygame.init()

width = 800
height = 600

def CreateMessageBox():
	collection.Append(MessageBox('MessageBox1', screen, (random.randint(0, 349), random.randint(0, 349)), (350, 150)))

screen = pygame.display.set_mode((width, height), 0, 32)
clock = pygame.time.Clock()
screen.fill((255, 255, 255))
pygame.display.set_caption('UI Component Test')
collection = UIComponentCollection()
label = TextLabel('TextLabel1', screen, (50, 50), (0, 0), 'Hello world!', 'arial', 48)
label.SetHoveredColor((5, 230, 65))

collection.Append(label)

button = Button('Button1', screen, (250, 450))
button.SetClickCallback(CreateMessageBox)
collection.Append(button)


collection.Render()
pygame.display.update()

while True:
    
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		cur_pos = pygame.mouse.get_pos()
		collection.Update(event)
	
	screen.fill((255, 255, 255))
	collection.Render()
	pygame.display.update()
	clock.tick(70)

