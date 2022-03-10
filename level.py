import pygame
from setuptools.command.rotate import rotate

from settings import *
from tile import Tile


class Level:
    def __init__(self):
        # get surface / pegar a superfice
        self.display_surface = pygame.display.get_surface()
        # Setup sprites / definir os sprites
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # setup sprites
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y), [self.visible_sprites])

    def run(self):
        self.visible_sprites.draw(self.display_surface)