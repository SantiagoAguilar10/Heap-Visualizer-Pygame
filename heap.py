# a chambear
# a chambear
# todo el mundo a chambear
import pygame
from random import randint
from time import sleep
from collections import deque as dq

CELL_SIZE = 50  # Tamaño de cada celda en píxeles
DELAY = 0.02    # Velocidad de animación

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)

global heap
heap = [1, 3, 5, 7, 8, 6, 9]

# Inicializa Pygame
pygame.init()

# Información de pantalla
# Esto es para que mi compu no haga K-BOOM!
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

# Calcula el tamaño ideal de celda para que el laberinto quepa
max_cell_width = screen_width // 25
max_cell_height = screen_height // 25
CELL_SIZE = min(CELL_SIZE, max_cell_width, max_cell_height)

# Crea la ventana con el tamaño ajustado
screen = pygame.display.set_mode((25 * CELL_SIZE, 25 * CELL_SIZE))

# Le ponemos primero el titulo de DFS
pygame.display.set_caption("Heap")

# Dividir la pantalla en una cuadrícula
cols = screen.get_width() // CELL_SIZE
rows = screen.get_height() // CELL_SIZE

def draw_grid():
    for x in range(0, screen.get_width(), CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, screen.get_height()))
    for y in range(0, screen.get_height(), CELL_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (screen.get_width(), y))


def add():
    x = 125
    y = 400

    for i in heap:
        pygame.draw.circle(screen, BLUE, (x + CELL_SIZE // 2, y + CELL_SIZE // 2), CELL_SIZE // 3)
        font = pygame.font.Font(None, 36)
        text = font.render(str(i), True, WHITE)
        text_rect = text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
        screen.blit(text, text_rect)
        x += CELL_SIZE + 10
        y -= CELL_SIZE + 10






def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(WHITE)
        draw_grid()
        add()
        pygame.display.update()
        sleep(2)
main()



"""
# Construir un montículo (heapq) sin import heapq

monti = [0]*30
tam = 0

def insertar(n):
  global tam
  tam += 1
  monti[tam] = n
  flotar(tam)


def flotar(x):
  padre = x//2
  while padre >= 1:
    if monti[padre] < monti[x]:
      monti[padre], monti[x] = monti[x], monti[padre]
      x = padre
      padre = x//2
    else:
      break

def hundir(n):

  while 2*n < tam:
    izq = 2*n
    der = 2*n + 1
    if monti[izq] > monti[der]:
      grande = izq
    else:
      grande = der
    if monti[n] < monti[grande]:
      monti[n], monti[grande] = monti[grande], monti[n]
    n = grande

def pop():
  global tam
  monti[1], monti[tam] = monti[tam], monti[1]
  tam -= 1
  hundir(1)
  r = monti[tam+1]
  monti[tam+1] = 0
  return monti[tam+1]

lista = [1, 2, 3, 4, 5, 6, 7, 8]

for n in lista:
  insertar(n)

print(monti)
print(monti[1:tam+1])
print(pop())
"""
