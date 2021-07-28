from os import path
import pyglet
import random

from engine.game import Game
from monsters.heavy_monster import HeavyMonster
from monsters.fast_monster import FastMonster
from monsters.speed_monster import SpeedMonster
from monsters.shield_monster import ShieldMonster


def get_random():
    return random.uniform(0.05, 0.90)

# ------- Your Code Here -------


background_file = 'assets/background/game_background.png'
game = Game(background_file, lives=3)

game.add_finish((0.97, 0.85))
game.add_finish((0.97, 0.94))

path = [
    (0.0, 0.29),
    (0.165, 0.28),
    (0.23, 0.24),
    (0.29, 0.26),
    (0.34, 0.24),
    (0.57, 0.24),
    (0.63, 0.29),
    (0.65, 0.4),
    (0.63, 0.48),
    (0.57, 0.53),
    (0.4, 0.56),
    (0.34, 0.7),
    (0.4, 0.845),
    (1.1, 0.845),
]

tower_spots = [
    (0.376, 0.421,),
    (0.525, 0.425,),
    (0.75, 0.425,),
    (0.455, 0.12,),
    (0.455, 0.74,),
    (0.612, 0.745,),
    (0.768, 0.745,),
]

game.add_tower_spots(tower_spots)

monsters = [
    FastMonster(path, 0),
    FastMonster(path, 1),
    HeavyMonster(path, 0.5),
    FastMonster(path, 2),
    FastMonster(path, 0),
    FastMonster(path, 1),
    HeavyMonster(path, 3),
    FastMonster(path, 0),
    FastMonster(path, 1),
    HeavyMonster(path, 0.5),
    FastMonster(path, 2),
    ShieldMonster(path, 0),
    FastMonster(path, 1),
    HeavyMonster(path, 3),
    FastMonster(path, 0),
    SpeedMonster(path, 1),
    HeavyMonster(path, 0.5),
    FastMonster(path, 2),
    ShieldMonster(path, 0),
    FastMonster(path, 1),
    HeavyMonster(path, 3),
    FastMonster(path, 0),
    SpeedMonster(path, 1),
    HeavyMonster(path, 0.5),
    FastMonster(path, 2),
    FastMonster(path, 0),
    FastMonster(path, 1),
    HeavyMonster(path, 3),
    FastMonster(path, 0),
    FastMonster(path, 1),
    HeavyMonster(path, 0.5),
    FastMonster(path, 2),
    FastMonster(path, 0),
    FastMonster(path, 1),
    HeavyMonster(path, 3),
    HeavyMonster(path, 1),
    ShieldMonster(path, 1),
    SpeedMonster(path, 1),
    SpeedMonster(path, 1),
    HeavyMonster(path, 1),
    HeavyMonster(path, 1),
    ShieldMonster(path, 1),
    HeavyMonster(path, 1),
    ShieldMonster(path, 1),
]

game.add_monsters(monsters)


# ------- End Code Here -------

if __name__ == '__main__':
    game.start_game()
    pyglet.app.run()
