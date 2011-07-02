#!/usr/bin/env python

# 	================================ Message Box Header UI Component ===============================
#
#	AUTHOR: KONSTANTIN DINEV
#	DATE: APRIL 2011
#	DESCRIPTION: User Interface message box header component designed as a helper for the message
#		box component. Contains header text, a close button and a minimize button
#	CONDITIONS: Requires BaseUIComponent.py to run
#       PROJECT BY: http://www.sarconsrealm.org
#	
#	================================================================================================

from BaseUIComponent import BaseUIComponent
from TextLabel import TextLabel
from ImageBox import ImageBox
import pygame, os

DEFAULT_MINIMIZE_BUTTON_IMAGE = os.path.join('images', 'MinimizeButtonNormal.png')
DEFAULT_MINIMIZE_BUTTON_HOVERED_IMAGE = os.path.join('images', 'MinimizeButtonHovered.png')
DEFAULT_MINIMIZE_BUTTON_CLICKED_IMAGE = os.path.join('images', 'MinimizeButtonClicked.png')
DEFAULT_CLOSE_BUTTON_IMAGE = os.path.join('images', 'CloseButtonNormal.png')
DEFAULT_CLOSE_BUTTON_HOVERED_IMAGE = os.path.join('images', 'CloseButtonHovered.png')
DEFAULT_CLOSE_BUTTON_CLICKED_IMAGE = os.path.join('images', 'CloseButtonClicked.png')

class MessageBoxHeader(BaseUIComponent):
	
	_headerLabel = None					# Text label for the header
	_minimizeButton = None				# Button for minimizing the message box
	_closeButton = None					# Button for closing(destroying) the message box
	_backgroundColor = None				# Background color for the header
	
	def __init__(self, id, parentSurface, upperLeftCorner = (0, 0), size = (0, 0), backgroundColor = (30, 30, 220)):
		BaseUIComponent.__init__(self, id, parentSurface, upperLeftCorner, size)
		self._InitSurface()
		self._backgroundColor = backgroundColor
		self.CloseButton()
		self.MinimizeButton()
		self.HeaderLabel()
		
	def __del__(self):
		del self._headerLabel
		del self._minimizeButton
		del self._closeButton
		del self._backgroundColor
		BaseUIComponent.__del__(self)
		
	def __str__(self):
		return str(self._headerLabel)
		
	def _InitSurface(self):
		self._controlSurface = pygame.Surface((self._width, 20), 0, self._parentSurface)
		
	def HeaderLabel(self, text = "Message Box", font = "arial", textSize = 18, color = (0, 0, 0), hoveredColor = (0, 0, 0)):
		if self._headerLabel != None:
			del self._headerLabel
		self._headerLabel = TextLabel(self._id + '_headerLabel', self._controlSurface, (10, 0), (self._width, self._height), text, font, textSize, color, hoveredColor)
		
	def MinimizeButton(self, image = DEFAULT_MINIMIZE_BUTTON_IMAGE, hoverImage = DEFAULT_MINIMIZE_BUTTON_HOVERED_IMAGE, clickImage = DEFAULT_MINIMIZE_BUTTON_CLICKED_IMAGE):
		self._minimizeButton = ImageBox(self._id + '_minimizeButton', self._controlSurface, (self._width - 42, 2), (16, 16), image, hoverImage, clickImage)
		
	def CloseButton(self, image = DEFAULT_CLOSE_BUTTON_IMAGE, hoverImage = DEFAULT_CLOSE_BUTTON_HOVERED_IMAGE, clickImage = DEFAULT_CLOSE_BUTTON_CLICKED_IMAGE):
		self._closeButton = ImageBox(self._id + '_closeButton', self._controlSurface, (self._width - 20, 2), (16, 16), DEFAULT_CLOSE_BUTTON_IMAGE, DEFAULT_CLOSE_BUTTON_HOVERED_IMAGE, DEFAULT_CLOSE_BUTTON_CLICKED_IMAGE)
	
	def SetBackgroundColor(self, color):
		self._backgroundColor = color
		
	def SetMinimizeCallback(self, callback):
		self._minimizeButton.SetClickCallback(callback)
		
	def SetCloseCallback(self, callback):
		self._closeButton.SetClickCallback(callback)
		
	def SetAbsPosition(self, newPosition):
		BaseUIComponent.SetAbsPosition(self, newPosition)
		self._headerLabel.SetAbsPosition(newPosition)
		self._minimizeButton.SetAbsPosition(newPosition)
		self._closeButton.SetAbsPosition(newPosition)
		
	def MouseMove(self, event):
		BaseUIComponent.MouseMove(self, event)
		self._headerLabel.MouseMove(event)
		self._minimizeButton.MouseMove(event)
		self._closeButton.MouseMove(event)
		
	def MouseDown(self, event):
		BaseUIComponent.MouseDown(self, event)
		self._headerLabel.MouseDown(event)
		self._minimizeButton.MouseDown(event)
		self._closeButton.MouseDown(event)
		
	def MouseUp(self, event):
		BaseUIComponent.MouseUp(self, event)
		self._headerLabel.MouseUp(event)
		self._minimizeButton.MouseUp(event)
		self._closeButton.MouseUp(event)
		
	def Render(self):
		BaseUIComponent.Render(self)
		self._controlSurface.fill(self._backgroundColor)
		self._headerLabel.Render()
		self._minimizeButton.Render()
		self._closeButton.Render()