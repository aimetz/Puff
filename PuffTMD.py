import pygame
import sys
import random
from pygame.math import Vector2


class Man:
    def __init__(self, x, y, speed):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, -1*speed)


def main():
    pygame.init()


    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))

    game_over = False
    pygame.key.set_repeat(5)
    green = (0,200,112)
    black = (255, 255, 255)
    red = (235, 0, 0)
    size = 40
    speed = .2
    val = 200 # needs to equal size / speed
    man = Man(width/2, height/2, speed)
    length = 1
    i = 0
    rl = [] # list to hold food locations
    bl = [] # list to hold old positions
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    man.velocity = man.velocity.rotate(-1.5)
                    bl.append((man.position[0], man.position[1])) 
                if event.key == pygame.K_RIGHT:
                    man.velocity = man.velocity.rotate(1.5)
                    bl.append((man.position[0], man.position[1])) 
        screen.fill(black) #fills screen black is actually white
        pygame.draw.rect(screen, green, (man.position[0], man.position[1], size, size)) # draws head
        bl.append((man.position[0], man.position[1])) # adds current position to end of list
        if len(bl) > val*(length+1): # if holding enough values removes the first
            bl.pop(0)
        for q in range(1, length): # draws all of body excpet head
            if q > 2 and abs(man.position[0]-bl[len(bl)-val*q][0])<(size-5) and abs(man.position[1]-bl[len(bl)-val*q][1])<(size-5): # checks if head hit each body part
                game_over = True
                print(length)
            pygame.draw.rect(screen, green, (bl[len(bl)-val*q][0], bl[len(bl)-val*q][1], size, size))
        man.position += man.velocity
        if man.position[0] < 0-size or man.position[0] > width or man.position[1] < 0-size or man.position[1] > height: # checks if you hit a wall
            game_over = True
            print(length)
        if i % 3000 == 0:
            rl.append((random.randint(0, width-size), random.randint(0, height-size), random.randint(0, width-size), random.randint(0, height-size)))
        for r in rl: # the list of food tokens
            if abs(r[0] - man.position[0]) < size and abs(r[1] - man.position[1]) < size: # checks if head hits each token
                man.position[0] = r[2]
                man.position[1] = r[3]
                rl.remove(r)
                length += 1
            elif abs(r[2] - man.position[0]) < size and abs(r[3] - man.position[1]) < size: # checks if head hits each token
                man.position[0] = r[0]
                man.position[1] = r[1]
                rl.remove(r)
                length += 1
            pygame.draw.rect(screen, red, (r[0], r[1], size, size)) #prints all remaining foods
            pygame.draw.rect(screen, red, (r[2], r[3], size, size))
        i += 1 # counts number of loops
        pygame.display.update()


main()