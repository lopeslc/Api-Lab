import pygame
import os
import random
import time
# Initialize pygame
pygame.init()

# Create the display window
widthView = 840
heightView = 510
view = pygame.display.set_mode((widthView, heightView))
clock = pygame.time.Clock()

pygame.display.set_caption("Space Invaders")

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Load images
current_dir = os.path.dirname(os.path.abspath(__file__))
player_image_path = os.path.join(current_dir, '../../assets/images/imuno_mother.png')
invader_image_path = os.path.join(current_dir, '../../assets/images/bacteria.png')
bullet_image_path = os.path.join(current_dir, '../../assets/images/bullet.png')
hit_effect_image_path = os.path.join(current_dir, '../../assets/images/hit_effect.png')

heroe1_image_path = os.path.join(current_dir, '../../assets/images/imuno_mother.png')
heroe2_image_path = os.path.join(current_dir, '../../assets/images/eritroLoop..png')
heroe3_image_path = os.path.join(current_dir, '../../assets/images/fagolao.png')
heroe5_image_path = os.path.join(current_dir, '../../assets/images/zeGotinha.png')

def load_heroe_img(heroe_path_img):
    heroe_image = pygame.image.load(heroe_path_img)
    return heroe_image

player_image = pygame.image.load(player_image_path)
player_rect = player_image.get_rect()
player_rect.center = (widthView // 2, heightView - 50)

invader_image = pygame.image.load(invader_image_path)
invader_width = invader_image.get_width()
invader_height = invader_image.get_height()

bullet_image = pygame.image.load(bullet_image_path)
hit_effect_image = pygame.image.load(hit_effect_image_path)

# Set initial state
invader_speed = 0.5  # Reduzindo a velocidade dos invasores
bullet_speed =.85
bullets = []
invader_group = []
num_invaders =15
invader_spacing = 200
hit_effect_duration = 5  # Duração do efeito de hit em segundos
last_hit_time = 0

# Criando o grupo de invasores
for i in range(num_invaders):
    invader_rect = invader_image.get_rect()
    invader_rect.x = random.randint(0, widthView - invader_width)
    invader_rect.y = random.randint(-heightView, 0)
    invader_group.append(invader_rect)

# Função para desenhar texto na tela
def draw_text(text, font, color, surface, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_rect = bullet_image.get_rect()
                bullet_rect.centerx = player_rect.centerx
                bullet_rect.bottom = player_rect.top
                bullets.append(bullet_rect)

    # Move player based on key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= 1
    if keys[pygame.K_RIGHT] and player_rect.right < widthView:
        player_rect.x += 1
    if keys[pygame.K_DOWN] and player_rect.right < widthView:
        player_rect.y += 1
    if keys[pygame.K_UP] and player_rect.right < widthView:
        player_rect.y += -1


    # Move invader
    for invader_rect in invader_group:
        invader_rect.y += 1
        if invader_rect.top > heightView:
            invader_rect.top = -invader_height
            invader_rect.x = random.randint(0, widthView - invader_width)

    # Move bullets and check for collisions
    for bullet in bullets:
        bullet.y -= bullet_speed
        for invader_rect in invader_group:
            if bullet.colliderect(invader_rect):
                bullets.remove(bullet)
                # Exiba o efeito de impacto
                view.blit(hit_effect_image, invader_rect.topleft)
                last_hit_time = time.time()
                # Remova o invasor atingido
                invader_group.remove(invader_rect)
                break

    # Verifique se o efeito de hit acabou
    if time.time() - last_hit_time > hit_effect_duration:
        last_hit_time = 0

    # Desenha tudo na tela
    view.fill(WHITE)
    view.blit(player_image, player_rect)
    for invader_rect in invader_group:
        view.blit(invader_image, invader_rect)
    for bullet_rect in bullets:
        view.blit(bullet_image, bullet_rect)
    if last_hit_time > 0:
        pygame.display.update()  # Atualiza a tela para mostrar o efeito de hit


    pygame.display.flip()
    clock.tick(60)
# Quit pygame
pygame.quit()
