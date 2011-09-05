#!/usr/bin/env python

# 	================================ Message Box UI Component ===============================
#
#	AUTHOR: KONSTANTIN DINEV
#	DATE: APRIL 2011
#	DESCRIPTION: User Interface message box component designed for applications using 
#		graphical user interface compatible with and designed for the PYGAME library
#	CONDITIONS: Requires BaseUIComponent.py MessageBoxHeader.py Button.py ImageBox.py 
#         TextLabel.py to run
#   PROJECT BY: http://www.sarconsrealm.org
#	
#	=========================================================================================

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

class MessageBox(BaseUIComponent):
	
	_header = None						# Header of the message box
	_text = None						# Button text label
	_backgroundImage = None				# Button background image
	_minimized = False					# Indicates whether the message box is minimized
	_size = None						# Default size before minimization
	
	def __init__(self, id, parentSurface, config = None):
		BaseUIComponent.__init__(self, id, parentSurface, config)
		self._InitSurface()
		self._size = self.dimensions
		self.Message(config)
		self._header = MessageBoxHeader(id + '_header', self._controlSurface, config)
		self._header.SetAbsPosition(self.position)
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
		
	# ===================== Properties =======================
	
	@property
	def text(self):
		return self._text.text
		
	@text.setter
	def text(self, value):
		self._text.text = value
		
	@property
	def header_text(self):
		return self._header.text
		
	@header_text.setter
	def header_text(self, value):
		self._header.text = value
		
	@property
	def minimized(self):
		return self._minimized
		
	@minimized.setter
	def minimized(self, value):
		self._minimized = value
		if value:
			self.SetDimensions(self._header.GetDimensions())
			self._InitSurface()
		else:
			self.SetDimensions(self._size)
			self._InitSurface()
		
	# ===================== Methods =======================
		
	def _InitSurface(self):
		if self._controlSurface != None:
			del self._controlsSurface
		self._controlSurface = pygame.Surface((self._width, self._height), 0, self._parentSurface)
		
	def Message(self, config = None):
		if self._text != None:
			del self._text
		self._text = TextLabel(self._id + '_text', self._controlSurface, config)
	
	def MouseMove(self, event):
		BaseUIComponent.MouseMove(self, event)
		self._header.MouseMove(event)

	def Drag(self, newMousePosition):
		BaseUIComponent.Drag(self, newMousePosition)
		self._header.SetAbsPosition(self.position)
		
	def MouseDown(self, event):
		clicked = BaseUIComponent.MouseDown(self, event)
		self._header.MouseDown(event)
		return clicked
		
	def MouseUp(self, event):
		BaseUIComponent.MouseUp(self, event)
		self._header.MouseUp(event)
		
	def Render(self):
		BaseUIComponent.Render(self)
		self._controlSurface.fill((255, 255, 255))
		self._header.Render()
		pygame.draw.rect(self._parentSurface, (0, 0, 0), (self._xPosition, self._yPosition, self._width, self._height), 1)
		if not self._minimized:
			self._text.Render()
	
	def ToggleMinimized(self):
		self._minimized = not self._minimized
		if self._minimized:
			self.SetDimensions(self._header.GetDimensions())
		else:
			self.SetDimensions(self._size)
		
	def Destroy(self):
		self._disposed = True
		self.__del__()
		

		
# 	================================ Message Box Header UI Component ===============================
#
#	AUTHOR: KONSTANTIN DINEV
#	DATE: APRIL 2011
#	DESCRIPTION: User Interface message box header component designed as a helper for the message
#		box component. Contains header text, a close button and a minimize button
#	CONDITIONS: Requires BaseUIComponent.py to run
#   PROJECT BY: http://www.sarconsrealm.org
#	
#	================================================================================================

class MessageBoxHeader(BaseUIComponent):
	
	_headerLabel = None					# Text label for the header
	_minimizeButton = None				# Button for minimizing the message box
	_closeButton = None					# Button for closing(destroying) the message box
	_backgroundColor = None				# Background color for the header
	
	def __init__(self, id, parentSurface, config = None):
		BaseUIComponent.__init__(self, id, parentSurface, config)
		self._InitSurface()
		self.CloseButton(config = config)
		self.MinimizeButton(config = config)
		self.HeaderLabel(config = config)
		
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
		
	def HeaderLabel(self, config):
		if self._headerLabel != None:
			del self._headerLabel
		self._headerLabel = TextLabel(self._id + '_headerLabel', self._controlSurface, config)
		
	def MinimizeButton(self, image = DEFAULT_MINIMIZE_BUTTON_IMAGE, hoverImage = DEFAULT_MINIMIZE_BUTTON_HOVERED_IMAGE, clickImage = DEFAULT_MINIMIZE_BUTTON_CLICKED_IMAGE, config = None):
		self._minimizeButton = ImageBox(self._id + '_minimizeButton', self._controlSurface, image, hoverImage, clickImage, config)
		
	def CloseButton(self, image = DEFAULT_CLOSE_BUTTON_IMAGE, hoverImage = DEFAULT_CLOSE_BUTTON_HOVERED_IMAGE, clickImage = DEFAULT_CLOSE_BUTTON_CLICKED_IMAGE, config = None):
		self._closeButton = ImageBox(self._id + '_closeButton', self._controlSurface, DEFAULT_CLOSE_BUTTON_IMAGE, DEFAULT_CLOSE_BUTTON_HOVERED_IMAGE, DEFAULT_CLOSE_BUTTON_CLICKED_IMAGE, config)
		
	# ===================== Properties =======================
	
	@property
	def text(self):
		return self._headerLabel.text
		
	@text.setter
	def text(self, value):
		self._headerLabel.text = value
	
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
	
	