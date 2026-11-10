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


# Ball Class
class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx, self.posy = posx, posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xFac, self.yFac = 1, 1

        self.ball = pygame.draw.circle(
            screen, self.color, (int(self.posx), int(self.posy)), self.radius)

    def display(self):
        pygame.draw.circle(screen, SHADOW_PINK, (int(self.posx), int(self.posy)), self.radius + 3)
        self.ball = pygame.draw.circle(
            screen, HEART_PINK, (int(self.posx), int(self.posy)), self.radius)
        pygame.draw.circle(
            screen, WHITE, (int(self.posx) - 2, int(self.posy) - 2), 3)

    def update(self):
        self.posx += self.xFac*self.speed
        self.posy += self.yFac*self.speed

        if self.posx <= 0 or self.posx >= WIDTH:
            self.xFac *= -1

        if self.posy <= 0:
            self.yFac *= -1

        if self.posy >= HEIGHT:
            return True

        return False

    def reset(self):
        self.posx = WIDTH // 2
        self.posy = HEIGHT - 150
        self.xFac, self.yFac = 1, -1

    def hit(self):
        self.yFac *= -1

    def getRect(self):
        return self.ball


# Helper Functions

def collisionChecker(rect, ball):
    if pygame.Rect.colliderect(rect, ball):
        return True
    return False


def populateBlocks(blockWidth, blockHeight, horizontalGap, verticalGap):
    listOfBlocks = []
    pastel_palette = [PASTEL_PINK, PASTEL_BLUE, PASTEL_GREEN, PASTEL_PURPLE, PASTEL_YELLOW]

    for i in range(15, WIDTH - blockWidth, blockWidth+horizontalGap):
        for j in range(40, HEIGHT//2, blockHeight+verticalGap):
            listOfBlocks.append(
                Block(i, j, blockWidth, blockHeight, 
                      random.choice(pastel_palette)))

    return listOfBlocks


def gameOver():
    gameOver = True
    while gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True


# Game Manager
def main():
    running = True
    lives = 3
    score = 0

    striker = Striker(WIDTH//2 - 50, HEIGHT-50, 100, 20, 10, PASTEL_PINK)
    strikerXFac = 0

    ball = Ball(WIDTH//2, HEIGHT-150, 8, 5, HEART_PINK)

    blockWidth, blockHeight = 45, 15
    horizontalGap, verticalGap = 10, 10

    listOfBlocks = populateBlocks(
        blockWidth, blockHeight, horizontalGap, verticalGap)

    