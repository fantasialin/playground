import pygame, sys
from pygame.locals import *
import random
import math
from fib_iter import fib as fib_iter


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


class draw_fib:
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
        self.factor = 10
        self.fib = None
        self.spiral_x = int(draw_width/2)
        self.spiral_y = int(draw_height/2)
        self.dot_radius = 3
        self.max_fib = 16
        self.count = 0
        self.drawonce = 0
        self.start = 4

        # generate the first n fibonacci numbers
        if None == self.fib:
            self.fib = self.fib_sequence(self.max_fib)

    # destructor
    def __del__(self):
        pass

    def fib_sequence(self, nums):
        result = []
        for i in range(nums+1):
            result.append(fib_iter(i))
        print(f'fib sequence to fib({nums+1}), {result}')
        return result

    # ref. https://github.com/applepiinc/arithmaticthinking/tree/main/Day%201%20Adventure%20Source%20Code
    def plot_spiral(self, nums):

        # draw spiral for the first 10 squares
        start_x = self.spiral_x
        start_y = self.spiral_y
        self.start -= 1
        if self.start <= 0:
            self.start = 4
        arc_width = 1
        idx = self.start%4 
        # 0 to n+1 because end index is exclusive
        for i in range(1, nums+1, 1): 
            #print(self.fib[i])
            ##pygame.draw.circle(self.image, (137,207,240), [start_x, start_y], 2, 0) 
                            
            #bottom right start
            tmp_color = orange
            if (idx%4 == 1):
                curr_x = start_x - self.fib[i]
                curr_y = start_y - self.fib[i]
                tmp_color = light_gray

            #top right start
            elif (idx%4 == 2):
                curr_x = start_x - self.fib[i]
                curr_y = start_y
                tmp_color = light_blue

            #top left start
            elif (idx%4 == 3):
                curr_x = start_x
                curr_y = start_y
                tmp_color = dark_gray

            # bottom left start
            else:
                curr_x = start_x
                curr_y = start_y - self.fib[i]

            tmp_rect = pygame.Rect(curr_x, curr_y, self.fib[i], self.fib[i])
            print(f'({i}) -> (x,y)={curr_x},{curr_y}, (start x, y)={start_x},{start_y} w,h {self.fib[i]}')
            rect = pygame.draw.rect(self.image, tmp_color, tmp_rect)
            #rect = pygame.draw.rect(self.image, light_gray, tmp_rect, 1)

            # center of the quadrant
            arc_x = 0
            arc_y = 0

            #bottom right start
            if (idx%4 == 1):
                arc_x = start_x - 2 * self.fib[i]
                arc_y = start_y - self.fib[i]
                pygame.draw.arc(self.image, RED, [arc_x, arc_y, 2 * self.fib[i], 2 * self.fib[i]], 0, math.pi/2, arc_width)

            
                start_x = start_x - self.fib[i]
                start_y = start_y - self.fib[i]

            #top right start
            elif (idx%4 == 2):
                arc_x = start_x - self.fib[i]
                arc_y = start_y
                pygame.draw.arc(self.image, RED, [arc_x, arc_y, 2 * self.fib[i], 2 * self.fib[i]], math.pi/2, math.pi, arc_width)

                start_x = start_x - self.fib[i]
                start_y = start_y + self.fib[i]

            #top left start
            elif (idx%4 == 3):
                arc_x = start_x
                arc_y = start_y - self.fib[i]
                pygame.draw.arc(self.image, RED, [arc_x, arc_y, 2 * self.fib[i], 2 * self.fib[i]], math.pi, math.pi*3/2, arc_width)

                start_x = start_x + self.fib[i]
                start_y = start_y + self.fib[i]

            # bottom left start
            else:
                arc_x = start_x - self.fib[i]
                arc_y = start_y - 2 * self.fib[i]
                pygame.draw.arc(self.image, RED, [arc_x, arc_y, 2 * self.fib[i], 2 * self.fib[i]], math.pi*3/2, math.pi*2, arc_width)

                start_x = start_x + self.fib[i]
                start_y = start_y - self.fib[i] 

            idx += 1
            ##pygame.draw.circle(self.image, (137,207,240), [start_x, start_y], 2, 0)
    
    def draw(self):
        # draw self
        if self.drawonce == 0:
            self.image.fill((240,240,240))

        if self.count < self.max_fib:
            self.count += 1
        else:
            self.count = 0

        self.plot_spiral(self.max_fib)

        #if self.drawonce == 0:
        #    self.plot_spiral(self.max_fib)
        #    self.drawonce = 1

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

    afib = draw_fib(surface, screen_width, screen_height, 500, 500,
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