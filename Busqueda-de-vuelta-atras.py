import pygame
import random

# Dimensiones de la ventana
WIDTH = 480
HEIGHT = 480

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Tamaño del tablero
BOARD_SIZE = 8

# Clase para representar el tablero
class Board:
    def __init__(self):
        self.board = [[0 for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
        self.queens = []

    # Método para colocar una reina en una posición aleatoria
    def place_queen(self):
        row = random.randint(0, BOARD_SIZE - 1)
        col = random.randint(0, BOARD_SIZE - 1)
        self.board[row][col] = 1
        self.queens.append((row, col))

    # Función para resolver el problema de las 6 reinas usando la búsqueda de vuelta atrás
    def backtrack_search(self, num_queens, last_queen):
        if num_queens == 6:
            return True

        # Buscar una posición válida para la siguiente reina
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if (row, col) in self.queens:
                    continue

                # Comprobar si la posición es válida
                valid = True
                for queen in self.queens:
                    if row == queen[0] or col == queen[1] or abs(row - queen[0]) == abs(col - queen[1]):
                        valid = False
                        break

                # Si la posición es válida, colocar la siguiente reina y continuar la búsqueda
                if valid:
                    self.board[row][col] = 1
                    self.queens.append((row, col))
                    if self.backtrack_search(num_queens + 1, (row, col)):
                        return True
                    else:
                        self.board[row][col] = 0
                        self.queens.remove((row, col))

        # Si no se puede colocar la siguiente reina en ninguna posición válida, volver atrás
        return False

    # Método para dibujar el tablero y las reinas
    def draw(self, screen):
        square_size = HEIGHT // BOARD_SIZE
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                x = col * square_size
                y = row * square_size
                color = WHITE if (row + col) % 2 == 0 else BLACK
                pygame.draw.rect(screen, color, [x, y, square_size, square_size])
                if self.board[row][col] == 1:
                    pygame.draw.circle(screen, RED, (x + square_size // 2, y + square_size // 2), square_size // 2 - 10)

# Función principal
def main():
    # Inicializar Pygame
    pygame.init()

    # Crear la ventana
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tablero de Ajedrez con 6 reinas")

    # Crear el tablero
    board = Board()
    print("dasdasd")

    # Resolver el problema de las 6 reinas
    board.backtrack_search(0, (-1, -1))

    # Ciclo principal del juego
    running = True
    while running:
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Salir del ciclo principal y terminar el programa

        # Dibujar el tablero y las reinas en la pantalla
        board.draw(screen)
        pygame.display.flip()

# Llamar a la función principal
if __name__ == "__main__":
    main()