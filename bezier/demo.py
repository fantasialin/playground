import pygame, sys
from pygame.locals import *
import random
import math
import numpy as np

#Number of frames per second
FPS = 2

screen_width = 800
screen_height = 600

# set up the colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARKGRAY = (40, 40, 40)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
orange = (245, 138, 66)
light_gray = (220, 220, 220)
light_blue = (66, 245, 224)
dark_gray = (100, 100, 100)

gridOriginX = 20
gridOriginY = 20
gridWidth = 20
gridHeight = 20


class draw_bezier:
    def __init__(self, surface, width, height, draw_width, draw_height, **kwargs):
        self.surface = surface
        self.width = width
        self.height = height
        self.draw_width = draw_width
        self.draw_height = draw_height
        self.visible = True
        self.isEnabled = True
        self.isPause = False
        self.x_offset = kwargs.get('x_offset', 0)
        self.y_offset = kwargs.get('y_offset', 0)
        self.win_area = pygame.Rect(0, 0, draw_width, draw_height)
        self.draw_area = pygame.Rect(self.x_offset, self.y_offset, draw_width+self.x_offset, draw_height+self.y_offset)
        self.image = pygame.Surface((draw_width, draw_height))
        self.quadratic_CPs = []
        self.quadratic_CPs.append((10,250))
        self.quadratic_CPs.append((200,50))
        self.quadratic_CPs.append((450,350))

        self.curve_1 = self.gen_quadratic(self.quadratic_CPs)

        self.test_CPs = []
        self.test_CPs.append((100,50))
        self.test_CPs.append((150,50))
        self.test_CPs.append((150,100))

        self.curve_2 = self.gen_quadratic(self.test_CPs)

        self.cubic_CPs = []
        self.cubic_CPs.append((10,300))
        self.cubic_CPs.append((50,150))
        self.cubic_CPs.append((300,150))
        self.cubic_CPs.append((450,400))

        self.curve_3 = self.gen_cubic(self.cubic_CPs)

    # destructor
    def __del__(self):
        pass

    def gen_quadratic(self, points):
        if len(points) < 3:
            return []
        # define Second-order bezier curve control point
        p0 = np.array(points[0])
        p1 = np.array(points[1])
        p2 = np.array(points[2])

        result = []

        # draw Second-order (quadratic) bezier curve
        for t in np.arange(0, 1, 0.01):
            b = (1 - t) ** 2 * p0 + 2 * (1 - t) * t * p1 + t ** 2 * p2
            result.append(b)

        return result

    def gen_cubic(self, points):
        if len(points) < 4:
            return []
        # define cubic bezier curve control point
        q0 = np.array(points[0])
        q1 = np.array(points[1])
        q2 = np.array(points[2])
        q3 = np.array(points[3])

        result = []

        # draw cubic bezier curve
        for t in np.arange(0, 1, 0.01):
            b = (1 - t) ** 3 * q0 + 3 * (1 - t) ** 2 * t * q1 + 3 * (1 - t) * t ** 2 * q2 + t ** 3 * q3
            result.append(b)

        return result


    def plot_bezier(self):

        for b in self.curve_1:
            pygame.draw.circle(self.image, (255, 0, 0), b.astype(int), 1)
        
        # draw control points
        pygame.draw.aalines(self.image, BLUE, False, self.quadratic_CPs, 1)
        for a in self.quadratic_CPs:
            pygame.draw.circle(self.image, (0, 0, 0), a, 3)

        for b in self.curve_2:
            pygame.draw.circle(self.image, (0, 255, 0), b.astype(int), 1)
        
        # draw control points
        pygame.draw.aalines(self.image, orange, False, self.test_CPs, 1)
        for a in self.test_CPs:
            pygame.draw.circle(self.image, (0, 0, 0), a, 3)

        for b in self.curve_3:
            pygame.draw.circle(self.image, (0, 0, 255), b.astype(int), 1)

        # draw control points
        pygame.draw.aalines(self.image, GREEN, False, self.cubic_CPs, 1)
        for a in self.cubic_CPs:
            pygame.draw.circle(self.image, (0, 0, 0), a, 3)

    
    def draw(self):
        # draw self
        self.image.fill((240,240,240))

        self.plot_bezier()

        # bitblt
        self.surface.blit(self.image, self.draw_area)

    def handleEvent(self, Event):
        if self.visible and self.isEnabled:
            pass

def main():
    pygame.init()
    pygame.display.set_caption('draw demo') 
    surface = pygame.display.set_mode((screen_width,screen_height)) 
    surface.fill(WHITE)
    fpsClock = pygame.time.Clock()

    offset = (screen_width - 500)/2

    afib = draw_bezier(surface, screen_width, screen_height, 500, 500,
                                x_offset=offset, y_offset=20, init_random_count=10, draw_single_color=True)

    # loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                afib.handleEvent(event)
            elif event.type == MOUSEMOTION:
                afib.handleEvent(event)

        afib.draw()

        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == '__main__':
    main()