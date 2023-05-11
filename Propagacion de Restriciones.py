import pygame
from pygame.locals import *
import sys
# Inicializar pygame
pygame.init()
pygame.font.init()

# Dimensiones de la ventana
WINDOW_SIZE = (450, 450)

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Tamaño de la cuadrícula del Sudoku
GRID_SIZE = 3

# Tamaño de cada celda de la cuadrícula
CELL_SIZE = WINDOW_SIZE[0] // GRID_SIZE

# Sudoku a resolver
sudoku = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
          [6, 8, 0, 0, 7, 0, 0, 9, 0],
          [1, 9, 0, 0, 0, 4, 5, 0, 0],
          [8, 2, 0, 1, 0, 0, 0, 4, 0],
          [0, 0, 4, 6, 0, 2, 9, 0, 0],
          [0, 5, 0, 0, 0, 3, 0, 2, 8],
          [0, 0, 9, 3, 0, 0, 0, 7, 4],
          [0, 4, 0, 0, 5, 0, 0, 3, 6],
          [7, 0, 3, 0, 1, 8, 0, 0, 0]]

# Inicializar pygame
# Crear la ventana
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku Solver")



# Función para dibujar el tablero
def draw_board():

    WIDTH = CELL_SIZE * GRID_SIZE
    HEIGHT = CELL_SIZE * GRID_SIZE
    window.fill(WHITE)

    for i in range(GRID_SIZE ** 2):
        for j in range(GRID_SIZE ** 2):
            value = sudoku[i][j]
            color = BLUE if value == 0 else BLACK

            # Dibujar el número en la celda
            font = pygame.font.Font(None, 36)
            text = font.render(str(value), True, color)
            text_rect = text.get_rect()
            text_rect.center = ((j * CELL_SIZE) + (CELL_SIZE // 2), (i * CELL_SIZE) + (CELL_SIZE // 2))
            window.blit(text, text_rect)

            # Dibujar los bordes de la celda
            pygame.draw.rect(window, BLACK, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

            # Dibujar las líneas más gruesas para separar las regiones 3x3
            if i % 3 == 0 and i != 0:
                pygame.draw.line(window, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 3)
            if j % 3 == 0 and j != 0:
                pygame.draw.line(window, BLACK, (j * CELL_SIZE, 0), (j * CELL_SIZE, HEIGHT), 3)

    pygame.display.flip()


def is_valid(row, col, num):
    # Verificar si el número ya está en la fila
    for i in range(GRID_SIZE ** 2):
        if sudoku[row][i] == num:
            return False

    # Verificar si el número ya está en la columna
    for j in range(GRID_SIZE ** 2):
        if sudoku[j][col] == num:
            return False

    # Verificar si el número ya está en el subcuadrado 3x3
    sub_square_row = (row // GRID_SIZE) * GRID_SIZE
    sub_square_col = (col // GRID_SIZE) * GRID_SIZE
    for i in range(sub_square_row, sub_square_row + GRID_SIZE):
        for j in range(sub_square_col, sub_square_col + GRID_SIZE):
            if sudoku[i][j] == num:
                return False

    # Si no hay conflictos, el número se puede colocar en la posición dada
    return True

# Función para resolver el Sudoku mediante propagación de restricciones
# Función para resolver el Sudoku mediante propagación de restricciones
def solve_sudoku():
    for row in range(GRID_SIZE ** 2):
        for col in range(GRID_SIZE ** 2):
            if sudoku[row][col] == 0:
                for num in range(1, GRID_SIZE ** 2 + 1):
                    if is_valid(row, col, num):
                        sudoku[row][col] = num
                        draw_board()
                        pygame.time.delay(300)
                        if solve_sudoku():
                            draw_board()
                            return True
                        sudoku[row][col] = 0
                return False
    return True


# Dibujar el tablero
draw_board()

# Iniciar el bucle principal
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    # Resolver el Sudoku
    solve_sudoku()

