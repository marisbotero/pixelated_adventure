import pygame
import sys
from menu import main_menu
from game import run_game

# Inicializa Pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aventura Pixelada")

# Loop principal
while True:
    main_menu(screen)  # Muestra el menú de inicio
    run_game(screen)   # Inicia el juego
    
    # Verifica si el usuario quiere salir
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
