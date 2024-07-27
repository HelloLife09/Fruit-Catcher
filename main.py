from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import math
import random

pygame.init()

pygame.display.set_caption("Fruit Catcher")

WIDTH, HEIGHT = 450, 600
BACKGROUND = pygame.transform.scale(pygame.image.load('Images\\Background.png'), (WIDTH, HEIGHT))
FPS = 60

BASKET_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

class Basket(): 
    basket_image = pygame.transform.scale(pygame.image.load('Images\\Basket.png').convert_alpha(), (80, 60))

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
    width = 60
    height = 60
    heart_image = pygame.transform.scale(pygame.image.load("Images\\Heart.png").convert_alpha(), (width, height))

    def __init__(self):
        self.x = random.randint(0, WIDTH - 20)
        self.rect = pygame.Rect(self.x, -30, Heart.width, Heart.height)
        self.heart_vel = (random.randint(36, 74) / 10)

    def update(self):
        self.rect.y += self.heart_vel

class Apple(Fruit):
    apple_image = pygame.transform.scale(pygame.image.load("Images\\Fruits\\Apple.png").convert_alpha(), (Fruit.width, Fruit.height))

    def __init__(self):
        super().__init__(random.randint(0, WIDTH - Fruit.width))
        self.rect = pygame.Rect(self.x, -30, Fruit.width, Fruit.height)  
        self.fruit_vel = 4.1

    def update(self):
        self.rect.y += self.fruit_vel

class Orange(Fruit):
    orange_image = pygame.transform.scale(pygame.image.load("Images\\Fruits\\Orange.png").convert_alpha(), (Fruit.width, Fruit.height))

    def __init__(self):
        super().__init__(random.randint(0, WIDTH - Fruit.width))
        self.rect = pygame.Rect(self.x, -30, Fruit.width, Fruit.height)  
        self.fruit_vel = 3.8 

    def update(self):
        self.rect.y += self.fruit_vel

class Banana(Fruit):
    banana_image = pygame.transform.scale(pygame.image.load("Images\\Fruits\\Banana.png").convert_alpha(), (Fruit.width + 10, Fruit.height + 10))

    def __init__(self):
        super().__init__(random.randint(0, WIDTH - Fruit.width - 10))
        self.rect = pygame.Rect(self.x, -30, Fruit.width + 10, Fruit.height + 10)
        self.fruit_vel = 4.5  

    def update(self):
        self.rect.y += self.fruit_vel
        
class Pear(Fruit):
    pear_image = pygame.transform.scale(pygame.image.load("Images\\Fruits\\Pear.png").convert_alpha(), (Fruit.width, Fruit.height))

    def __init__(self):
        super().__init__(random.randint(0, WIDTH - Fruit.width))
        self.rect = pygame.Rect(self.x, -30, Fruit.width, Fruit.height)  
        self.fruit_vel = 4.2 

    def update(self):
        self.rect.y += self.fruit_vel

class Blueberry(Fruit):
    blueberry_image = pygame.transform.scale(pygame.image.load("Images\\Fruits\\Blueberry.png").convert_alpha(), (Fruit.width - 10, Fruit.height - 10))

    def __init__(self):
        super().__init__(random.randint(0, WIDTH - Fruit.width + 10))
        self.rect = pygame.Rect(self.x, -30, Fruit.width - 10, Fruit.height - 10)  
        self.fruit_vel = 4.8  
    
    def update(self):
        self.rect.y += self.fruit_vel

class Grape(Fruit):
    grape_image = pygame.transform.scale(pygame.image.load("Images\\Fruits\\Grape.png").convert_alpha(), (Fruit.width, Fruit.height + 10))

    def __init__(self):
        super().__init__(random.randint(0, WIDTH - Fruit.width))
        self.rect = pygame.Rect(self.x, -30, Fruit.width, Fruit.height + 10)  
        self.fruit_vel = 4.6  

    def update(self):
        self.rect.y += self.fruit_vel

class Stone(Hazard):
    stone_image = pygame.transform.scale(pygame.image.load('Images\\Hazards\\Rock.png').convert_alpha(), (Hazard.width - 5, Hazard.height - 5))

    def __init__(self):
        super().__init__(random.randint(0, WIDTH - Hazard.width + 5))
        self.rect = pygame.Rect(self.x, -30, Hazard.width - 5, Hazard.height - 5)
        self.hazard_vel = (random.randint(54, 78) / 10)

    def update(self):
        self.rect.y += self.hazard_vel

class Bomb(Hazard):
    bomb_image = pygame.transform.scale(pygame.image.load('Images\\Hazards\\Bomb.png').convert_alpha(), (Hazard.width, Hazard.height))

    def __init__(self):
        super().__init__(random.randint(0, WIDTH - Hazard.width))
        self.rect = pygame.Rect(self.x, -30, Hazard.width, Hazard.height)
        self.hazard_vel = (random.randint(64, 95) / 10)

    def update(self):
        self.rect.y += self.hazard_vel

class Fly(Hazard):
    fly_image = pygame.transform.smoothscale(pygame.image.load('Images\\Hazards\\Fly.png').convert_alpha(), (Hazard.width- 10, Hazard.height))

    def __init__(self):
        super().__init__(random.randint(0, WIDTH - Hazard.width + 10))
        self.rect = pygame.Rect(self.x, -30, Hazard.width - 10, Hazard.height)
        self.hazard_vel = (random.randint(72, 98) / 10)
        self.x_vel = random.choice([vel for vel in range(-10, 10) if abs(vel) > 4])

    def update(self):
        self.rect.y += self.hazard_vel
        self.rect.x += self.x_vel
        if self.rect.x < 0 or self.rect.x > WIDTH - self.rect.width:
            self.x_vel *= -1

def draw(window, basket, fruits, hazards, heart, add_heart):
    bar = pygame.Rect(0, 480, WIDTH, 10)
    window.blit(BACKGROUND, (0, 0))

    pygame.draw.rect(window, (50, 50, 50), bar)

    window.blit(Basket.basket_image, basket.rect)

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
        elif isinstance(hazard, Fly):
            window.blit(Fly.fly_image, hazard.rect)

    if add_heart and heart is not None:
        window.blit(Heart.heart_image, heart.rect)
        add_heart = False

    pygame.display.update()

def main():
    clock = pygame.time.Clock()

    fruit_classes = [Apple, Orange, Banana, Pear, Blueberry, Grape]
    fruits = []
    fruit_count = 0
    fruit_add_incr = 2000

    hazard_classes = [Stone, Bomb, Fly]
    hazards = []
    hazard_count = 0
    hazard_add_incr = 4000

    health_count = 0
    heart_list = []
    add_heart = True
    health_add_incr = 10000

    basket = Basket(WIDTH/2, HEIGHT-175, 80, 60)

    health = 3
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

        if health <= 0:
            run = False

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
        health_count += time_elapsed

        if fruit_count > fruit_add_incr:
            for _ in range(random.randint(1, 3)):
                fruit_class = random.choice(fruit_classes)
                fruit = fruit_class() 
                fruits.append(fruit)
            fruit_add_incr = max(200, fruit_add_incr - 10)
            fruit_count = 0
        
        if health_count > health_add_incr and health < 3:
            heart = Heart()
            heart_list.append(heart)
            add_heart = True
            health_count = 0


        if hazard_count > hazard_add_incr:
            if random.random() <= 0.65:
                hazard = random.choice([hazard for hazard in hazard_classes if hazard != Bomb])()
            else:
                hazard = Bomb()
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

        for heart in heart_list:
            heart.update()
            if heart.rect.y > HEIGHT:
                heart_list.remove(heart)
            elif heart.rect.bottom >= basket.rect.top and heart.rect.colliderect(basket.rect):
                heart_list.remove(heart)
                health += 1
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
                    health -= 1
                break

        basket.update()
        draw(window, basket, fruits, hazards, heart_list[0] if heart_list else None, add_heart)

    pygame.quit()

if __name__ == '__main__':
    main()
