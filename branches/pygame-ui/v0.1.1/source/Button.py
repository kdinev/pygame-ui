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
	
	def __init__(self, id, parentSurface, config = None):
		BaseUIComponent.__init__(self, id, parentSurface, config)
		self._InitSurface()
		bg_styling = config.InitStylingManagerByType(self.styling.xml_node, "ImageBox")
		self.BackgroundImage(id + '_backGroundImage', DEFAULT_IMAGE_PATH, DEFAULT_HOVERED_IMAGE_PATH, DEFAULT_CLICKED_IMAGE_PATH, bg_styling)
		lbl_styling = config.InitStylingManagerByType(self.styling.xml_node, "TextLabel")
		self.Label(id + '_text', config = lbl_styling)
		x = (self.width - self._label.width) / 2
		y = (self.height - self._label.height) / 2
		self._label.position = (x, y)
		
	def __del__(self):
		BaseUIComponent.__del__(self)
		del self._label
		del self._backgroundImage
		
	def __str__(self):
		return str(self._label)
		
	@property
	def text(self):
		return self._label.text
		
	@text.setter
	def text(self, value):
		self._label.text = value
		x = (self.width - self._label.width) / 2
		y = (self.height - self._label.height) / 2
		self._label.position = (x, y)
		
	def _InitSurface(self):
		self._controlSurface = pygame.Surface((self.width, self.height), 0, self._parentSurface)
		
	def Label(self, id, config = None):
		if self._label != None:
			del self._label
		self._label = TextLabel(id, self._controlSurface, config = config)
		x = (self.width - self._label.width) / 2
		y = (self.height - self._label.height) / 2
		self._label.position = (x, y)
	
	def BackgroundImage(self, id, imagePath = DEFAULT_IMAGE_PATH, hoveredImagePath = DEFAULT_HOVERED_IMAGE_PATH, clickedImagePath = DEFAULT_CLICKED_IMAGE_PATH, config = None):
		if self._backgroundImage != None:
			del self._backgroundImage
		self._backgroundImage = ImageBox(id, self._controlSurface, imagePath, hoveredImagePath, clickedImagePath, config)
		
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
