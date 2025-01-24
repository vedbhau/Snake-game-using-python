# Importing libraries
import pygame
import random
import time

# Initialize pygame
pygame.init()

# Window dimensions
WIDTH, HEIGHT = 600, 400

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Game settings
SNAKE_BLOCK = 10
SNAKE_SPEED = 20

# Fonts
FONT_STYLE = pygame.font.SysFont("calibri", 40)
SCORE_FONT = pygame.font.SysFont("calibri", 20)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game 🐍")

# Clock for controlling game speed
clock = pygame.time.Clock()

# Display score
def display_score(score):
    value = SCORE_FONT.render(f"Score: {score}", True, BLACK)
    screen.blit(value, [10, 10])

# Draw the snake
def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], block_size, block_size])

# Display game-over message
def game_over_message(score):
    screen.fill(BLUE)
    message = FONT_STYLE.render("Game Over! Press R to Restart", True, WHITE)
    screen.blit(message, [WIDTH // 8, HEIGHT // 3])
    score_msg = SCORE_FONT.render(f"Your Final Score: {score}", True, WHITE)
    screen.blit(score_msg, [WIDTH // 3, HEIGHT // 2])
    pygame.display.update()
    time.sleep(2)

# Main game loop
def game_loop():
    # Snake initialization
    x, y = WIDTH // 2, HEIGHT // 2
    x_change, y_change = 0, 0
    snake_list = []
    snake_length = 1

    # Food position
    food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    running = True
    game_over = False

    while running:
        while game_over:
            game_over_message(snake_length - 1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -SNAKE_BLOCK
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = SNAKE_BLOCK
                    x_change = 0

        # Check boundaries
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_over = True

        x += x_change
        y += y_change
        screen.fill(WHITE)

        # Draw food
        pygame.draw.rect(screen, RED, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])

        # Snake movement
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if snake collides with itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_over = True

        draw_snake(SNAKE_BLOCK, snake_list)
        display_score(snake_length - 1)

        # Check if snake eats the food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            snake_length += 1

        pygame.display.update()
        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()


# Start the game
game_loop()
