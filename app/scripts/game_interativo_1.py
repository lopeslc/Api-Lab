import pygame

def game_interativo_1():    
    display = pygame.display.set_mode((500,500))
    
    rectangle1 = pygame.Rect(0, 0, 50, 50)
    rectangle2 = pygame.Rect(450, 0, 50, 50)
    ball = pygame.Rect(250, 250, 50, 50)
    
    loop=True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = False


        display.fill((254,206,132))
        # minha tela sempre atualizando
        pygame.draw.rect(display, (199,51,37), rectangle1)
        pygame.draw.rect(display, (199,51,37), rectangle2)
        pygame.draw.circle(display, (181,219,255), (ball.x, ball.y), ball.width//2)
        
        pygame.display.flip()
        
game_interativo_1()