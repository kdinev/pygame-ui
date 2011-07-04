#!/usr/bin/env python

# 	================================ Button UI Component ===============================
#
#	AUTHOR: KONSTANTIN DINEV
#	DATE: APRIL 2011
#	DESCRIPTION: User Interface button component designed for applications using 
#		graphical user interface compatible with and designed for the PYGAME library
#	CONDITIONS: Requires BaseUIComponent.py to run
#   PROJECT BY: http://www.sarconsrealm.org
#	
#	====================================================================================

from BaseUIComponent import BaseUIComponent
from TextLabel import TextLabel
from ImageBox import ImageBox
import pygame, os

DEFAULT_IMAGE_PATH = os.path.join('images', 'ButtonBackgroundNormal.png')
DEFAULT_HOVERED_IMAGE_PATH = os.path.join('images', 'ButtonBackgroundHovered.png')
DEFAULT_CLICKED_IMAGE_PATH = os.path.join('images', 'ButtonBackgroundClicked.png')

class Button(BaseUIComponent):
	
	_label = None						# Button text label
	_backgroundImage = None				# Button background image
	
	def __init__(self, id, parentSurface, upperLeftCorner = (0, 0), size = (90, 30)):
		BaseUIComponent.__init__(self, id, parentSurface, upperLeftCorner, size)
		self._InitSurface()
		self._backgroundImage = ImageBox(id + '_backGroundImage', self._controlSurface, (0, 0), size, DEFAULT_IMAGE_PATH, DEFAULT_HOVERED_IMAGE_PATH, DEFAULT_CLICKED_IMAGE_PATH)
		self._label = TextLabel(id + '_text', self._controlSurface, (5, 5), size, 'Button', 'arial', 18)
		x = (self._width - self._label._width) / 2
		y = (self._height - self._label._height) / 2
		self._label.SetPosition((x, y))
		
	def __del__(self):
		del self._label
		del self._backgroundImage
		BaseUIComponent.__del__(self)
		
	def __str__(self):
		return str(self._label)
		
	def _InitSurface(self):
		self._controlSurface = pygame.Surface((self._width, self._height), 0, self._parentSurface) 
		
	def Label(self, id, text = "", font = "arial", textSize = 0, color = (0, 0, 0), hoveredColor = (127, 127, 127)):
		if self._label != None:
			del self._label
		self._label = TextLabel(self._controlSurface, (0, 0), (self._width, self._height), text, font, textSize, color, hoveredColor)
		x = (self._width - self._label._width) / 2
		y = (self._height - self._label._height) / 2
		self._label.SetPosition((x, y))
		# self._label = TextLabel(id, self._controlSurface, (x, y), (self._width, self._height), text, font, textSize, color, hoveredColor)
	
	def BackgroundImage(self, id, imagePath = DEFAULT_IMAGE_PATH, hoveredImagePath = DEFAULT_HOVERED_IMAGE_PATH, clickedImagePath = DEFAULT_CLICKED_IMAGE_PATH):
		if self._backgroundImage != None:
			del self._backgroundImage
		self._backgroundImage = ImageBox(id, self._controlSurface, (0, 0), (self._width, self._height), imagePath, hoveredImagePath, clickedImagePath)
		
	def Hover(self, event):
		BaseUIComponent.Hover(self, event)
		self._backgroundImage.Hover(event)
		self._label.Hover(event)
		
	def MouseDown(self, event):
		BaseUIComponent.MouseDown(self, event)
		if self._clicked:
			self._backgroundImage.Activate()
			self._label.Activate()
		
	def MouseUp(self, event):
		BaseUIComponent.MouseUp(self, event)
		self._backgroundImage.Deactivate()
		self._label.Deactivate()
		
	def Unhover(self, event):
		BaseUIComponent.Unhover(self, event)
		self._backgroundImage.Unhover(event)
		self._label.Unhover(event)
		
	def Render(self):
		BaseUIComponent.Render(self)
		self._backgroundImage.Render()
		self._label.Render()
