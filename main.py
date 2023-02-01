import pygame

#pygame window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")

#game loop
running = True
robotDragging = False
#Robot Pose
robotPose = [350,250]

while running:

    #background
    screen.fill((0, 0, 0))

    #robot rectangle object
    robotRect = pygame.Rect(robotPose[0], robotPose[1], 100, 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                if robotRect.collidepoint(event.pos):
                    robotDragging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = robotRect.x - mouse_x
                    offset_y = robotRect.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                robotDragging = False

        elif event.type == pygame.MOUSEMOTION:
            if robotDragging:
                mouse_x, mouse_y = event.pos
                robotPose[0] = mouse_x + offset_x
                robotPose[1] = mouse_y + offset_y

    robotRect = pygame.Rect(robotPose[0], robotPose[1], 100, 100)

    #draw robotRect
    pygame.draw.rect(screen, (255, 0, 0), robotRect, 2)

    #show text
    font = pygame.font.Font('freesansbold.ttf', 14)

    #Current Position Text
    posText = font.render('Current Position:', True, (255, 255, 255), (0, 0, 0))
    posTextRect = posText.get_rect()
    posTextRect.left = 10
    posTextRect.top = 10
    screen.blit(posText, posTextRect)
    
    #Target Position Text
    targetText = font.render('Target Position:', True, (255, 255, 255), (0, 0, 0))
    targetTextRect = targetText.get_rect()
    targetTextRect.left = 10
    targetTextRect.top = 25
    screen.blit(targetText, targetTextRect)

    pygame.time.Clock().tick(144)

    pygame.display.update()