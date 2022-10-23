import string

import pygame
import random
from pygame import event

def asknumber():
    global n
    k = 0
    while k < 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    n = 1
                    k = 1
                elif event.key == pygame.K_2:
                    n = 2
                    k = 1
                elif event.key == pygame.K_3:
                    n = 3
                    k = 1
                elif event.key == pygame.K_4:
                    n = 4
                    k = 1
                elif event.key == pygame.K_5:
                    n = 5
                    k = 1
                elif event.key == pygame.K_6:
                    n = 6
                    k = 1
                elif event.key == pygame.K_7:
                    n = 7
                    k = 1
                elif event.key == pygame.K_8:
                    n = 8
                    k = 1
                elif event.key == pygame.K_9:
                    n = 9
                    k = 1

    return n

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
colors = [RED, GREEN, BLUE]
def genlet(length):
    letters = string.ascii_lowercase
    rand_let = ''.join(random.choice(letters) for i in range (length))
    return rand_let

io = pygame.Surface((2932,30))
q = []
q.append(io)
print(io)


class Button():
    def __init__(self, W, H, dx, dy, image1, image2, name_rect):

        self.image1 = image1
        self.W = W
        self.H = H
        self.dy = dy
        self.dx = dx
        self.image2 = image2
        self.name_rect = name_rect

    def draw(self, sc):
        pos = pygame.mouse.get_pos()
        if self.name_rect.collidepoint(pos):
            sc.blit(self.image2, (self.W // 3 + self.dx, self.H // 3 + self.dy))

        sc.blit(self.image1, (self.W // 3 + self.dx, self.H // 3 + self.dy))

def in_names():
    in_1_str = 0
    in_2_str = 0
    in_3_str = 0
    in_4_str = 0
    in_5_str = 0
    in_6_str = 0
    in_7_str = 0
    in_8_str = 0
    in_9_str = 0

    in_1_stb = 0
    in_2_stb = 0
    in_3_stb = 0
    in_4_stb = 0
    in_5_stb = 0
    in_6_stb = 0
    in_7_stb = 0
    in_8_stb = 0
    in_9_stb = 0

    in_names_str = [in_1_str, in_2_str, in_3_str, in_4_str, in_5_str, in_6_str, in_7_str, in_8_str, in_9_str ]
    in_names_stb = [in_1_stb, in_2_stb, in_3_stb, in_4_stb, in_5_stb, in_6_stb, in_7_stb, in_8_stb, in_9_stb]




class Counting_and_Printing():
    def __init__(self, horiz, vert, all, int_nt, int_nw, in_names_str, in_names_stb, number_str):
        self.number_str = number_str
        self.in_names_str = in_names_str
        self.in_names_stb = in_names_stb
        self.int_nt = int_nt
        self.int_nw = int_nw
        self.horiz = horiz
        self.vert = vert
        self.all = all


    def Counting(self):
        q = []
        # for i in self.horiz[self.number_str]:
        #     for j in range (0, self.int_nw):
        #         if self.horiz[self.number_str][j] == (0, 0, 0, 255):
        #             self.in_names_str[self.number_str] += 1
        # self.in_names_str[self.number_str] -= self.int_nw - 1

        x = self.horiz[self.number_str].count((0, 0, 0, 255))

        if self.all == 0:
            self.all += 1
        print('in 1st string:', self.in_names_str[self.number_str])
        print("% of power spent on first task:", float(self.in_names_str[self.number_str]/self.all*100), "%")
        self.in_names_str[self.number_str] = 0
        print("aaaaaaa", x)
        giving = float(x / self.all * 100)
        giving_ready = float('{:.3f}'.format(giving))

        return giving_ready



    def Counting_vert(self):
        x = self.vert[self.number_str].count((0, 0, 0, 255))

        if self.all == 0:
            self.all += 1
        print('in 1st string:', self.in_names_str[self.number_str])
        print("% of power spent on first task:", float(self.in_names_str[self.number_str]/self.all*100), "%")
        self.in_names_str[self.number_str] = 0
        print("aaaaaaa", x)
        giving = float(x / self.all * 100)
        giving_ready = int('{:.0f}'.format(giving))

        return giving_ready









