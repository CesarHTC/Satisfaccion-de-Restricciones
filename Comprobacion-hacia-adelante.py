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
    def forward_checking_search(self, num_queens, last_queen):
        if num_queens == 6:
            return True

        # Buscar las posiciones disponibles para la siguiente reina
        available_positions = []
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

                # Si la posición es válida, añadirla a las posiciones disponibles
                if valid:
                    available_positions.append((row, col))

        # Para cada posición disponible, realizar la comprobación hacia delante
        for position in available_positions:
            # Realizar la comprobación hacia delante para la posición actual
            old_domains = {}
            for i in range(num_queens, 6):
                old_domains[i] = self.domains[i].copy()
                self.domains[i] = self.domains[i] - set(get_conflicts(position, i, self.queens))

            # Si algún dominio quedó vacío, volver atrás
            if any(len(domain) == 0 for domain in self.domains[num_queens:]):
                for i in range(num_queens, 6):
                    self.domains[i] = old_domains[i]
                continue

            # Colocar la siguiente reina y continuar la búsqueda
            self.board[position[0]][position[1]] = 1
            self.queens.append(position)
            if self.forward_checking_search(num_queens + 1, position):
                return True
            else:
                # Si no se pudo encontrar una solución, deshacer los cambios
                self.board[position[0]][position[1]] = 0
                self.queens.remove(position)
                for i in range(num_queens, 6):
                    self.domains[i] = old_domains[i]

        # Si no se pudo colocar la siguiente reina en ninguna posición válida, volver atrás
        return False

# Función auxiliar para obtener las posiciones que entran en conflicto con una reina en una posición dada
def get_conflicts(position, queen_num, queens):
    conflicts = []
    for i in range(queen_num):
        if abs(position[0] - queens[i][0]) == abs(position[1] - queens[i][1]):
            conflicts.append(queens[i])
        elif position[0] == queens[i][0]:
            conflicts.append(queens[i])
        elif position[1] == queens[i][1]:
            conflicts.append(queens[i])
    return conflicts

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
    board.forward_checking_search(0, (-1, -1))

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