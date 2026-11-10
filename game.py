import pygame
import random

pygame.init()

# Dimensions of the screen
WIDTH, HEIGHT = 600, 500

# Colors (Tema Pink Bunny & Pastel Aesthetic)
BG_COLOR = (255, 240, 245)       # Pink pastel sangat lembut
PASTEL_PINK = (255, 182, 193)    # Pink kelinci
PASTEL_BLUE = (176, 224, 230)    # Powder Blue
PASTEL_GREEN = (152, 251, 152)   # Pale Green
PASTEL_PURPLE = (221, 160, 221)  # Plum / Ungu pastel
PASTEL_YELLOW = (255, 253, 208)  # Cream / Kuning pastel
WHITE = (255, 255, 255)
DARK_TEXT = (110, 70, 90)        # Warna teks cokelat keunguan yang manis
HEART_PINK = (255, 105, 180)     # Hot Pink untuk bola
SHADOW_PINK = (230, 130, 160)

font = pygame.font.Font('freesansbold.ttf', 15)
font_large = pygame.font.Font('freesansbold.ttf', 22)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pink Bunny Block Breaker")

# to control the frame rate
clock = pygame.time.Clock()
FPS = 30


