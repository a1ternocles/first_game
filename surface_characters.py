import pygame


def player(path = 'graphics\\Player\\player_walk_1.png'):
    return pygame.image.load(path).convert_alpha()

def snail1(path='graphics\\snail\\snail1.png'):
    return pygame.image.load(path).convert_alpha()

def snail2(path='graphics\\snail\\snail2.png'):
    return pygame.image.load(path).convert_alpha()