#!/usr/bin/env python

# 	============================== Base UI Component Model ================================
#
#	AUTHOR: KONSTANTIN DINEV
#	DATE: APRIL 2011
#	DESCRIPTION: User Interface base component designed for applications using graphical 
#		user interface compatible with and designed for the PYGAME library
#	CONDITIONS: Use with the UIComponentCollection class
#   PROJECT BY: http://www.sarconsrealm.org
#	
#	=======================================================================================
from ConfigurationManager import *
import pygame

CLICK 	= pygame.USEREVENT + 1
DRAG  	= pygame.USEREVENT + 2
HOVER 	= pygame.USEREVENT + 3
UNHOVER = pygame.USEREVENT + 4
COUNT 	= pygame.USEREVENT + 5

class BaseUIComponent(object):
	
	# ====================================== Members ======================================
	_id = ''					# component's string identifier
	_parentSurface = None 		# surface screen to render the control at
	_controlSurface = None		# control's surface created on the screen
	_styling = None				# the new css-like styling from xml which would take over 
								# the below definitions inside the component
	_data = None				# Holds the data manager instance
	_absX = 0					# upper left corner absolute x-axis position 
	_absY = 0					# upper left corner absolute y-axis position
	_draggable = False			# enables the surface to be draggable
	_oldMousePosition = None	# updates mouse position in case of draggable
	_resizable = False			# enables the surface to be resizable
	_hovered = False			# flag indicating whether the control is hovered
	_clicked = False			# flag used to determine if mousedown and mouseup are both
								# within the same component
	_hoverCallback = None		# callback function executed on hover
	_clickCallback = None		# callback function executed on click
	_disposed = False			# THIS IS HERE TEMPORARILY
	
	# ========================= CONSTRUCTORS AND DESTRUCTORS =========================
	
	def __init__(self, id, parentSurface, config = None):
		self._id = id
		self._parentSurface = parentSurface
		if isinstance(config, ConfigurationManager):
			self.styling = config.InitStylingManager(id)
			if self.styling == None:
				self.styling = StylingManager()
		elif isinstance(config, StylingManager):
			self.styling = config
		else:
			self.styling = StylingManager()
		
	def __del__(self):
		if self._controlSurface != None:
			del self._controlSurface
		if self._parentSurface != None:
			del self._parentSurface
		if self._hoverCallback != None:
			del self._hoverCallback
		if self._clickCallback != None:
			del self._clickCallback
		if self._styling != None:
			del self._styling
			
	def __str__(self):
		return self._id
		
	# =========================== ACCESSORS AND MODIFIERS ==========================
	# ========================= new-style class properties =========================
	
	@property
	def rectangle(self):
		return self._controlSurface.get_rect(topleft=(self._absX + self.left, self._absY + self.top), w=self.width, h=self.height)
		
	@property
	def hover_callback(self):
		return self._hoverCallback
		
	@hover_callback.setter
	def hover_callback(self, value):
		self._hoverCallback = value
		
	@property
	def click_callback(self):
		return self._clickCallback
		
	@click_callback.setter
	def click_callback(self, value):
		self._clickCallback = value
		
	@property
	def width(self):
		return self.styling.width
		
	@width.setter
	def width(self, value):
		self.styling.width = value
		
	@property
	def height(self):
		return self.styling.height
		
	@height.setter
	def height(self, value):
		self.styling.height = value
	
	@property
	def dimensions(self):
		return (self.width, self.height)
	
	@dimensions.setter
	def dimensions(self, value):
		self.width, self.height = value
		
	@property
	def position(self):
		return (self.left, self.top)
	
	@position.setter
	def position(self, value):
		self.left, self.top = value
		
	@property
	def top(self):
		return self.styling.top
		
	@top.setter
	def top(self, value):
		self.styling.top = value
		
	@property
	def left(self):
		return self.styling.left
		
	@left.setter
	def left(self, value):
		self.styling.left = value
		
	@property
	def visibility(self):
		return self.styling.visibility
		
	@visibility.setter
	def visibility(self, value):
		self.styling.visibility = value
		
	@property
	def background_color(self):
		return self.styling.background_color
		
	@background_color.setter
	def background_color(self):
		self.styling.background_color = value
		
	@property
	def abs_position(self):
		return (self._absX, self._absY)
		
	@abs_position.setter
	def abs_position(self, value):
		self._absX, self._absY = value
		
	@property
	def id(self):
		return self._id
		
	@id.setter
	def id(self, value):
		self._id = id
		
	@property
	def surface(self):
		return self._controlSurface
	
	@property
	def transparency(self):
		return self._controlSurface.get_alpha()
	
	@transparency.setter
	def transparency(self, value):
		self._controlSurface.set_alpha(value)
		
	@property
	def draggable(self):
		return self._draggable
		
	@draggable.setter
	def draggable(self, value):
		self._draggable = value
		
	@property
	def styling(self):
		return self._styling
		
	@styling.setter
	def styling(self, value):
		self._styling = value
		
	@property
	def parent_surface(self):
		return self._parentSurface
		
	@parent_surface.setter
	def parent_surface(self, value):
		self._parentSurface = value
		
	# ========================= RENDERER =========================	
		
	def Render(self):
		if self.visibility == 'visible':
			self._parentSurface.blit(self._controlSurface, dest=self.position, area=(0, 0, self.width, self.height))
			if self.background_color != None:
				self._controlSurface.fill(self.background_color)
			
	
	# ========================= EVENT HANDLERS =========================
	
	def MouseMove(self, event):
		newMousePosition = pygame.mouse.get_pos()
		rect = self.rectangle
		if self._clicked and self.draggable:
			self.Drag(newMousePosition)
		else:
			hovered = rect.collidepoint(newMousePosition)
			if not self._hovered and hovered:
				self.Hover(event)
			elif self._hovered and not hovered:
				self.Unhover(event)
	
	def Drag(self, newMousePosition):
		pygame.event.post(pygame.event.Event(DRAG, component=self))
		delta = (self._oldMousePosition[0] - newMousePosition[0], self._oldMousePosition[1] - newMousePosition[1])
		self.left -= delta[0]
		self.top -= delta[1]
		self._oldMousePosition = newMousePosition
			
	# Mouse down activates the component if the event is within the component's bounds
	def MouseDown(self, event):
		newMousePosition = pygame.mouse.get_pos()
		self._oldMousePosition = newMousePosition
		rect = self.rectangle
		clicked = rect.collidepoint(newMousePosition)
		if clicked:
			self.Activate()
			return True
		return False
	
	# Mouse up fires click on the component if released within the component's bounds
	# and if the mouse down has also been within component's bounds
	def MouseUp(self, event):
		newMousePosition = pygame.mouse.get_pos()
		rect = self.rectangle
		clicked = rect.collidepoint(newMousePosition)
		if self._clicked and clicked:
			self.Click(event)
		self.Deactivate()
	
	# ========= SECTION OF EVENT METHODS NEEDING A SPECIFIC OVERLOAD WITHIN EACH COMPONENT =========
	
	def Hover(self, event):
		pygame.event.post(pygame.event.Event(HOVER, component=self))
		self._hovered = True
		if self._hoverCallback != None:
			self._hoverCallback()
	
	def Unhover(self, event):
		pygame.event.post(pygame.event.Event(UNHOVER, component=self))
		self._hovered = False
		
	def Activate(self):
		self._clicked = True
		
	def Deactivate(self):
		self._clicked = False
		
	def Click(self, event):
		# To do: Implement additional enumeration for the new events that would be pushed
		# 		onto the events queue
		# pygame.event.post(pygame.event.Event('ComponentClick', {'id': self._id}))
		# To do: Enumerate all new client events
		pygame.event.post(pygame.event.Event(CLICK, component=self))
		if self._clickCallback != None:
			self._clickCallback()
	
	
