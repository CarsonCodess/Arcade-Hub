import importlib

import pygame
import os

import __main__
from Text import Text
from GameSelectButton import GameSelectButton
from Game import Game
import __main__

buttons = []


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
    buttons.clear()
    if game_count == 0:
        buttons.append(GameSelectButton("No Game Found", (width, height), 96, ""))
    else:
        for i, game in enumerate(games):
            ini_path = os.path.join(dir_path, game, 'game.ini')
            name = "Unnamed Game"
            main = ""
            with open(ini_path, 'r') as ini:
                for line in ini:
                    if 'Title: ' in line:
                        name = line.strip().replace('Title: ', '')
                    if 'Main: ' in line:
                        main = line.strip().replace('Main: ', '')
            position_y = (height // (game_count + 1)) * (i + 1) * 2
            buttons.append(GameSelectButton(name, (width, position_y), 96, os.path.join(r'Games', game, main)))


currentGame = None


def render():
    screen = pygame.display.get_surface()

    width = pygame.display.Info().current_w
    height = pygame.display.Info().current_h

    header = Text('Games', (width, height / 7), 124)
    header.render(screen)
    for text in buttons:
        text.render(screen, pygame.time.get_ticks())

    if currentGame is None:
        textColor = (201, 201, 201)
        mouse = pygame.mouse.get_pos()
        for btn in buttons:
            if btn.isInsideOf(mouse):
                btn.setColor('black')
            else:
                btn.setColor(textColor)
    else:
        currentGame.render(None, screen)


def onClick():
    global currentGame
    mouse = pygame.mouse.get_pos()
    for btn in buttons:
        if btn.isInsideOf(mouse):
            module = importlib.import_module(str(btn.getFilePath()).replace('\\', '.'))
            lis = list(str(btn.getFilePath()).split("\\"))
            length = len(lis)
            game = getattr(module, lis[length - 1])
            currentGame = game
            currentGame.startGame(None)
            __main__.onInGame()

