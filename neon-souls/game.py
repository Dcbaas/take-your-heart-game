#!/usr/bin/env python3

import pygame
import sys
sys.path.append('../')
import league
from background import Background
from player import Player

"""
Copied and modified from example.
"""
def init_map(engine, p):
    """Create map and background"""
    league.Settings.tile_size = 16
    league.Settings.fill_color = (31, 38, 84)
    sprites = league.Spritesheet('./assets/tileset-collapsed.png', league.Settings.tile_size, 14)
    level1 = league.Tilemap('./assets/level1.lvl', sprites, layer = 1)
    world_size = (level1.wide*league.Settings.tile_size, level1.high*league.Settings.tile_size)
    engine.drawables.add(level1.passable.sprites()) 
    background = Background('./assets/near-buildings-bg.png')
    engine.drawables.add(background) 
    p.world_size = world_size
    p.rect = p.image.get_rect()
    engine.objects.append(p)
    engine.drawables.add(p)





def main():
    e = league.Engine("Neon Souls")
    
    e.init_pygame()

    p = Player(2,300,450)

    # create background and level
    init_map(e, p)

    pygame.time.set_timer(pygame.USEREVENT + 1, 1000 // league.Settings.gameTimeFactor)
    e.key_events[pygame.K_a] = p.move_left
    e.key_events[pygame.K_d] = p.move_right
    e.key_events[pygame.K_w] = p.move_up
    e.key_events[pygame.K_s] = p.move_down
    e.events[pygame.QUIT] = e.stop
    e.run()

if __name__=='__main__':
    main()
