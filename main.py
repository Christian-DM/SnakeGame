import pygame
import random

# background
pygame.init()
pygame.display.set_caption("Jogo Snake Python")
width, height = 1200, 800
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# cores
C_BLACK = (0, 0, 0)
C_WHITE = (255, 255, 255)
C_RED = (255, 0, 0)
C_GREEN = (0, 255, 0)

# parametros da cobrinha
SQUARE_SIZE = 20
GAME_SPEED = 15


def spawn_food():  # gera comida
    food_x = round(random.randrange(0, width - SQUARE_SIZE) / float(SQUARE_SIZE)) * float(SQUARE_SIZE)
    food_y = round(random.randrange(0, height - SQUARE_SIZE) / float(SQUARE_SIZE)) * float(SQUARE_SIZE)
    return food_x, food_y

def draw_food(size, food_x, food_y):  # desenha comida
    pygame.draw.rect(window, C_GREEN, [food_x, food_y, size, size])

def draw_snake(size, pixels):
    for pixel in pixels:
        pygame.draw.rect(window, C_WHITE, [pixel[0], pixel[1], size, size])

def draw_score(score):
    font = pygame.font.SysFont("Lucida Sans Typewriter", 35)
    text = font.render(f"Pontos: {score}", True, C_RED)
    window.blit(text, [1, 1])

def select_speed(key):
    if key == pygame.K_DOWN:
        speed_x = 0
        speed_y = SQUARE_SIZE
    elif key == pygame.K_UP:
        speed_x = 0
        speed_y = - SQUARE_SIZE
    elif key == pygame.K_RIGHT:
        speed_x = SQUARE_SIZE
        speed_y = 0
    elif key == pygame.K_LEFT:
        speed_x = - SQUARE_SIZE
        speed_y = 0
    return speed_x, speed_y

def run_game():
    end_game = False

    x = width / 2
    y = height / 2

    speed_x = 0
    speed_y = 0

    snake_size = 1
    pixels = []

    food_x, food_y = spawn_food()

    # rodar loop infinito
    while not end_game:
        window.fill(C_BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
            elif event.type == pygame.KEYDOWN:
                speed_x, speed_y = select_speed(event.key)


        # desenhar_comida
        draw_food(SQUARE_SIZE, food_x, food_y)

        # atualizar cobra
        if x < 0  or x >= width or y < 0 or  y >= height:
            end_game = True

        x += speed_x
        y += speed_y
        # desenhar_cobra
        pixels.append([x, y])
        if len(pixels) > snake_size:
            del pixels[0]
        # se a cobrinha bater no na cobrinha
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                end_game = True

        draw_snake(SQUARE_SIZE, pixels)

        # desenhar_pontos
        draw_score(snake_size - 1)

        # atualização da tela
        pygame.display.update()

        #criar uma nova comida
        if x == food_x and y == food_y:
            snake_size += 1
            food_x, food_y = spawn_food()

        clock.tick(GAME_SPEED)


run_game()
