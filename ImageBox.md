# Introduction #

ImageBox component supports all image types supported by pygame. The image is essentially loaded via pygame.image.load function and is then wrapped as a surface object component and it supports and fires all events provided by the pygame-ui framework.


# Details #

Pygame-UI ImageBox is a component directly inheriting the BaseUIComponent. It does not wrap any other Pygame-UI components in itself and thus is used as a base component for loading any images using the framework.