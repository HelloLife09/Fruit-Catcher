from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import math
import random

pygame.init()

pygame.display.set_caption("Fruit Catcher")

WIDTH, HEIGHT = 450, 600
BACKGROUND = pygame.transform.scale(pygame.image.load('assets\\Background.png'), (WIDTH, HEIGHT))
FPS = 60

BASKET_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

class Basket(): 
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.x_vel = 0  

    def move(self, dx):
        self.x += dx
        self.rect.x = self.x

    def move_left(self):
        self.x_vel = -BASKET_VEL

    def move_right(self):
        self.x_vel = BASKET_VEL

    def update(self):
        if self.x_vel < 0 and self.rect.x > 0:
            self.move(self.x_vel)
        elif self.x_vel > 0 and (self.rect.x + self.rect.width) < WIDTH:
            self.move(self.x_vel)
        else:
            self.x_vel = 0

class Fruit:
    width = 40
    height = 40 

    def __init__(self, x):
        self.x = x

class Hazard:
    width = 40
    height = 40 

    def __init__(self, x):
        self.x = x

class Heart:
    width = 40
    height = 40 
    heart_image = pygame.transform.scale(pygame.image.load("assets\\Heart.png").convert_alpha(), (width, height))

    def __init__(self):
        self.x = random.randint(0, WIDTH - 20)
        self.rect = pygame.Rect(self.x, -30, width, height)
        self.heart_vel = (random.randint(36, 74) / 10)

class Apple(Fruit):
    apple_image = pygame.transform.scale(pygame.image.load("assets\\Fruits\\Apple.png").convert_alpha(), (width, height))

    def __init__(self):
        super().__init__(random.randint(0, WIDTH - 20))
        self.rect = pygame.Rect(self.x, -30, width, height)
        self.fruit_vel = 4.1

    def update(self):
        self.rect.y += self.fruit_vel

class Orange(Fruit):
    orange_image = pygame.transform.scale(pygame.image.load("assets\\Fruits\\Orange.png").convert_alpha(), (width, height))

    def __init__(self):
        super().__init__(random.randint(0, WIDTH - 20))
        self.rect = pygame.Rect(self.x, -30, width, height)
        self.fruit_vel = 3.8  

    def update(self):
        self.rect.y += self.fruit_vel

class Banana(Fruit):
    banana_image = pygame.transform.scale(pygame.image.load("assets\\Fruits\\Banana.png").convert_alpha(), (width + 10, height + 10))

    def __init__(self):
        super().__init__(random.randint(0, WIDTH - 20))
        self.rect = pygame.Rect(self.x, -30, width, height + 10)
        self.fruit_vel = 4.5  

    def update(self):
        self.rect.y += self.fruit_vel

class Pear(Fruit):
    pear_image = pygame.transform.scale(pygame.image.load("assets\\Fruits\\Pear.png").convert_alpha(), (width, height))

    def __init__(self):
        super().__init__(random.randint(0, WIDTH - 20))
        self.rect = pygame.Rect(self.x, -30, width, height)
        self.fruit_vel = 4.2  

    def update(self):
        self.rect.y += self.fruit_vel

class Blueberry(Fruit):
    blueberry_image = pygame.transform.scale(pygame.image.load("assets\\Fruits\\Blueberry.png").convert_alpha(), (width - 10, height - 10))

    def __init__(self):
        super().__init__(random.randint(0, WIDTH - 20))
        self.rect = pygame.Rect(self.x, -30, width - 10, height - 10)  
        self.fruit_vel = 4.8  

    def update(self):
        self.rect.y += self.fruit_vel

class Grape(Fruit):
    grape_image = pygame.transform.scale(pygame.image.load("assets\\Fruits\\Grape.png").convert_alpha(), (width, height + 10))

    def __init__(self):
        super().__init__(random.randint(0, WIDTH - 20))
        self.rect = pygame.Rect(self.x, -30, width, height + 10)  
        self.fruit_vel = 4.6  

    def update(self):
        self.rect.y += self.fruit_vel

class Stone(Hazard):
    stone_image = pygame.transform.scale(pygame.image.load('assets\\Hazards\\Rock.png').convert_alpha(), (width - 5, height - 5))

    def __init__(self):
        super().__init__(random.randint(0, WIDTH - 20))
        self.rect = pygame.Rect(self.x, -30, width - 5, height - 5)
        self.hazard_vel = (random.randint(54, 78) / 10)

    def update(self):
        self.rect.y += self.hazard_vel

class Bomb(Hazard):
    bomb_image = pygame.transform.scale(pygame.image.load('assets\\Hazards\\Bomb.png').convert_alpha(), (width, height))

    def __init__(self):
        super().__init__(random.randint(0, WIDTH - 20))
        self.rect = pygame.Rect(self.x, -30, width, height)
        self.hazard_vel = (random.randint(64, 95) / 10)

    def update(self):
        self.rect.y += self.hazard_vel


def draw(window, basket, fruits, hazards):
    bar = pygame.Rect(0, 480, WIDTH, 10)
    window.blit(BACKGROUND, (0, 0))

    pygame.draw.rect(window, (255, 230, 179), basket.rect)

    pygame.draw.rect(window, (50, 50, 50), bar)

    for fruit in fruits:
        if isinstance(fruit, Apple):
            window.blit(Apple.apple_image, fruit.rect)  
        elif isinstance(fruit, Orange):
            window.blit(Orange.orange_image, fruit.rect) 
        elif isinstance(fruit, Banana):
            window.blit(Banana.banana_image, fruit.rect)
        elif isinstance(fruit, Pear):
            window.blit(Pear.pear_image, fruit.rect) 
        elif isinstance(fruit, Blueberry):
            window.blit(Blueberry.blueberry_image, fruit.rect)
        elif isinstance(fruit, Grape):
            window.blit(Grape.grape_image, fruit.rect)

    for hazard in hazards:
        if isinstance(hazard, Stone):
            window.blit(Stone.stone_image, hazard.rect)
        elif isinstance(hazard, Bomb):
            window.blit(Bomb.bomb_image, hazard.rect)

    pygame.display.update()

def main():
    clock = pygame.time.Clock()

    fruit_classes = [Apple, Orange, Banana, Pear, Blueberry, Grape]
    fruits = []
    fruit_count = 0
    fruit_add_incr = 2000

    hazard_classes = [Stone, Bomb]
    hazards = []
    hazard_count = 0
    hazard_add_incr = 5000

    basket = Basket(WIDTH/2, HEIGHT-180, 100, 60)

    life = 0
    score = 0

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    break

        keys = pygame.key.get_pressed()

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            basket.move_left()
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            basket.move_right()
        else:
            basket.x_vel = 0

        time_elapsed = clock.tick(FPS)
        fruit_count += time_elapsed
        hazard_count += time_elapsed

        if fruit_count > fruit_add_incr:
            for _ in range(random.randint(1, 3)):
                fruit_class = random.choice(fruit_classes)
                fruit = fruit_class() 
                fruits.append(fruit)
            fruit_add_incr = max(200, fruit_add_incr - 10)
            fruit_count = 0

        if hazard_count > hazard_add_incr:
            for _ in range(random.randint(0, 1)):
                if random.random() <= 0.85:
                    hazard == Stone()
                else:
                    hazard == Bomb()
                hazards.append(hazard)
            hazard_add_incr = max(600, hazard_add_incr - 5)
            hazard_count = 0

        for fruit in fruits[:]:
            fruit.update()
            if fruit.rect.y > HEIGHT:
                fruits.remove(fruit)
            elif fruit.rect.bottom >= basket.rect.top and fruit.rect.colliderect(basket.rect):
                fruits.remove(fruit)
                score += 1
                break

        for hazard in hazards[:]:
            hazard.update()
            if hazard.rect.y > HEIGHT:
                hazards.remove(hazard)
            elif hazard.rect.bottom >= basket.rect.top and hazard.rect.colliderect(basket.rect):
                hazards.remove(hazard)
                if isinstance(hazard, Stone):
                    score -= 1
                elif isinstance(hazard, Bomb):
                    score -= 3
                    life -= 1
                break

        basket.update()
        draw(window, basket, fruits, hazards)

    pygame.quit()

if __name__ == '__main__':
    main()
