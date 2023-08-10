import pygame

pygame.init()

window = pygame.display.set_mode((600, 480))
pygame.display.set_caption("Runner")
pygame.display.set_icon(pygame.image.load("images/GUI/icon.png").convert_alpha())

heart = pygame.transform.scale(pygame.image.load("images/GUI/Heart.png").convert_alpha(), (50, 50))

lives = 3

def draw_hearts(lives):
    for x in range(lives):
        window.blit(heart, (x * 55, 5))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_hearts(lives)
    pygame.display.update()

pygame.quit()
