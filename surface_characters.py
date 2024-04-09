import pygame


def player(path = 'first_game\\graphics\\Player\\player_walk_1.png'):
    return pygame.image.load(path).convert_alpha()

def snail1(path='first_game\\graphics\\snail\\snail1.png'):
    return pygame.image.load(path).convert_alpha()

def snail2(path='first_game\\graphics\\snail\\snail2.png'):
    return pygame.image.load(path).convert_alpha()