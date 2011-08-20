#!/usr/bin/env python

# 	============================== Image Box UI Component ==============================
#
#	AUTHOR: KONSTANTIN DINEV
#	DATE: APRIL 2011
#	DESCRIPTION: User Interface image box component designed for applications using 
#		graphical user interface compatible with and designed for the PYGAME library
#	CONDITIONS: Requires BaseUIComponent.py to run
#   PROJECT BY: http://www.sarconsrealm.org
#	
#	====================================================================================

from BaseUIComponent import BaseUIComponent
import pygame, os

class ImageBox(BaseUIComponent):
	
	_imagePath = None
	_hoveredImagePath = None
	_clickedImagePath = None
	_loadedImage = None
	_loadedHoveredImage = None
	_loadedClickedImage = None
	
	def __init__(self, id, activeScreen, upperLeftCorner = (0, 0), size = (0, 0), imagePath = "", hoveredImagePath = "", clickedImagePath = ""):
		BaseUIComponent.__init__(self, id, activeScreen, upperLeftCorner, size)
		self._imagePath = imagePath
		self._LoadImage()
		
		if hoveredImagePath != "":
			self._hoveredImagePath = hoveredImagePath
			self._LoadHoveredImage()
		
		if clickedImagePath != "":
			self._clickedImagePath = clickedImagePath
			self._LoadClickedImage()
			
		
	def __del__(self):
		BaseUIComponent.__del__(self)
		del self._imagePath
		del self._hoveredImagePath
		del self._clickedImagePath
		del self._loadedImage
		del self._loadedHoveredImage
		del self._loadedClickedImage
		
	def __str__(self):
		return self._imagePath
		
	def _LoadImage(self):
		self._loadedImage = pygame.image.load(self._imagePath).convert_alpha()
		if self._width == self._height == 0:
			self._width = self._loadedImage.get_width()
			self._height = self._loadedImage.get_height()
		self._InitSurface()
			
	def _LoadHoveredImage(self):
		self._loadedHoveredImage = pygame.image.load(self._hoveredImagePath).convert_alpha()
		
	def _LoadClickedImage(self):
		self._loadedClickedImage = pygame.image.load(self._clickedImagePath).convert_alpha()
		
	def SetImage(self, newImage):
		self._imagePath = newImage
		self._LoadImage()
		
	def SetHoveredImage(self, newImage):
		self._hoveredImagePath = newImage
		self._LoadHoveredImage()
		
	def SetClickedImage(self, newImage):
		self._clickedImagePath = newImage
		self._LoadClickedImage()
		
	def _InitSurface(self):
		if self._clicked:
			self._controlSurface = self._loadedClickedImage
		elif self._hovered:
			self._controlSurface = self._loadedHoveredImage
		else:
			self._controlSurface = self._loadedImage
		
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
		
	def MouseUp(self, event):
		BaseUIComponent.MouseUp(self, event)
		self._InitSurface()
		
	
		
	