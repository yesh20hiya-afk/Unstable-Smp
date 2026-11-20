import random
import pygame

# Initialize Pygame
pygame.init()

# Screen & game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FONT_SIZE = 36
MOVEMENT_SPEED = 5
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pet Food Game")
clock = pygame.time.Clock()

# TODO 1: Load and scale background image ("pet_bg.jpg")
loaded_bg = pygame.image.load("pet_bg.jpg")
background_image = pygame.transform.scale(loaded_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

# TODO 2: Set font
font = pygame.font.SysFont("Arial", FONT_SIZE)


class Pet(pygame.sprite.Sprite):
    def __init__(self, width=50, height=50, color=(139, 69, 19)):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)

    def move(self, x_change, y_change):
        # TODO 3: Keep the pet inside the screen
        self.rect.x = max(0, min(SCREEN_WIDTH - self.rect.width, self.rect.x + x_change))
        self.rect.y = max(0, min(SCREEN_HEIGHT - self.rect.height, self.rect.y + y_change))


class Food(pygame.sprite.Sprite):
    def __init__(self, width=30, height=30, color=(255, 165, 0)):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)


# Sprites & game state
pet = Pet()
pet_food = Food()
all_sprites = pygame.sprite.Group()
all_sprites.add(pet)
all_sprites.add(pet_food)

food_collected = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not food_collected:
        # TODO 4: Move the pet with arrow keys
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
        pet.move(x_change, y_change)

        # TODO 5: Check collision with food
        if pet.rect.colliderect(pet_food.rect):
            all_sprites.remove(pet_food)
            food_collected = True

    # Draw background and sprites
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    # TODO 6: Show message in the middle when food is collected
    if food_collected:
        message = font.render("Food Collected!", True, pygame.Color("black"))
        text_x = (SCREEN_WIDTH - message.get_width()) // 2
        text_y = (SCREEN_HEIGHT - message.get_height()) // 2
        screen.blit(message, (text_x, text_y))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()