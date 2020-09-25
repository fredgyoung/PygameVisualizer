import pygame, sys
from pygame.locals import *
from random import randint

# Initialize program
pygame.init()

# Assign FPS a value
FPS = 60
FramePerSec = pygame.time.Clock()

# Setting up color objects
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Example")

cards = []

def draw_grid():
    # Horizontal
    #pygame.draw.line(DISPLAYSURF, BLACK, (90, 390), (1090, 390), 1)
    pygame.draw.line(DISPLAYSURF, BLACK, (90, 490), (1090, 490), 1)
    # Vertical
    for x in range(90, 1190, 100):
        pygame.draw.line(DISPLAYSURF, BLACK, (x, 410), (x, 490), 1)


def swap_cards(i, j):
    cards[i].swap_position(cards[j].x)
    cards[j].swap_position(cards[i].x)

class Card():
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.width = 80
        self.height = 80
        self.value = value
        self.destinations = []

    def swap_position(self, position):
        self.destinations.append((self.x, self.y-200))
        self.destinations.append((position, self.y-200))
        self.destinations.append((position, self.y))

    def shift_right(self):
        self.destinations.append((self.x+100, self.y))

    def shift_left(self):
        self.destinations.append((self.x-100, self.y))

    def update(self):
        if self.destinations:
            dest_x, dest_y = self.destinations[0]
            if self.x < dest_x:
                self.x += 2
            elif self.x > dest_x:
                self.x -= 2
            if self.y < dest_y:
                self.y += 2
            elif self.y > dest_y:
                self.y -= 2
            if self.x == dest_x and self.y == dest_y:
                self.destinations.pop(0)

    def draw(self, surface):
        pygame.draw.rect(surface, BLACK, (self.x, self.y, self.width, self.height), 1)
        font = pygame.font.Font(None, 50)
        text = str(self.value)
        size = font.size(text)
        ren = font.render(text, 0, BLACK)
        surface.blit(ren, (self.x + 20, self.y + 20))

for x in range(10):
    card = Card(x*100+100, 400, randint(10, 99))
    cards.append(card)

# Beginning Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                for card in cards:
                    card.shift_right()
            if event.key == pygame.K_LEFT:
                for card in cards:
                    card.shift_left()
            if event.key == pygame.K_UP:
                swap_cards(1, 8)


    DISPLAYSURF.fill(WHITE)
    draw_grid()

    for card in cards:
        card.update()
        card.draw(DISPLAYSURF)

    pygame.display.update()

    FramePerSec.tick(FPS)


















