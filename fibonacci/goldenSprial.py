import pygame, sys
from pygame.locals import *
import random
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

#Number of frames per second
FPS = 10

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


class draw_goldenSprial:
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
        self.angle = 0

    # destructor
    def __del__(self):
        pass

    def plot_golden_spiral(self, num_points, angle):
        # generate angles (radians) 4xPi (a circle)
        theta = np.linspace(0, 4 * np.pi, num_points)
        
        # generate radius
        radius = np.exp(0.30635 * theta)
        #print(f'radius {len(radius)}')
        
        # translate Polar coordination to Cartesian coordinate
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)

        fig, ax = plt.subplots()
        
        # draw golden sprial
        ax.plot(x, y)
        canvas = FigureCanvas(fig)
        plt.close()
        canvas.draw()

        # get canvas pixel data
        buffer = canvas.buffer_rgba()
        image_data = pygame.image.fromstring(buffer.tobytes(), buffer.shape[1::-1], "RGBA")

        #print(f' shape >> {image_data.get_rect()}')
        #print(f' surface >> {self.image.get_rect()}')
        pygame.surfarray.blit_array(self.image, pygame.surfarray.pixels3d(image_data))


    def draw(self):
        # draw self
        self.image.fill((240,240,240))

        # 绘制黄金螺旋，指定点的数量
        if self.angle < 20:
            self.angle += 1
        else:
            self.angle = 1
        self.plot_golden_spiral(1000, self.angle)

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

    offset = (screen_width - 640)/2

    aSprial = draw_goldenSprial(surface, screen_width, screen_height, 640, 480,
                                x_offset=offset, y_offset=20, init_random_count=10, draw_single_color=True)

    # loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                aSprial.handleEvent(event)
            elif event.type == MOUSEMOTION:
                aSprial.handleEvent(event)

        aSprial.draw()

        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == '__main__':
    main()