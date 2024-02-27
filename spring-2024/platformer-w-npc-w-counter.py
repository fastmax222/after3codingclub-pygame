import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Player properties
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 2 * player_size
player_speed = 5
jumping = False
jump_count = 10

# Red block properties
red_block_size = 50
red_block_x = WIDTH
red_block_y = HEIGHT - 2 * red_block_size
red_block_speed = 5

# Counter variable
contact_counter = 0

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Platformer")
font = pygame.font.Font(None, 36)  # Set the font and size
clock = pygame.time.Clock()

def jump():
    global player_y, jumping, jump_count
    if not jumping:
        jumping = True
        jump_count = 10  # You can adjust the jump height by changing the jump_count

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Red block movement
    red_block_x -= red_block_speed
    if red_block_x < -red_block_size:
        red_block_x = WIDTH  # Reset to the right edge

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    red_block_rect = pygame.Rect(red_block_x, red_block_y, red_block_size, red_block_size)

    if player_rect.colliderect(red_block_rect):
        contact_counter += 1
        print("Contact Counter:", contact_counter)

    # Jumping
    if jumping:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False

    # Gravity simulation (simple - player always falls)
    if player_y < HEIGHT - player_size and not jumping:
        player_y += 5  # You can adjust the gravity value

    # Draw background
    screen.fill(WHITE)

    # Draw red block
    pygame.draw.rect(screen, RED, (red_block_x, red_block_y, red_block_size, red_block_size))

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    # Display contact counter on the screen
    text = font.render(f"Contacts: {contact_counter}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
