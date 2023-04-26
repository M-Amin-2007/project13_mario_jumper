"""write by: Amin"""
from ctypes import windll
from random import choice, randint
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
speed = 5
# objects
lands = [Actor("land_green", (land * 64 + 32, HEIGHT - 32)) for land in range(WIDTH // 64 + 2)]
mario = Actor("p1", (50, HEIGHT - 91))
obstacles = []
for obs in range(4):
    obstacle = Actor(choice(["obj1", "obj2", "obj3"]))
    obstacle.midbottom = (obs * 400 + 500, HEIGHT - 64)
    obstacles.append(obstacle)
# main loop functions
def draw():
    """draw everything in game here."""
    mod.screen.blit("sky2", (0, 0))
    for land_item in lands: land_item.draw()
    mario.draw()
    for obstacle_item in obstacles: obstacle_item.draw()
def update():
    """update every thing in every frame."""
    # move
    for land_item in lands: land_item.x -= speed
    for obstacle_item in obstacles: obstacle_item.x -= speed
    # objects_loop
    for obstacle_item in obstacles:
        if obstacle_item.x < -obstacle_item.width // 2:
            obstacle_item.image = choice(["obj1", "obj2", "obj3"])
            new_x = obstacles[obstacles.index(obstacle_item) - 1].x +\
                    randint(int(160 * speed ** 0.5), int(210 * speed ** 0.5))
            obstacle_item.bottomleft = (new_x, HEIGHT - 64)
    for land_item in lands:
        if land_item.x < - land_item.width // 2:
            last_land = lands[lands.index(land_item) - 1]
            land_item.x = last_land.x + 64
pgzrun.go()
