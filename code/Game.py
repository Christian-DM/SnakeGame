import pygame
import random


from code.Background import window, clock
from code.Const import width, SQUARE_SIZE, height, C_GREEN, C_WHITE, C_RED, C_BLACK, GAME_SPEED


class Game:
    def run(self):
        pass


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
    pygame.mixer_music.load(f'./asset/forest.crdownload')
    pygame.mixer_music.set_volume(0.3)
    pygame.mixer_music.play(-1)


    end_game = False

    x = width / 2
    y = height / 2

    speed_x = 0
    speed_y = 0

    snake_size = 1
    pixels = []

    food_x, food_y = spawn_food()

    while not end_game:
        window.fill(C_BLACK)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
            elif event.type == pygame.KEYDOWN:
                speed_x, speed_y = select_speed(event.key)

        draw_food(SQUARE_SIZE, food_x, food_y)

        if x < 0 or x >= width or y < 0 or y >= height:
            end_game = True

        x += speed_x
        y += speed_y

        pixels.append([x, y])
        if len(pixels) > snake_size:
            del pixels[0]

        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                end_game = True

        draw_snake(SQUARE_SIZE, pixels)


        draw_score(snake_size - 1)


        pygame.display.update()


        if x == food_x and y == food_y:
            snake_size += 1
            food_x, food_y = spawn_food()

        clock.tick(GAME_SPEED)


run_game()
