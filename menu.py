import pygame
import sys
from config import WIDTH, HEIGHT, WHITE, BLACK

def main_menu(screen):
    font = pygame.font.Font(None, 50)
    clock = pygame.time.Clock()
    
    while True:
        screen.fill(WHITE)
        title_text = font.render("Aventura Pixelada", True, BLACK)
        start_text = font.render("Presiona ENTER para jugar", True, BLACK)
        exit_text = font.render("Presiona ESC para salir", True, BLACK)
        
        screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, HEIGHT//3))
        screen.blit(start_text, (WIDTH//2 - start_text.get_width()//2, HEIGHT//2))
        screen.blit(exit_text, (WIDTH//2 - exit_text.get_width()//2, HEIGHT//2 + 50))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Iniciar juego
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        clock.tick(30)
