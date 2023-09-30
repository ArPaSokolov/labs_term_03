import pygame
from random import randint

def draw_triangle(A_x, A_y, B_x, B_y, C_x, C_y):
    pygame.init()

    win = pygame.display.set_mode((600, 600))

    pygame.display.set_caption("Serpinsky triangle")

    Triangle = [[A_x, A_y], [B_x, B_y], [C_x, C_y]]

    x = randint(0, 600)
    y = randint(0, 600)

    RUN = True
    while RUN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
        A = randint(0, 2)
        x = .5 * (x + Triangle[A][0])
        y = .5 * (y + Triangle[A][1])

        pygame.draw.line(win, (255, 255, 255), (x, y), (x, y), 1)
        pygame.display.update()

    pygame.quit()

print("Enter the coordinates of the three vertices.\nX and Y take values from 0 to 600.")
a_x, a_y = map(int, input("Enter X and Y for vertice A separated by a space: ").split())
b_x, b_y = map(int, input("Enter X and Y for vertice B separated by a space: ").split())
c_x, c_y = map(int, input("Enter X and Y for vertice C separated by a space: ").split())

draw_triangle(a_x, a_y, b_x, b_y, c_x, c_y)