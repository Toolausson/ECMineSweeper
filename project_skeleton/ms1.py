import pygame
import sys
import random
from cell_ms import Cell
from calcs import measure_distance

pygame.init()

SCREEN_MIN_SIZE = 750  # Can be made to autoadjust after % of ur screen
amount_of_cells = 16  # The amount of cells is equal in rows and columns, 16x16 (LOCKED)
bomb_chance = 0.2  # Change to prefered value or use default 0.25

CELL_SIZE = SCREEN_MIN_SIZE // amount_of_cells
READJUSTED_SIZE = CELL_SIZE * amount_of_cells

SCREEN_WIDTH, SCREEN_HEIGHT = READJUSTED_SIZE, READJUSTED_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("MineSweeper")

cells = []
bomb_count = 0  #kolla antal bomber 
cells_shown = 0 #visa antal öppnade celler, if cells_shown + bomb_count = amount_of_cells ** 2 ->tjoohoo.




def create_cells():
    x_pos = y_pos = 0
    for _ in range(amount_of_cells):
        row = []
        for _ in range(amount_of_cells):
            cell = Cell(x_pos, y_pos, CELL_SIZE, CELL_SIZE, bomb_chance)
            x_pos += CELL_SIZE
            row.append(cell)
        x_pos = 0
        y_pos += CELL_SIZE
        cells.append(row)



def count_neighbouring_bombs(rowcell, colcell):
    for ri in range(-1, 2):
        for ci in range(-1, 2):
            rpos = rowcell + ri
            cpos = colcell + ci

            if ((rpos > -1 and rpos < amount_of_cells) and (cpos > -1 and cpos < amount_of_cells) and
                    (rpos != rowcell or cpos != colcell)):
                cell = cells[rpos][cpos]
                if cell.bomb:
                    cells[rowcell][colcell].neighbouring_bombs += 1


def draw_cells():
    for cell_row in cells:
        for cell in cell_row:
            cell.draw(screen)


def show_cell(x, y):
    cell_row = y // CELL_SIZE
    cell_col = x // CELL_SIZE

    if 0 <= cell_row < amount_of_cells and 0 <= cell_col < amount_of_cells:
        cell = cells[cell_row][cell_col]
        cell.show()
        if cell.neighbouring_bombs == 0 and not cell.bomb:
            count_neighbouring_bombs(cell_row, cell_col)
        elif cell.bomb:
            pygame.display.set_caption("MineSweeper - DU HAR FÖRLORAT, Ut å lek!")


#def print_obj_properties():
#    for i in range(len(cells)):
#        for j in range(len(cells[i])):
#            cell = cells[i][j]
#            print(f"Cell ({i}, {j}) - Bomb?: {cell.bomb}, Gömd: {cell.hidden}, Grannbomber: {cell.neighbouring_bombs}")


def event_handler(event):
    if event.type == pygame.QUIT:
        terminate_program()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        show_cell(mouse_x, mouse_y)
        #print_obj_properties()


def run_setup():
    create_cells()
    screen.fill((24, 128, 192))
    for i in range(amount_of_cells):
        for j in range(amount_of_cells):
            count_neighbouring_bombs(i, j)
    #print_obj_properties()


def terminate_program():
    pygame.quit()
    sys.exit()


def main():
    run_setup()

    while True:
        for event in pygame.event.get():
            event_handler(event)

        screen.fill((24, 128, 192))
        draw_cells()

        pygame.display.flip()


if __name__ == "__main__":
    main()
