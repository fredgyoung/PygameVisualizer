import pygame, sys
from pygame.locals import *
from random import randint
import pygbutton

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
GREY = (192, 192, 192)

# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((1250, 600))
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

class Button(pygame.Rect):
    """
    The Rect object has several virtual attributes which can be used to move and align the Rect:
    x,y
    top, left, bottom, right
    topleft, bottomleft, topright, bottomright
    midtop, midleft, midbottom, midright
    center, centerx, centery
    size, width, height
    w,h
    """
    def __init__(self, x, y, width, height, text):
        super().__init__(x, y, width, height)
        self.text = text




class Window:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.size = self.right - self.left + 1

    def draw(self, surface):
        surface.fill(GREY)
        x = self.left * 100 + 90
        y = 390
        width = (self.right - self.left + 1) * 100
        height = 100
        pygame.draw.rect(surface, WHITE, (x, y, width, height))
        pygame.draw.rect(surface, BLACK, (x, y, width, height), 1)

    def expand_left(self):
        if self.left > 0:
            self.left -= 1

    def expand_right(self):
        if self.right < 9:
            self.right += 1

    def shrink_left(self):
        if self.right - self.left > 0:
            self.left += 1

    def shrink_right(self):
        if self.right - self.left > 0:
            self.right -= 1

    def shift_left(self):
        if self.left > 0:
            self.left -= 1
            self.right -= 1

    def shift_right(self):
        if self.right < 9:
            self.left += 1
            self.right += 1


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

window = Window(3, 5)

expand_left_button = pygbutton.PygButton((50, 50, 150, 30), 'expand_left')
shrink_left_button = pygbutton.PygButton((250, 50, 150, 30), 'shrink_left')
expand_right_button = pygbutton.PygButton((450, 50, 150, 30), 'expand_right')
shrink_right_button = pygbutton.PygButton((650, 50, 150, 30), 'shrink_right')
shift_left_button = pygbutton.PygButton((850, 50, 150, 30), 'shift_left')
shift_right_button = pygbutton.PygButton((1050, 50, 150, 30), 'shift_right')

# Beginning Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if 'click' in expand_left_button.handleEvent(event):
            window.expand_left()
        if 'click' in expand_right_button.handleEvent(event):
            window.expand_right()
        if 'click' in shrink_left_button.handleEvent(event):
            window.shrink_left()
        if 'click' in shrink_right_button.handleEvent(event):
            window.shrink_right()
        if 'click' in shift_left_button.handleEvent(event):
            window.shift_left()
        if 'click' in shift_right_button.handleEvent(event):
            window.shift_right()

    #DISPLAYSURF.fill(WHITE)
    window.draw(DISPLAYSURF)
    #draw_grid()

    for card in cards:
        card.update()
        card.draw(DISPLAYSURF)

    expand_left_button.draw(DISPLAYSURF)
    expand_right_button.draw(DISPLAYSURF)
    shrink_left_button.draw(DISPLAYSURF)
    shrink_right_button.draw(DISPLAYSURF)
    shift_left_button.draw(DISPLAYSURF)
    shift_right_button.draw(DISPLAYSURF)

    pygame.display.update()

    FramePerSec.tick(FPS)



