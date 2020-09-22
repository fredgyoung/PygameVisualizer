import pygame, sys
from pygame.locals import *

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

class Card():
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.width = 80
        self.height = 80
        self.value = value
        self.destinations = []

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

        # load font, prepare values
        font = pygame.font.Font(None, 50)
        text = str(self.value)
        size = font.size(text)

        # no AA, no transparancy, normal
        ren = font.render(text, 0, BLACK)
        surface.blit(ren, (self.x + 30, self.y + 20))

'''
def move_card(index, destination_x, destination_y):
    if cards[index].x < destination_x: cards[index].x += 1
    elif cards[index].x > destination_x: cards[index].x -= 1
    if cards[index].y < destination_y: cards[index].y += 1
    elif cards[index].y > destination_y: cards[index].y -= 1
'''

for x in range(10):
    card = Card(x*100+100, 400, x)
    cards.append(card)

cards[8].value = 1
cards[1].value = 8

cards[8].destinations.extend([(900, 200), (200, 200), (200, 400)])
cards[1].destinations.extend([(200, 200), (900, 200), (900, 400)])

# Beginning Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(WHITE)

    for card in cards:
        card.update()
        card.draw(DISPLAYSURF)

    #move_card(8, 900, 200)
    pygame.display.update()

    FramePerSec.tick(FPS)


















