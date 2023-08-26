import pygame
from random import randint
# Settings
pygame.init()

window = pygame.display.set_mode((600, 480))
pygame.display.set_caption("Runner")
pygame.display.set_icon(pygame.image.load("images/GUI/icon.png").convert_alpha())
# Player Images
heart = pygame.transform.scale(pygame.image.load("images/GUI/Heart.png").convert_alpha(), (50, 50))
player = [pygame.transform.scale(pygame.image.load("images/Player/Player1.png").convert_alpha(), (40, 70)),
          pygame.transform.scale(pygame.image.load("images/Player/Player2.png").convert_alpha(), (40, 70))]
# Enemy settings
enemy = pygame.transform.scale(pygame.image.load("images/Enemy.png").convert_alpha(), (50, 70))
enemy_timer = pygame.USEREVENT + 1
enemies_in_game = []
# BG images
BG = pygame.image.load("images/BG.png").convert_alpha()
Clouds = pygame.image.load("images/Clouds.png").convert_alpha()
Grass = pygame.image.load("images/Grass.png").convert_alpha()
Mountians = pygame.image.load("images/Mountians.png").convert_alpha()
Trees = pygame.image.load("images/Trees.png").convert_alpha()
# Player variables
lives = 3
animation_frame = 0
jump_count = 8
is_jump = False
player_y = 330
# BG variables
BG_X = 0
Clouds_X = 0
Grass_X = 0
Mountians_X = 0
Trees_X = 0
# Sounds
jump_sounds = [pygame.mixer.Sound("Sounds/Jump1.wav"),
               pygame.mixer.Sound("Sounds/Jump2.wav"),
               pygame.mixer.Sound("Sounds/Jump3.wav")]
music = pygame.mixer.Sound("Sounds/BG.mp3")
music.play(-1)

score = 0
main_font = pygame.font.Font("Other/Kanit-Black.ttf", 40)
message = main_font.render("Score: " + str(score), False, (0, 0, 0))
clock = pygame.time.Clock()
pygame.time.set_timer(enemy_timer, randint(2000, 3000))
def draw_hearts(lives: int):
    for x in range(lives):
        window.blit(heart, (x * 55, 5))
# Main cycle
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == enemy_timer:
            enemies_in_game.append(enemy.get_rect(topleft=(650, 330)))
            pygame.time.set_timer(enemy_timer, randint(1700, 3000))

    player_collider = player[animation_frame].get_rect(topleft=(100, player_y))
    # Drawing BG
    window.blit(BG, (BG_X + 600, 0))
    window.blit(BG, (BG_X, 0))
    window.blit(Mountians, (Mountians_X + 600, 0))
    window.blit(Mountians, (Mountians_X, 0))
    window.blit(Grass, (Grass_X + 600, 0))
    window.blit(Grass, (Grass_X, 0))
    window.blit(Trees, (Trees_X + 600, 0))
    window.blit(Trees, (Trees_X, 0))
    window.blit(Clouds, (Clouds_X + 600, 0))
    window.blit(Clouds, (Clouds_X, 0))
    #  Drawing other
    if enemies_in_game:
        for el in enemies_in_game:
            window.blit(enemy, el)
            el.x -= 10
            if player_collider.colliderect(el):
                lives -= 1
    window.blit(player[animation_frame], (100, player_y))
    draw_hearts(lives)
    pygame.display.update()
    window.blit(message, (0, 0))

    keys = pygame.key.get_pressed()

    # Jumping
    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
            jump_sounds[randint(0, 2)].play()
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
    # Moving BG
    BG_X += -1.0
    Mountians_X += -2.5
    Grass_X += -3.5
    Trees_X += -3.0
    Clouds_X += -2.0

    animation_frame += 1
    if animation_frame > 1:
        animation_frame = 0
    # BG Change
    if BG_X <= -600:
        BG_X = 0
    if Mountians_X <= -600:
        Mountians_X = 0
    if Clouds_X <= -600:
        Clouds_X = 0
    if Grass_X <= -600:
        Grass_X = 0
    if Trees_X <= -600:
        Trees_X = 0
    # Lives check
    if lives <= 0:
        pygame.quit()
# Ending game
pygame.quit()