import pygame
from config import WIDTH, HEIGHT, WHITE, BLACK, FPS
from enemies import Enemy

def run_game(screen):
    clock = pygame.time.Clock()
    player = pygame.Rect(WIDTH//2, HEIGHT-60, 40, 40)
    enemy = Enemy(100, 100, 40, 40)
    
    running = True
    while running:
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, player)
        enemy.move()
        enemy.draw(screen)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= 5
        if keys[pygame.K_RIGHT]:
            player.x += 5
        
        clock.tick(FPS)
