import pygame

pygame.init()

window = pygame.display.set_mode((600, 480))
pygame.display.set_caption("Runner")
pygame.display.set_icon(pygame.image.load("images/GUI/icon.png").convert_alpha())

heart = pygame.transform.scale(pygame.image.load("images/GUI/Heart.png").convert_alpha(), (50, 50))
player = [pygame.transform.scale(pygame.image.load("images/Player/Player1.png").convert_alpha(), (70, 70)),
          pygame.transform.scale(pygame.image.load("images/Player/Player2.png").convert_alpha(), (70, 70))]
BG = pygame.image.load("images/BG.png").convert()

lives = 3
animation_frame = 0
BG_X = 0
jump_count = 8
is_jump = False
player_y = 330

clock = pygame.time.Clock()

def draw_hearts(lives: int):
    for x in range(lives):
        window.blit(heart, (x * 55, 5))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.blit(BG, (BG_X + 600, 0))
    window.blit(BG, (BG_X, 0))
    window.blit(player[animation_frame], (100, player_y))
    draw_hearts(lives)
    pygame.display.update()

    keys = pygame.key.get_pressed()

    # Jumping
    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -8:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 8

    clock.tick(10)

    BG_X += -5
    animation_frame += 1
    if animation_frame > 1:
        animation_frame = 0
    if BG_X <= -600:
        BG_X = 0

pygame.quit()
