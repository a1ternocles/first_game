import pygame

#------ Plain Surface- ----

def plainSurface(surface_width,surface_height):
    test_surface =  pygame.Surface((surface_width, surface_height))
    test_surface.fill('Red')
    return test_surface

def imageBackground(path):
    return pygame.image.load(path)