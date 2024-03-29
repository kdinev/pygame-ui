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
		except (TypeError, AttributeError):
			print('Error processing the configuration')
			xmlReader.close()
			
		xmlReader.close()
	
	# returns object of type ComponentStyle or None if a component with the specified id does not exist 
	# in the current configuration
	def InitComponentStyle(self, componentId):
		if self._parsedDom.documentElement.nodeName != 'configuration':
			raise TypeError('Incorrect root node: pygame-ui config requires configuration as its root element')
		if self._stylingElement == None:
			self._stylingElement = self._parsedDom.documentElement.getElementsByTagName('styling')[0]
		if self._stylingElement == None:
			raise TypeError('Component node does not exist in the current configuration')
		
		for child in self._stylingElement.childNodes:
			if child.nodeName == 'component':
				if child.getAttribute('id') == componentId:
					return ComponentStyle(child)
		else:
			return None
			
	
			
	def FindAllComponents(self):
		if self._parsedDom.documentElement.nodeName != 'configuration':
			raise TypeError('Incorrect root node: pygame-ui config requires configuration as its root element')
		if self._stylingElement == None:
			self._stylingElement = self._parsedDom.documentElement.getElementsByTagName('styling')[0]
		if self._stylingElement == None:
			raise TypeError('Component node does not exist in the current configuration')
		
		componentList = []
		for child in self._stylingElement.childNodes:
			if child.nodeName == 'component':
				componentList.append((child.getAttribute('id'), child.getAttribute('type'), ComponentStyle(child)))
				
		return componentList

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
	_verticalAlign = 'top'
	_xmlNode = None
	
	def __init__(self, componentNode):
		self._xmlNode = componentNode
		
	def __str__(self):
		return('{\n top: {0};\n left: {1};\n width: {2}{3};\n height: {4}{5};\n background-image: url({6});\n }\n', self.top, self.left, self.width, self.width_unit, self.height, self.height_unit, self.background_image)
		
	# ========================= Properties =========================
	
	@property
	def dimensions(self):
		if not self._initialized:
			self.InitStyles()
		return (self._width, self._height)
		
	@dimensions.setter
	def dimensions(self, value):
		self._width, self._height = value
		
	@property
	def width(self):
		if not self._initialized:
			self.InitStyles()
			
		return self._width
		
	@width.setter
	def width(self, value):
		self._width = value
		
	@property
	def width_unit(self):
		if not self._initialized:
			self.InitStyles()
			
		return self._widthUnit
	
	@property
	def height(self):
		if not self._initialized:
			self.InitStyles()
			
		return self._height
		
	@height.setter
	def height(self, value):
		self._height = value
		
	@property
	def height_unit
		if not self._initialized:
			self.InitStyles()
			
		return self._heightUnit
		
	@property
	def position(self):
		if not self._initialized:
			self.InitStyles()
		
		return (self._top, self._left)
		
	@position.setter
	def position(self, value):
		self._top, self._left = value
	
	@property
	def top(self):
		if not self._initialized:
			self.InitStyles()
		
		return self._top
		
	@top.setter
	def top(self, value):
		self._top = value
		
	@property
	def left(self):
		if not self._initialized:
			self.InitStyles()
		
		return self._left
		
	@left.setter
	def left(self, value):
		self._left = value
	
	@property
	def background_image(self):
		if not self._initialized:
			self.InitStyles()
		
		return self._backgroundImage
	
	@background_image.setter
	def background_image(self, value):
		self._backgroundImage = value
		
	@property
	def background_color(self):
		if not self._initialized:
			self.InitStyles()
			
		return self._backgroundColor
		
	@background_color.setter
	def background_color(self, value):
		self._backgroundColor = value
		
	@property
	def color(self):
		if not self._initialized:
			self.InitStyles()
			
		return self._color
		
	@color.setter
	def color(self, value):
		self._color = value
		
	@property
	def font_size(self):
		if not self._initialized:
			self.InitStyles()
			
		return self._fontSize
		
	@font_size.setter
	def font_size(self, value):
		self._fontSize = value
		
	@property
	def font_family(self):
		if not self._initialized:
			self.InitStyles()
			
		return self._fontFamily
		
	@font_family.setter
	def font_family(self, value):
		self._fontFamily = value
	
	@property
	def text_align(self):
		if not self._initialized:
			self.InitStyles()
			
		return self._textAlign
		
	@text_align.setter
	def text_align(self, value):
		self._textAlign = value
		
	@property
	def vertical_align(self):
		if not self._initialized:
			self.InitStyles()
			
		return self._verticalAlign
	
	@vertical_align.setter
	def vertical_align(self, value):
		self._verticalAlign = value
			
	def InitStyles(self):
		if self._xmlNode == None:
			raise TypeError('Component configuration node not found')
		else:
			for child in self._xmlNode.childNodes:
				if child.nodeName == 'width':
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
				elif child.nodeName == 'backgroundImage':
					self._backgroundImage = child.firstChild.data
				elif child.nodeName == 'backgroundColor':
					self._backgroundColor = self.ParseColor(child.firstChild.data)
				elif child.nodeName == 'color':
					self._color = self.ParseColor(child.firstChild.data)
				elif child.nodeName == 'textAlign':
					self._textAlign = child.firstChild.data
				elif child.nodeName == 'verticalAlign':
					self._verticalAlign = child.firstChild.data
					
			self._initialized = True
					
	def ParseColor(self, color):
		# RGB color definition
		if color[0] == '#':
			color = color[1:]
			if len(color) == 6:
				return pygame.Color(int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16))
			elif len(color) == 3:
				return pygame.Color(int(color[0:1] * 2, 16), int(color[1:2] * 2, 16), int(color[2:3] * 2, 16))
		# else:
		# parse color of type keyword e.g. Black, red, YELLOW, etc.