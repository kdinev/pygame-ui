#!/usr/bin/env python

# 	================================ Message Box UI Component ===============================
#
#	AUTHOR: KONSTANTIN DINEV
#	DATE: APRIL 2011
#	DESCRIPTION: User Interface message box component designed for applications using 
#		graphical user interface compatible with and designed for the PYGAME library
#	CONDITIONS: Requires BaseUIComponent.py MessageBoxHeader.py Button.py ImageBox.py 
#         TextLabel.py to run
#       PROJECT BY: http://www.sarconsrealm.org
#	
#	=========================================================================================

from BaseUIComponent import BaseUIComponent
from MessageBoxHeader import MessageBoxHeader
from TextLabel import TextLabel
import pygame

class MessageBox(BaseUIComponent):
	
	_header = None						# Header of the message box
	_text = None						# Button text label
	_backgroundImage = None				# Button background image
	_minimized = False					# Indicates whether the message box is minimized
	
	def __init__(self, id, parentSurface, upperLeftCorner = (0, 0), size = (0, 0), text = "No text currently", minimized = False):
		BaseUIComponent.__init__(self, id, parentSurface, upperLeftCorner, size)
		self._InitSurface()
		self.Message(text, 'arial', 12, (0, 0, 0), (0, 0, 0))
		self._header = MessageBoxHeader(id + '_header', self._controlSurface, (0, 0), (self._width, 20))
		self._header.SetAbsPosition(upperLeftCorner)
		self._minimized = minimized
		self._header.SetMinimizeCallback(self.ToggleMinimized)
		self._header.SetCloseCallback(self.Destroy)
		
	def __del__(self):
		if self._text != None:
			del self._text
		if self._backgroundImage != None:
			del self._backgroundImage
		if self._header != None:
			del self._header
		BaseUIComponent.__del__(self)
		
	def __str__(self):
		return str(self._text)
		
	def SetMinimized(self, value):
		self._minimized = value
		
	def GetMinimized(self):
		return self._minimized
		
	def _InitSurface(self):
		self._controlSurface = pygame.Surface((self._width, self._height), 0, self._parentSurface)
		
	def Message(self, text = "", font = "arial", textSize = 0, color = (0, 0, 0), hoveredColor = (127, 127, 127)):
		if self._text != None:
			del self._text
		self._text = TextLabel(self._id + '_text', self._controlSurface, (10, 25), (self._width - 20, self._height - 30), text, font, textSize, color, hoveredColor)
	
	def MouseMove(self, event):
		BaseUIComponent.MouseMove(self, event)
		self._header.MouseMove(event)
		
	def MouseDown(self, event):
		BaseUIComponent.MouseDown(self, event)
		self._header.MouseDown(event)
		
	def MouseUp(self, event):
		BaseUIComponent.MouseUp(self, event)
		self._header.MouseUp(event)
		
	def Render(self):
		BaseUIComponent.Render(self)
		self._controlSurface.fill((255, 255, 255))
		self._header.Render()
		if not self._minimized:
			pygame.draw.rect(self._parentSurface, (0, 0, 0), (self._xPosition, self._yPosition, self._width, self._height), 1)
			self._text.Render()
	
	def ToggleMinimized(self, control, event):
		self._minimized = not self._minimized
		
	def Destroy(self, control, event):
		self._disposed = True
	
	