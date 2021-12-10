import pygame
from pygame.locals import QUIT
import time
import sys

# 1 2 3
# 8 0 4
# 7 6 5 <-- 0 is empty

# (x= 0, y= 0) --> 1
# (x= 0, y= 1) --> 2
# (x= 0, y= 2) --> 3
# (x= 1, y= 0) --> 8
# (x= 1, y= 1) --> 0
# (x= 1, y= 2) --> 4
# (x= 2, y= 0) --> 7
# (x= 2, y= 1) --> 6
# (x= 2, y= 3) --> 5

board = [[1, 2, 3], 
        [8, 0, 4], 
        [7, 6, 5]]
        

pygame.init()
SURFACE = pygame.display.set_mode((384, 384))
FPSCLOCK = pygame.time.Clock()

def main():
    tile_1 = pygame.image.load("./nums/1.png")
    tile_1 = pygame.transform.scale(tile_1, (128, 128))

    tile_2 = pygame.image.load("./nums/2.png")
    tile_2 = pygame.transform.scale(tile_2, (128, 128))

    tile_3 = pygame.image.load("./nums/3.png")
    tile_3 = pygame.transform.scale(tile_3, (128, 128))

    tile_4 = pygame.image.load("./nums/4.png")
    tile_4 = pygame.transform.scale(tile_4, (128, 128))

    tile_5 = pygame.image.load("./nums/5.png")
    tile_5 = pygame.transform.scale(tile_5, (128, 128))

    tile_6 = pygame.image.load("./nums/6.png")
    tile_6 = pygame.transform.scale(tile_6, (128, 128))

    tile_7 = pygame.image.load("./nums/7.png")
    tile_7 = pygame.transform.scale(tile_7, (128, 128))

    tile_8 = pygame.image.load("./nums/8.png")
    tile_8 = pygame.transform.scale(tile_8, (128, 128))

    tile_0 = pygame.image.load("./nums/0.png")
    tile_0 = pygame.transform.scale(tile_0, (128, 128))

    tiles = [[tile_1, tile_2, tile_3],
            [tile_8, tile_0, tile_4],
            [tile_7, tile_6, tile_5]]

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    for i in range(3):
                        for j in range(3):
                            if board[i][j] == 0:
                                ii = i
                                jj = j
                    if jj != 0:
                        board[ii][jj] = board[ii][jj - 1]
                        board[ii][jj - 1] = 0
                        tiles[ii][jj] = tiles[ii][jj - 1]
                        tiles[ii][jj - 1] = tile_0

                elif event.key == pygame.K_LEFT:
                    for i in range(3):
                        for j in range(3):
                            if board[i][j] == 0:
                                ii = i
                                jj = j
                    if jj != 2:
                        board[ii][jj] = board[ii][jj + 1]
                        board[ii][jj + 1] = 0
                        tiles[ii][jj] = tiles[ii][jj + 1]
                        tiles[ii][jj + 1] = tile_0

                elif event.key == pygame.K_UP:
                    for i in range(3):
                        for j in range(3):
                            if board[i][j] == 0:
                                ii = i
                                jj = j
                    if ii != 2:
                        board[ii][jj] = board[ii + 1][jj]
                        board[ii + 1][jj] = 0
                        tiles[ii][jj] = tiles[ii + 1][jj]
                        tiles[ii + 1][jj] = tile_0

                elif event.key == pygame.K_DOWN:
                    for i in range(3):
                        for j in range(3):
                            if board[i][j] == 0:
                                ii = i
                                jj = j
                    if ii != 0:
                        board[ii][jj] = board[ii - 1][jj]
                        board[ii - 1][jj] = 0
                        tiles[ii][jj] = tiles[ii - 1][jj]
                        tiles[ii - 1][jj] = tile_0

        SURFACE.fill((18, 55, 85))
        for i in range(3):
            for j in range(3):
                SURFACE.blit(tiles[i][j], (j*128, i*128))

        pygame.display.update()

if __name__ == '__main__':
    main()



                        





