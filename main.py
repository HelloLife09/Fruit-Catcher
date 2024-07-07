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
    width = 20
    height = 20

    def __init__(self, x):
        self.x = x
        # y = -30
        
class Hazard:
    width = 20
    height = 20

    def __init__(self, x):
        self.x = x

class Apple(Fruit):
    def __init__(self):
        super().__init__(random.randint(0, WIDTH - 20))
        self.rect = pygame.Rect(self.x, -30, 20, 20)
        self.fruit_vel = 4.1

    def update(self):
        self.rect.y += self.fruit_vel

class Orange(Fruit):
    def __init__(self):
        super().__init__(random.randint(0, WIDTH - 20))
        self.rect = pygame.Rect(self.x, -30, 20, 20)
        self.fruit_vel = 3.8  

    def update(self):
        self.rect.y += self.fruit_vel

class Banana(Fruit):
    def __init__(self):
        super().__init__(random.randint(0, WIDTH - 20))
        self.rect = pygame.Rect(self.x, -30, 20, 20)
        self.fruit_vel = 4.5  

    def update(self):
        self.rect.y += self.fruit_vel

class Pear(Fruit):
    def __init__(self):
        super().__init__(random.randint(0, WIDTH - 20))
        self.rect = pygame.Rect(self.x, -30, 20, 20)
        self.fruit_vel = 4.2  

    def update(self):
        self.rect.y += self.fruit_vel

class Blueberry(Fruit):
    def __init__(self):
        super().__init__(random.randint(0, WIDTH - 20))
        self.rect = pygame.Rect(self.x, -30, 15, 15)  
        self.fruit_vel = 4.8  

    def update(self):
        self.rect.y += self.fruit_vel

class Grape(Fruit):
    def __init__(self):
        super().__init__(random.randint(0, WIDTH - 20))
        self.rect = pygame.Rect(self.x, -30, 15, 15)  
        self.fruit_vel = 4.6  

    def update(self):
        self.rect.y += self.fruit_vel

class Stone(Hazard):
    stone_image = pygame.transform.scale(pygame.image.load('assets\\Objects\\Rock.png').convert_alpha(), (30, 30))

    def __init__(self):
        super().__init__(random.randint(0, WIDTH - 20))
        self.rect = pygame.Rect(self.x, -30, 30, 30)
        self.hazard_vel = (random.randint(54, 78) / 10)

    def update(self):
        self.rect.y += self.hazard_vel

class Bomb(Hazard):
    bomb_image = pygame.transform.scale(pygame.image.load('assets\\Objects\\Bomb.png').convert_alpha(), (30, 30))

    def __init__(self):
        super().__init__(random.randint(0, WIDTH - 20))
        self.rect = pygame.Rect(self.x, -30, 30, 30)
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
            pygame.draw.rect(window, (255, 0, 0), fruit.rect, border_radius=10)  
        elif isinstance(fruit, Orange):
            pygame.draw.rect(window, (255, 165, 0), fruit.rect, border_radius=10)  
        elif isinstance(fruit, Banana):
            pygame.draw.rect(window, (255, 255, 0), fruit.rect, border_radius=10)  
        elif isinstance(fruit, Pear):
            pygame.draw.rect(window, (140, 255, 80), fruit.rect, border_radius=10)  
        elif isinstance(fruit, Blueberry):
            pygame.draw.rect(window, (0, 0, 255), fruit.rect, border_radius=10)  
        elif isinstance(fruit, Grape):
            pygame.draw.rect(window, (100, 0, 150), fruit.rect, border_radius=10) 

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
                hazard_class = random.choice(hazard_classes)
                hazard = hazard_class()
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
                else:
                    print("Error: Unknown hazard type")
                break

        basket.update()
        draw(window, basket, fruits, hazards)

    pygame.quit()

if __name__ == '__main__':
    main()
