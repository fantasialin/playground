import pygame, sys
from pygame.locals import *
import random
import math
import numpy as np
from scipy.interpolate import splprep, splev

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


class funcBottons:
    def __init__(self, owner, surface, position=(0,0), width=100, height=40, **kwargs):
        self.surface = surface
        self.startX = position[0]
        self.startY = position[1]
        self.Width = width
        self.Height = height
        self.owner = owner
        self.visible = True
        self.isEnabled = True
        self.items = []
        self.dict = {}
        self.font = pygame.font.SysFont(None, 30)

    def draw(self):
        for a in self.items:
            pygame.draw.rect(self.surface, light_gray, a[1])
            pygame.draw.rect(self.surface, dark_gray, a[1], 2)
            text_surface = a[0]
            self.surface.blit(text_surface,text_surface.get_rect(center=a[1].center))

    def addButton(self, text_, callback):
        idx = len(self.items)
        text = self.font.render(text_, True, BLACK)
        rect = pygame.Rect(self.startX + (idx*(self.Width + 20)), self.startY, self.Width, self.Height)
        item = (text, rect, callback) # 0 -> text, 1 -> rect, 2 -> callback
        self.dict[text_] = item
        self.items.append(item)
    
    def handleEvent(self, Event):
        if Event.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN) or not self.visible:
            return False
        #print("pos>> ",self.text, " >> ",Event.pos)
        if self.visible and self.isEnabled:
            for item in self.items:
                if item[1].collidepoint(Event.pos):
                    item[2]() # callback

class draw_spline:
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

        self.button_child = funcBottons(self, surface, (20, self.draw_height + self.y_offset + 10), 120, 40)
        self.button_child.addButton("reset", self.reset)

        self.need_draw = True
        self.drag_node = False

        self.curves = []

        self.nodes = {}
        self.select_idx = -1

        self.random_CPs(5)

        

    # destructor
    def __del__(self):
        pass

    def random_CPs(self, count):
        self.curves = []
        self.nodes = {}
        CPs = []
        rect_CPs = []
        for i in range(count):
            x = random.randint(2,self.draw_width-2)
            y = random.randint(2,self.draw_height-2)
            print(f'<{i}> x,y = {x}, {y}')
            CPs.append((x,y))
            rect_CPs.append(pygame.Rect(x-2+self.x_offset, y-2+self.y_offset, 5, 5))
        
        self.nodes["point"] = CPs
        self.nodes["rect"] = rect_CPs

        self.curves.append((self.gen_spline(CPs, 100), CPs, RED))

    def update_CPs(self, CPs):
        self.curves = []
        self.curves.append((self.gen_spline(CPs, 100), CPs, RED))
        self.need_draw = True

    def reset(self):
        self.random_CPs(8)
        self.need_draw = True

    def gen_spline(self, points, step=1000):
        if len(points) < 4:
            return []
        
        result = []
        control_points = np.array(points)   

        # Compute the Spline Interpolation
        tck, u = splprep(control_points.T, s=0)
        u_new = np.linspace(0, 1, step)
        interpolated_points = np.array(splev(u_new, tck)).T
        for point in interpolated_points:
            result.append(point.astype(int))

        return result


    def plot_spline(self):

        for a in self.curves:
            # draw curve
            if False: # use dot to plot curve
                for b in a[0]:
                    pygame.draw.circle(self.image, a[2], b.astype(int), 1)
            else:
                pygame.draw.aalines(self.image, a[2], False, a[0], 1)

            if None != a[1]:
                # draw control points
                #pygame.draw.aalines(self.image, BLACK, False, a[1], 1)     
                for p in a[1]:
                    pygame.draw.circle(self.image, orange, p, 3)
   
    def draw_spline(self):
        if self.need_draw:
            self.image.fill((240,240,240))

            self.plot_spline()

            # bitblt
            self.surface.blit(self.image, self.draw_area)
            self.need_draw = False

    def draw(self):
        # draw self
        self.draw_spline()
        self.button_child.draw()

    def handleEvent(self, Event):
        if self.visible and self.isEnabled:
            if Event.type == MOUSEBUTTONDOWN:
                self.button_child.handleEvent(Event)
                print(f'pos = {Event.pos}')
                if len(self.nodes) > 0:
                    idx = 0
                    self.select_idx = -1
                    for a in self.nodes["rect"]:
                        if a.collidepoint(Event.pos):
                            self.drag_node = True
                            #print(f'select idx = {idx}')
                            self.select_idx = idx
                            break
                        idx += 1
                        
            elif Event.type == MOUSEBUTTONUP:
                print(f'mouse up')
                if len(self.nodes) > 0:
                    if len(self.nodes["point"]) > self.select_idx and self.select_idx >= 0:
                        point = self.nodes["point"][self.select_idx]
                        self.nodes["rect"][self.select_idx] = pygame.Rect(point[0]-2+self.x_offset, point[1]-2+self.y_offset, 5, 5)
                        print(f'update rect')
                self.drag_node = False
                self.select_idx = -1
            elif Event.type == MOUSEMOTION:
                if self.drag_node:
                    mouse_x, mouse_y = Event.pos
                    point = (int(mouse_x-self.x_offset), int(mouse_y-self.y_offset))
                    print(f'mouse x,y = {point[0]}, {point[1]}')
                    if self.select_idx != -1:
                        CPs = self.nodes["point"]
                        if self.select_idx >=0 and self.select_idx < len(CPs):
                            CPs[self.select_idx] = point
                            self.update_CPs(CPs)
                            self.nodes["point"][self.select_idx] = point

def main():
    pygame.init()
    pygame.display.set_caption('draw demo') 
    surface = pygame.display.set_mode((screen_width,screen_height)) 
    surface.fill(WHITE)
    fpsClock = pygame.time.Clock()

    offset = (screen_width - 500)/2

    aspline = draw_spline(surface, screen_width, screen_height, 500, 500,
                                x_offset=offset, y_offset=20, init_random_count=10, draw_single_color=True)

    # loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                aspline.handleEvent(event)
            elif event.type == MOUSEBUTTONUP:
                aspline.handleEvent(event)
            elif event.type == MOUSEMOTION:
                aspline.handleEvent(event)

        aspline.draw()

        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == '__main__':
    main()