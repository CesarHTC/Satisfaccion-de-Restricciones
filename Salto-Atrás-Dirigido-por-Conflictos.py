import pygame

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la pantalla
WIDTH = 450
HEIGHT = 450
WINDOW_SIZE = (WIDTH, HEIGHT)

# Definir los colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLUE = (0, 0, 255)

# Definir el tamaño de las celdas
CELL_SIZE = WIDTH // 9

# Crear la ventana
window = pygame.display.set_mode(WINDOW_SIZE)

# Definir el sudoku
sudoku = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]

def draw_board():
    window.fill(WHITE)

    # Dibujar las líneas gruesas de las cuadrículas de 3x3
    for i in range(0, WIDTH, CELL_SIZE*3):
        pygame.draw.line(window, BLACK, (i, 0), (i, HEIGHT), 4)
        pygame.draw.line(window, BLACK, (0, i), (WIDTH, i), 4)

    for i in range(9):
        for j in range(9):
            value = sudoku[i][j]
            color = BLUE if value != 0 else BLACK  # si el valor es 0, el color es negro

            # Dibujar el número en la celda
            font = pygame.font.Font(None, 36)
            text = font.render(str(value), True, color)
            text_rect = text.get_rect()
            text_rect.center = (j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2)
            window.blit(text, text_rect)

            # Dibujar los bordes de la celda
            pygame.draw.rect(window, BLACK, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
           
    pygame.display.flip()


def is_valid(sudoku, row, col, num):
    # Verificar si el número ya está en la fila
    if num in sudoku[row]:
        return False
    
    # Verificar si el número ya está en la columna
    for i in range(9):
        if sudoku[i][col] == num:
            return False
    
    # Verificar si el número ya está en la subcuadrícula
    sub_row = (row // 3) * 3
    sub_col = (col // 3) * 3
    for i in range(sub_row, sub_row + 3):
        for j in range(sub_col, sub_col + 3):
            if sudoku[i][j] == num:
                return False
    
    # Si no se violan las reglas, el número se puede colocar en la celda
    return True

def solve_sudoku(sudoku):
    # Encontrar la siguiente celda vacía
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                row = i
                col = j
                break
        else:
            continue
        break
    
    # Si no hay celdas vacías, el sudoku está resuelto
    else:
        return True
    
    # Probar los números del 1 al 9 en la celda vacía
    for num in range(1, 10):
        # Verificar si el número se puede colocar en la celda
        if is_valid(sudoku, row, col, num):
            # Colocar el número en la celda
            sudoku[row][col] = num
            pygame.time.delay(1000)
            draw_board()
            # Intentar resolver el sudoku con el número colocado
            if solve_sudoku(sudoku):

                return True
            
            # Si no se puede resolver el sudoku con el número colocado,
            # retroceder y probar con un número diferente
            sudoku[row][col] = 0
    
# Si no se puede colocar ningún número en la celda vacía, el sudoku no tiene solución
    return False

solve_sudoku(sudoku)


# Iniciar el bucle principal

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Salir del programa
pygame.quit()
