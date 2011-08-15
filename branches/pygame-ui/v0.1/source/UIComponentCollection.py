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
from ConfigurationManager import ConfigurationManager
from TextLabel import TextLabel
from ImageBox import ImageBox
from Button import Button
from MessageBox import MessageBox

class UIComponentCollection(object):
	
	_uiComponentCollection = None
	_currentMousePosition = None
	_focusedComponent = None
	_configManager = None
	
	def __init__(self, config = None, newCollection = []):
		self._uiComponentCollection = newCollection
		if config != None:
			self._configManager = ConfigurationManager(config)
			self.InitComponents()
		
	def __del__(self):
		for component in self._uiComponentCollection:
			del component
		
	def __add__(self, rhs):
		self._uiComponentCollection.append(rhs)
		return self
		
	def __sub__(self, rhs):
		for component in self._uiComponentCollection:
			if component.GetId() == rhs.GetId():
				self._uiComponentCollection.remove(component)
				del component
		
	def InitComponents():
		componentList = self._configManager.FindAllComponents()
		for entry in componentList:
			if entry[1] == 'TextLabel':
				self += TextLabel(id = entry[0], config = entry[2])
			elif entry[1] == 'ImageBox':
				self += ImageBox(id = entry[0], config = entry[2])
			elif entry[1] == 'Button':
				self += Button(id = entry[0], config = entry[2])
			elif entry[1] == 'MessageBox':
				self += MessageBox(id = entry[0], config = entry[2])
		
		
	def Append(self, component):
		self._uiComponentCollection.append(component)
	
	def AppendComponent(self, newComponent):
		self += newComponent
		
	def GetComponentById(self, id):
		for component in self._uiComponentCollection:
			if component.id == id:
				return component
		
	def Focus(self, component):
		self._focusedComponent = component
		
	def RemoveFocus(self):
		if self._focusedComponent != None:
			del self._focusedComponent
		self._focusedComponent = None
		
	def Update(self, event):
		if event.type == MOUSEMOTION:
			for component in self._uiComponentCollection:
				if not component._disposed:
					component.MouseMove(event)
				else:
					self._uiComponentCollection.remove(component)
					if self._focusedComponent == component:
						self.RemoveFocus()
					del component
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			if self._focusedComponent != None:
				if self._focusedComponent.MouseDown(event):
					return
					
			for i in range(-1, -(len(self._uiComponentCollection) + 1), -1):
				component = self._uiComponentCollection[i]
				if not component._disposed:
					active = component.MouseDown(event)
					if active:
						self.Focus(component)
						self._uiComponentCollection.remove(component)
						self._uiComponentCollection.append(component)
						return
				else:
					self._uiComponentCollection.remove(component)
					if self._focusedComponent == component:
						self.RemoveFocus()
					del component
			else:
				self.RemoveFocus()
		elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
			for component in self._uiComponentCollection:
				if not component._disposed:
					component.MouseUp(event)
				else:
					self._uiComponentCollection.remove(component)
					if self._focusedComponent == component:
						self.RemoveFocus()
					del component
				
	def Render(self):
		for component in self._uiComponentCollection:
			if not component._disposed:
				component.Render()
			else:
				self._uiComponentCollection.remove(component)
				if self._focusedComponent == component:
						self.RemoveFocus()
				del component