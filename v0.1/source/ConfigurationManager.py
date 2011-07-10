#!/usr/bin/env python

# 	=============================== Configuration Manager =================================
#
#	AUTHOR: KONSTANTIN DINEV
#	DATE: July 2011
#	DESCRIPTION: Configuration manager designed for pygame-ui component framework. This
#		manager takes xml configuration for components and initializes styling and other
#		framework configurations
#	CONDITIONS: Used by the BaseUIComponent class to initialize individual component 
#		styling
#	VISION: Initial precondition for designer and design time development
#   PROJECT BY: http://www.sarconsrealm.org
#	
#	=======================================================================================
from xml.dom.minidom import parse

class ConfigurationManager:
	_parsedDom = None
	_stylingElement = None
	
	def __init__(self, xmlPath):
		try:
			xmlReader = open(xmlPath)
		except IOError:
			print('No such file or directory')
			raise IOError('Incorrect configuration path provided')
			
		try:
			self._parsedDom = parse(xmlReader)
		except TypeError, AttributeError:
			print('Error processing the configuration')
			xmlReader.close()
			
		xmlReader.close()
	
	# returns object of type ComponentStyle or None if a component with the specified id does not exist 
	# in the current configuration
	def InitComponentStyle(self, componentId):
		if self._parsedDom.documentElement.nodeName != 'configuration':
			raise TypeError('Incorrect root node: pygame-ui config requires configuration as its root element')
		self._stylingElement = self._parsedDom.documentElement.getElemenetsByTagName('styling')[0]
		if self._stylingElement = None:
			raise TypeError('Component node does not exist in the current configuration')
		
		for child in self._stylingElement.childNodes:
			if child.nodeName == 'component':
				if child.getAttribute('id') == componentId:
					return ComponentStyle(child)
		else:
			return None

class ComponentStyle:
	_initialized = False
	_top = 0
	_left = 0
	_width = 0
	_widthUnit = 'px'
	_height = 0
	_heightUnit = 'px'
	_backgroundImage = None
	_backgroundColor = None
	_color = None
	_fontSize = 0
	_fontFamily = None
	_textAlign = 'left'
	_xmlNode = None
	
	def __init__(self, componentNode):
		self._xmlNode = componentNode
		
	def GetDimensions(self):
		if not self._initialized:
			self.InitStyles()
			
		return (self._width, self._height)
		
	def GetWidth(self):
		if not self._initialized:
			self.InitStyles()
			
		return self._width
		
	def GetHeight(self):
		if not self._initialized:
			self.InitStyles()
			
		return self._height
		
	def GetPosition(self):
		if not self._initialized:
			self.InitStyles()
		
		return (self._top, self._left)
			
			
	def InitStyles(self):
		if self._xmlNode == None:
			raise TypeError('Component configuration node not found')
		else:
			for child in self._xmlNode.childNodes:
				if child.nodeName == 'width:
					unit = child.getAttribute('unit')
					if unit != None:
						self._widthUnit = unit
					self._width = int(child.firstChild.data)
				elif child.nodeName == 'height':
					unit = child.getAttribute('unit')
					if unit != None:
						self._heightUnit = unit
					self._height = int(child.firstChild.data)
				elif child.nodeName == 'top':
					self._top = int(child.firstChild.data)
				elif child.nodeName == 'left':
					self._left = int(child.firstChild.data)
				elif child.nodeName == 'fontFamily':
					self._fontFamily = child.firstChild.data
				elif child.nodeName == 'fontSize':
					self._fontSize = child.firstChild.data
			self._initialized = True
					
					