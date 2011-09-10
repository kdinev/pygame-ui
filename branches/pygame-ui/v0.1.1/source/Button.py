#!/usr/bin/env python

# 	================================ Button UI Component ===============================
#
#	AUTHOR: KONSTANTIN DINEV
#	DATE: APRIL 2011
#	DESCRIPTION: User Interface button component designed for applications using 
#		graphical user interface compatible with and designed for the PYGAME library
#	CONDITIONS: Requires ImageBox.py to run
#   PROJECT BY: http://www.sarconsrealm.org
#	
#	====================================================================================

from TextLabel import TextLabel
from ImageBox import ImageBox
import pygame, os

DEFAULT_IMAGE_PATH = os.path.join('images', 'ButtonBackgroundNormal.png')
DEFAULT_HOVERED_IMAGE_PATH = os.path.join('images', 'ButtonBackgroundHovered.png')
DEFAULT_CLICKED_IMAGE_PATH = os.path.join('images', 'ButtonBackgroundClicked.png')

class Button(ImageBox):
	
	_label = None						# Button text label
	
	def __init__(self, id, parentSurface, imagePath = DEFAULT_IMAGE_PATH, hoveredImagePath = DEFAULT_HOVERED_IMAGE_PATH, clickedImagePath = DEFAULT_CLICKED_IMAGE_PATH, config = None):
		ImageBox.__init__(self, id, parentSurface, imagePath, hoveredImagePath, clickedImagePath, config)
		lbl_styling = config.InitStylingManagerByType(self.styling.xml_node, "TextLabel")
		self.Label(id + '_text', config = lbl_styling)
		x = (self.width - self._label.width) / 2
		y = (self.height - self._label.height) / 2
		self._label.position = (x, y)
		
	def __del__(self):
		ImageBox.__del__(self)
		del self._label
		
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
		
	def Label(self, id, config = None):
		if self._label != None:
			del self._label
		self._label = TextLabel(id, self._controlSurface, config = config)
		x = (self.width - self._label.width) / 2
		y = (self.height - self._label.height) / 2
		self._label.position = (x, y)
		
	def Hover(self, event):
		ImageBox.Hover(self, event)
		self._label.Hover(event)
		
	def MouseDown(self, event):
		ImageBox.MouseDown(self, event)
		if self._clicked:
			self._label.Activate()
		
	def MouseUp(self, event):
		ImageBox.MouseUp(self, event)
		self._label.Deactivate()
		
	def Unhover(self, event):
		ImageBox.Unhover(self, event)
		self._label.Unhover(event)
		
	def Render(self):
		ImageBox.Render(self)
		self._label.parent_surface = self.surface
		self._label.Render()
