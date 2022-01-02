import pygame
from pygame.locals import QUIT
import time
import sys
import copy

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


# create a copy of the initial board as it is the final state wanted, and the var board is going to be changed accordingly to movements and so on       
goal_board = copy.deepcopy(board) 


pygame.init()
SURFACE = pygame.display.set_mode((384, 384))
FPSCLOCK = pygame.time.Clock()

# Heuristic calc function
def calc_heuristic(grid, goal_grid):
    nbr = 0
    for i in range(3):
        for j in range(3):
            if grid[i][j] != goal_grid[i][j]:
                nbr += 1
    return nbr
# Get position from the matrix (board)
def position(elem, matrix):
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == elem :
                return (i, j)
            
# Get respect neighbors of a cell
def neighbors(cell):
    neighbors = []
    dRow = [ -1, 0, 1, 0]
    dCol = [ 0, 1, 0, -1]
    for i in range(4):
        adjx = cell[0] + dRow[i]
        adjy = cell[1] + dCol[i]
        neighbors.append((adjx, adjy))
    return neighbors

# check if a cell is valid (within grid)
def is_valid(cell):
    if cell[0] < 0 or cell[0] > 2 or cell[1] < 0 or cell[1] > 2 :
        return False
    else:
        return True

# move the current cell to the potential next cell in the list of next cells to calculate the heuristic for each one of the pot moves
def move (tile, swap_pos, board):
    pos0 = position(tile, board)
    board[pos0[0]][pos0[1]] = board[swap_pos[0]][swap_pos[1]]
    board[swap_pos[0]][swap_pos[1]] = 0
    
def exist_in_list(cell, queue_elem):
    for i in queue_elem:
        if i[2] == cell:
            return True
        else:
            return False

def get_min(open):
    min = open[0][0]
    elem = ""
    for i in open:
        if i[0] <= min :
            min = i[0]
            elem = i
    return elem


def main():
# creating the grid and respective tiles
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
# possibility to quit if wished (clicked close window)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
# generate mouvements and possibility to pply A* to a given grid
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
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
                
                elif event.key == pygame.K_KP_ENTER:

                    tiles = [[tile_1, tile_8, tile_2],
                             [tile_0, tile_4, tile_3],
                             [tile_7, tile_6, tile_5]]
                    board_m = [[1, 8, 2], 
                             [0, 4, 3], 
                             [7, 6, 5]]
                    board_u = [[1, 8, 2], 
                             [0, 4, 3], 
                             [7, 6, 5]]

                    # Apply A* here
                    
                    open = []
                    closed = []
                    h = calc_heuristic(board_m, goal_board)
                    f = h + 1
                    # we start executing at the position of the empty tile (0)
                    s = ((f, h, position(0, board_m)))
                    open.append(s)
                    solved = False
                    while open and not solved:
                        # sort the open list to have smaller fs first
                        curr_cell = get_min(open)
                        if curr_cell in closed:
                            break
                        else:
                            next_cells = neighbors(curr_cell[2])
                            for cell in next_cells:
                                if is_valid(cell):
                                    board_m = copy.deepcopy(board_u)
                                    curr_cell = cell
                                    move(0, curr_cell, board_m)
                                    h = calc_heuristic(board_m, goal_board)
                                    f = h + 1
                                    if exist_in_list(cell, open):
                                        if cell[1] > h:
                                            open.append((f, h, cell))
                                        else :
                                            break
                                    open.append((f, h, cell))
                            elem = open.pop(0)
                            closed.append(elem)
                            move(0, elem[2], board_u)
                            if board_u == goal_board:
                                solved = True
                    print(closed)

                    # visualize the solution
       


                    
        SURFACE.fill((18, 55, 85))
        for i in range(3):
            for j in range(3):
                SURFACE.blit(tiles[i][j], (j*128, i*128))

    
        pygame.display.update()

if __name__ == '__main__':
    main()



                        




