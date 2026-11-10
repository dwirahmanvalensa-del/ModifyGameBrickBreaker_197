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


# Striker class (Karakter Kelinci dengan Telinga Panjang)
class Striker:
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx, self.posy = posx, posy
        self.width, self.height = width, height
        self.speed = speed
        self.color = color

        self.strikerRect = pygame.Rect(
            self.posx, self.posy, self.width, self.height)

    def display(self):
        # Badan kelinci (papan pemukul)
        self.striker = pygame.draw.rect(screen, PASTEL_PINK, self.strikerRect, border_radius=10)
        pygame.draw.rect(screen, WHITE, self.strikerRect, 2, border_radius=10)
        
        # Telinga kelinci di atas badan
        ear_width, ear_height = 14, 30
        ear1_x = self.posx + 20
        ear2_x = self.posx + self.width - 34
        ear_y = self.posy - ear_height
        
        pygame.draw.ellipse(screen, PASTEL_PINK, (ear1_x, ear_y, ear_width, ear_height))
        pygame.draw.ellipse(screen, WHITE, (ear1_x + 3, ear_y + 5, ear_width - 6, ear_height - 10))
        
        pygame.draw.ellipse(screen, PASTEL_PINK, (ear2_x, ear_y, ear_width, ear_height))
        pygame.draw.ellipse(screen, WHITE, (ear2_x + 3, ear_y + 5, ear_width - 6, ear_height - 10))

    def update(self, xFac):
        self.posx += self.speed*xFac

        if self.posx <= 0:
            self.posx = 0
        elif self.posx+self.width >= WIDTH:
            self.posx = WIDTH-self.width

        self.strikerRect = pygame.Rect(
            self.posx, self.posy, self.width, self.height)

    def getRect(self):
        return self.strikerRect


# Block Class
class Block:
    def __init__(self, posx, posy, width, height, color):
        self.posx, self.posy = posx, posy
        self.width, self.height = width, height
        self.color = color
        self.damage = 100

        if color in [PASTEL_PURPLE, PASTEL_BLUE]:
            self.health = 200
        else:
            self.health = 100

        self.blockRect = pygame.Rect(
            self.posx, self.posy, self.width, self.height)

    def display(self):
        if self.health > 0:
            self.brick = pygame.draw.rect(screen, self.color, self.blockRect, border_radius=6)
            pygame.draw.rect(screen, WHITE, self.blockRect, 2, border_radius=6)

    def hit(self):
        self.health -= self.damage

    def getRect(self):
        return self.blockRect

    def getHealth(self):
        return self.health


