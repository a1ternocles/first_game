import pygame

def surfaceText(texting):
    
    font_type = 'first_game\\font\\Pixeltype.ttf'
    font_style = 28

    text_info = texting
    antialias_info = False
    color = 'Black'
    
    font = pygame.font.Font(font_type,font_style)
    text = font.render(text_info,
                       antialias_info,
                       color)

    return text.convert()
