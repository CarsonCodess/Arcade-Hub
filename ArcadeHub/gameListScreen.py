import pygame
import os
from Text import Text
from Button import Button

texts = []


def start():
    screen = pygame.display.get_surface()

    width = pygame.display.Info().current_w
    height = pygame.display.Info().current_h
    dir_path = r'Games\\'
    games = []

    for path in os.listdir(dir_path):
        if os.path.isdir(os.path.join(dir_path, path)) and os.path.exists(os.path.join(dir_path, path, 'game.ini')):
            games.append(path)

    game_count = len(games)
    if game_count == 0:
        texts.append(Button("No Game Found", (width, height), 96))
    else:
        for i, game in enumerate(games):
            ini_path = os.path.join(dir_path, game, 'game.ini')
            name = "Unnamed Game"
            with open(ini_path, 'r') as ini:
                for line in ini:
                    if 'Title: ' in line:
                        name = line.strip().replace('Title: ', '')
                        break
            position_y = (height // (game_count + 1)) * (i + 1) * 2
            texts.append(Button(name, (width, position_y), 96))


def render(clock):
    screen = pygame.display.get_surface()

    width = pygame.display.Info().current_w
    height = pygame.display.Info().current_h

    header = Text('Games', (width, height / 7), 124)
    header.render(screen)
    for text in texts:
        text.render(screen, 0)
