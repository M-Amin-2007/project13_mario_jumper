"""write by: Amin"""
from ctypes import windll
import pgzrun
import pygame
# functions
# variables and initialize
WIDTH = 816
HEIGHT = 600
TITLE = "Mario Jumper 2023"
hwnd = pygame.display.get_wm_info()["window"]
windll.user32.MoveWindow(hwnd, 300, 50, WIDTH, HEIGHT, False)
# objects
# main loop functions
def draw():
    """draw everything in game here."""
    pass
pgzrun.go()
