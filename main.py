"""write by: Amin"""
from ctypes import windll
from sys import modules
import pgzrun
import pygame
from pgzero.actor import Actor
# functions
# variables and initialize
WIDTH = 816
HEIGHT = 600
TITLE = "Mario Jumper 2023"
hwnd = pygame.display.get_wm_info()["window"]
windll.user32.MoveWindow(hwnd, 300, 50, WIDTH, HEIGHT, False)
mod = modules["__main__"]
# objects
lands = [Actor("land_green", (land * 64 + 32, HEIGHT - 32)) for land in range(WIDTH // 64 + 1)]
mario = Actor("p1", (50, HEIGHT - 91))
# main loop functions
def draw():
    """draw everything in game here."""
    mod.screen.blit("sky2", (0, 0))
    for land_item in lands:land_item.draw()
    mario.draw()
pgzrun.go()
