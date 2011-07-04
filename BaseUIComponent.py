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
import pygame

class ComponentStyle:
	_top = 0
	_left = 0
	_width = 0
	_height = 0
	_backgroundImage = None
	_backgroundColor = None
	_color = None
	_fontSize = None
	_textAlign = None

class BaseUIComponent(object):
	
	# ====================================== Members ======================================
	_id = ''					# component's string identifier
	_parentSurface = None 		# surface screen to render the control at
	_controlSurface = None		# control's surface created on the screen
	_xPosition = 0				# upper left corner x-axis position relative to parent 
	_yPosition = 0				# upper left corner y-axis position relative to parent
	_absX = 0					# upper left corner absolute x-axis position 
	_absY = 0					# upper left corner absolute y-axis position
	_width = 0					# surface rectangle's width
	_height = 0					# surface recrangle's height
	_draggable = False			# enables the surface to be draggable
	_hovered = False			# flag indicating whether the control is hovered
	_clicked = False			# flag used to determine if mousedown and mouseup are both
								# within the same component
	_hoverCallback = None		# callback function executed on hover
	_clickCallback = None		# callback function executed on click
	_disposed = False			# THIS IS HERE TEMPORARILY
	
	# ========================= CONSTRUCTORS AND DESTRUCTORS =========================
	
	def __init__(self, id, parentSurface, upperLeftCorner = (0, 0), size = (0, 0)):
		self._id = id
		self._parentSurface = parentSurface
		self._xPosition = upperLeftCorner[0]
		self._yPosition = upperLeftCorner[1]
		self._width = size[0]
		self._height = size[1]
		
	def __del__(self):
		self._disposed = True
		del self._controlSurface
		del self._parentSurface
		if self._hoverCallback != None:
			del self._hoverCallback
		if self._clickCallback != None:
			del self._clickCallback
			
	def __str__(self):
		return self._id
		
	# ========================= ACCESSORS AND MODIFIERS =========================
	
	def GetRectangle(self):
		return self._controlSurface.get_rect(topleft=(self._absX + self._xPosition, self._absY + self._yPosition))
		
	def SetHoverCallback(self, callback):
		self._hoverCallback = callback
		
	def SetClickCallback(self, callback):
		self._clickCallback = callback
		
	def GetWidth(self):
		return self._width
		
	def SetWidth(self, newWidth):
		self._width = newWidth
		
	def GetHeight(self):
		return self._height
		
	def SetHeight(self, newHeight):
		self._height = newHeight
		
	def SetDimensions(self, newDim):
		self._width, self._height = newDim
		
	def GetDimensions(self):
		return self._width, self._height
		
	def GetPosition(self):
		return (self._xPosition, self._yPosition)
		
	def SetPosition(self, newPosition):
		self._xPosition, self._yPosition = newPosition
		
	def GetAbsPosition(self):
		return (self._absX, self._absY)
		
	def SetAbsPosition(self, newPosition):
		self._absX, self._absY = newPosition
		
	def GetId(self):
		return self._id
		
	def Surface():
		return self._controlSurface
		
	# ========================= RENDERER =========================	
		
	def Render(self):
		self._parentSurface.blit(self._controlSurface, (self._xPosition, self._yPosition), area=(0, 0, self._width, self._height))
			
	
	# ========================= EVENT HANDLERS =========================
	
	def MouseMove(self, event):
		newMousePosition = pygame.mouse.get_pos()
		rect = self.GetRectangle()
		hovered = rect.collidepoint(newMousePosition)
		if not self._hovered and hovered:
			self.Hover(event)
		elif self._hovered and not hovered:
			self.Unhover(event)
			
	# Mouse down activates the component if the event is within the component's bounds
	def MouseDown(self, event):
		newMousePosition = pygame.mouse.get_pos()
		rect = self.GetRectangle()
		clicked = rect.collidepoint(newMousePosition)
		if clicked:
			self.Activate()
			return True
		return False
	
	# Mouse up fires click on the component if released within the component's bounds
	# and if the mouse down has also been within component's bounds
	def MouseUp(self, event):
		newMousePosition = pygame.mouse.get_pos()
		rect = self.GetRectangle()
		clicked = rect.collidepoint(newMousePosition)
		if self._clicked and clicked:
			self.Click(event)
		self.Deactivate()
	
	# ========= SECTION OF EVENT METHODS NEEDING A SPECIFIC OVERLOAD WITHIN EACH COMPONENT =========
	# 
	# 	To do: How to get dynamic arguments for the callback functions
	#	Update: Arguements for the callback are the component and the event
	
	def Hover(self, event):
		self._hovered = True
		if self._hoverCallback != None:
			self._hoverCallback(self, event)
	
	def Unhover(self, event):
		self._hovered = False
		
	def Activate(self):
		self._clicked = True
		
	def Deactivate(self):
		self._clicked = False
		
	def Click(self, event):
		# To do: Implement additional enumeration for the new events that would be pushed
		# 		onto the events queue
		# pygame.event.post(pygame.event.Event('ComponentClick', {'id': self._id}))
		if self._clickCallback != None:
			self._clickCallback(self, event)
	
	
