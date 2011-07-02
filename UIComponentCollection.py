#!/usr/bin/env python

# 	============================== UI Component Collection Framework ==============================
#
#	AUTHOR: KONSTANTIN DINEV
#	DATE: APRIL 2011
#	DESCRIPTION: User Interface component collection designed for applications using graphical
#		user interface compatible with and designed for the PYGAME library
#   PROJECT BY: http://www.sarconsrealm.org
#	
#	===============================================================================================

import pygame
from pygame.locals import *
from sys import exit

class UIComponentCollection(object):
	
	_uiComponentCollection = None
	_currentMousePosition = None
	_focusedComponent = None
	
	def __init__(self, newCollection = []):
		self._uiComponentCollection = newCollection
		
	def __del__(self):
		for component in self._uiComponentCollection:
			del component
		
	def __add__(self, rhs):
		self._uiComponentCollection.append(rhs)
		return self
		
	def Append(self, component):
		self._uiComponentCollection.append(component)
	
	def AppendComponent(self, newComponent):
		self += newComponent
		
	def GetComponentById(self, id):
		for component in self._uiComponentCollection:
			if component.GetId() == id:
				return component
		
	def Focus(component):
		self._focusedComponent = component
		
	def RemoveFocus():
		self._focusedComponent = None
		
	def Update(self, event):
		if event.type == MOUSEMOTION:
			for component in self._uiComponentCollection:
				if not component._disposed:
					component.MouseMove(event)
				else:
					self._uiComponentCollection.remove(component)
					del component
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			for component in self._uiComponentCollection:
				if not component._disposed:
					component.MouseDown(event)
				else:
					self._uiComponentCollection.remove(component)
					del component
		elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
			for component in self._uiComponentCollection:
				if not component._disposed:
					component.MouseUp(event)
				else:
					self._uiComponentCollection.remove(component)
					del component
				
	def Render(self):
		for component in self._uiComponentCollection:
			if not component._disposed:
				component.Render()
			else:
				self._uiComponentCollection.remove(component)
				del component