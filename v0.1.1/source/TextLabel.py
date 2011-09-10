#!/usr/bin/env python

# 	============================== TextLabel UI Component ==============================
#
#	AUTHOR: KONSTANTIN DINEV
#	DATE: APRIL 2011
#	DESCRIPTION: User Interface text label component designed for applications using 
#		graphical user interface compatible with and designed for the PYGAME library
#	CONDITIONS: Requires BaseUIComponent.py to run
#       PROJECT BY: http://www.sarconsrealm.org
#	
#	====================================================================================

from BaseUIComponent import BaseUIComponent
import pygame

class TextLabel(BaseUIComponent):
	_text = ""									# text of the label
	_hoveredColor = (255, 30, 30)				# the hovered color of the text
	
	def __init__(self, id, parentSurface, config = None):
		BaseUIComponent.__init__(self, id, parentSurface, config)
		self._InitSurface()
		self.width = self._controlSurface.get_width()
		self.height = self._controlSurface.get_height()
		
	def __del__(self):
		BaseUIComponent.__del__(self)
		del self._hoveredColor
		del self._text
		
	def __str__(self):
		return self._text
		
	@property
	def text(self):
		return self._text
		
	@text.setter
	def text(self, value):
		self._text = value
		self._InitSurface()
		self.width = self._controlSurface.get_width()
		self.height = self._controlSurface.get_height()
		
	@property
	def font_family(self):
		return self.styling.font_family
	
	@font_family.setter
	def font_family(self, value):
		self.styling.font_family = value
		self._InitSurface()
		
	@property
	def font_size(self):
		return self.styling.font_size
		
	@font_size.setter
	def font_size(self, value):
		self.styling.font_size = value
		self._InitSurface()
		
	@property
	def color(self):
		return self.styling.color
		
	@color.setter
	def color(self, value):
		self.styling.color = value
		self._InitSurface()
		
	@property
	def hover_color(self):
		return self._hoveredColor
		
	@hover_color.setter
	def hover_color(self, value):
		self._hoveredColor = newColor
		
	def _InitSurface(self):
		font = pygame.font.SysFont(self.font_family, self.font_size)
		if not self._hovered:
			self._controlSurface = font.render(self._text, True, self.color)
		else:
			self._controlSurface = font.render(self._text, True, self._hoveredColor)
		
	def Hover(self, event):
		BaseUIComponent.Hover(self, event)
		self._InitSurface()
		
	def Unhover(self, event):
		BaseUIComponent.Unhover(self, event)
		self._InitSurface()
		
	def Activate(self):
		BaseUIComponent.Activate(self)
		self._InitSurface()
		
	def Deactivate(self):
		BaseUIComponent.Deactivate(self)
		self._InitSurface()
		
	
	
	