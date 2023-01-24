import pygame
pos = 0
main = pygame.display.set_mode((900, 900))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                pos = pygame.mouse.get_pos()
            if pos[0]//300 == 0:
                pygame.draw.line(main, (255, 255, 255), (0, 0), (300, 300), 5)
                pygame.draw.line(main, (255, 255, 255), (300, 0), (0, 300), 5)
            if pos[0]//300 == 1:
                pygame.draw.line(main, (255, 255, 255), (300, 0), (600, 300), 5)
                pygame.draw.line(main, (255, 255, 255), (600, 0), (300, 300), 5)
            if pos[0]//300 == 2:
                pygame.draw.line(main, (255, 255, 255), (600, 0), (900, 300), 5)
                pygame.draw.line(main, (255, 255, 255), (900, 0), (600, 300), 5)
            elif pos[1]//300 == 1:
                pygame.draw.line(main, (255, 255, 255), (0, 300), (300, 600), 5)
                pygame.draw.line(main, (255, 255, 255), (300, 300), (0, 600), 5)
    pygame.display.flip()
pygame.quit()














