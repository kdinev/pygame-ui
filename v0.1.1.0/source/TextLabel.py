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
	_font = ""									# font to display the text in
	_textSize = 0								# size of the text in pt
	_color = (0, 0, 0)							# the color of the text 
	_hoveredColor = (127, 127, 127)				# the hovered color of the text
	
	def __init__(self, id, parentSurface, upperLeftCorner = (0, 0), size = (0, 0), text = "", font = "arial", textSize = 0, color = (0, 0, 0), hoveredColor = (127, 127, 127)):
		BaseUIComponent.__init__(self, id, parentSurface, upperLeftCorner, size)
		self._text = text
		self._font = font
		self._textSize = textSize
		self._color = color
		self._hoveredColor = hoveredColor
		self._InitSurface()
		self._width = self._controlSurface.get_width()
		self._height = self._controlSurface.get_height()
		
	def __del__(self):
		BaseUIComponent.__del__(self)
		del self._color
		del self._hoveredColor
		del self._text
		del self._font
		del self._textSize
		
	def __str__(self):
		return self._text
		
	def SetText(self, newText):
		self._text = newText
		self._InitSurface()
		
	def SetFont(self, newFont):
		self._font = newFont
		self._InitSurface()
		
	def SetTextSize(self, newTextSize):
		self._textSize = newTextSize
		self._InitSurface()
		
	def SetColor(self, newColor):
		self._color = newColor
		self._InitSurface()
		
	def SetHoveredColor(self, newColor):
		self._hoveredColor = newColor
		
	def _InitSurface(self):
		font = pygame.font.SysFont(self._font, self._textSize)
		if not self._hovered:
			self._controlSurface = font.render(self._text, True, self._color)
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
		
	
	
	