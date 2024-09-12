#Snake in 100 mins
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        self.grow = False

    def move(self):
        head = self.body[0]
        if self.direction == "UP":
            new_head = (head[0], head[1] - 1)
        elif self.direction == "DOWN":
            new_head = (head[0], head[1] + 1)
        elif self.direction == "LEFT":
            new_head = (head[0] - 1, head[1])
        elif self.direction == "RIGHT":
            new_head = (head[0] + 1, head[1])

        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def grow_snake(self):
        self.grow = True

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0]*GRID_SIZE, segment[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Food class
class Food:
    def __init__(self):
        self.position = self.randomize_position()

    def randomize_position(self):
        return random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0]*GRID_SIZE, self.position[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Game function
def game():
    snake = Snake()
    food = Food()
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != "DOWN":
                    snake.direction = "UP"
                elif event.key == pygame.K_DOWN and snake.direction != "UP":
                    snake.direction = "DOWN"
                elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                    snake.direction = "LEFT"
                elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                    snake.direction = "RIGHT"

        # Check if snake eats the food
        if snake.body[0] == food.position:
            snake.grow_snake()
            food.position = food.randomize_position()

        # Check if snake hits the wall or itself
        if (snake.body[0][0] < 0 or snake.body[0][0] >= GRID_WIDTH or
            snake.body[0][1] < 0 or snake.body[0][1] >= GRID_HEIGHT or
            snake.body[0] in snake.body[1:]):
            running = False

        snake.move()
        snake.draw()
        food.draw()

        pygame.display.update()
        clock.tick(10)

    pygame.quit()


game()
