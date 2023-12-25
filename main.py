import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Color Catcher'
WHITE_COLOR = (255, 255, 255)
FPS = 60

# Player
player_color = (255, 0, 0)  # Red is the starting color
player_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100, 50, 50)

# Falling Block
object_rect = pygame.Rect(0, 0, 50, 50)
object_color = (255, 0, 0)  # Default color

# Clock and Screen
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)

# Game variables
score = 0
combo = 0

def draw_text(text, size, color, x, y):
    font = pygame.font.SysFont('Arial', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Game loop
def main():
    global player_color
    global combo
    global score
    global object_rect
    global object_color

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Change the color
                    player_color = random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255)])

        # Move the "player" around with the arrow keys
        keys = pygame.key.get_pressed()
        # Either left or right
        if keys[pygame.K_LEFT] and player_rect.x > 0:
            player_rect.x -= 15
        elif keys[pygame.K_RIGHT] and player_rect.x < SCREEN_WIDTH - player_rect.width:
            player_rect.x += 15

        # Set the screen boundary
        if player_rect.x < 0:
            player_rect.x = 0
        elif player_rect.x > SCREEN_WIDTH - player_rect.width:
            player_rect.x = SCREEN_WIDTH - player_rect.width

        # Create falling blocks vertically
        if random.randint(0, 100) < 5:
            object_rect.x = random.randint(0, SCREEN_WIDTH - 50)
            object_rect.y = 0
            object_color = random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255)])

        # Update the score
        if object_color == player_color:
            score += 1
            combo += 1
        else:
            combo = 0

        # Move the falling blocks
        object_rect.y += 5 + combo

        # Collision detection
        if player_rect.colliderect(object_rect):
            if object_color == player_color:
                score += 1
                combo += 1
                object_rect.y = SCREEN_HEIGHT + 1
            else:
                combo = 0

        # Draw the screen
        screen.fill(WHITE_COLOR)
        pygame.draw.rect(screen, player_color, player_rect)
        pygame.draw.rect(screen, object_color, object_rect)
        draw_text('Score: ' + str(score), 18, (0, 0, 0), SCREEN_WIDTH / 2, 10)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
