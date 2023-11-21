import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("La Legende de Caillou")

# Define colors
white = (255, 255, 255)
blue = (0, 0, 255)

# Define player attributes
player_width, player_height = 50, 50
player_x, player_y = 100, 100
player_velocity_y = 0
gravity = 0.5

# Main game loop
running = True
while running:
    screen.fill(white)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Apply gravity
    player_velocity_y += gravity
    player_y += player_velocity_y

    # Simulate collision with ground (for simplicity)
    if player_y >= screen_height - player_height:
        player_y = screen_height - player_height
        player_velocity_y = 0

    # Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5

    # Draw player
    pygame.draw.rect(screen, blue, (player_x, player_y, player_width, player_height))

    pygame.display.flip()  # Update the display

    pygame.time.Clock().tick(60)  # Control frame rate
