import pygame

def main():
    pygame.init()
    sw,sh = 500,500
    screen = pygame.display.set_mode((sw,sh))
    pygame.display.set_caption('Colour changing sprite')

    colours = {
        'red': pygame.Color('red'),
        'green': pygame.Color('green'),
        'blue': pygame.Color('blue'),
        'yellow': pygame.Color('yellow'),
        'white': pygame.Color('white')
    }
    current_colour = colours['white']

    x,y = 30,30
    sprite_w,sprite_h = 60,60

    clock = pygame.time.Clock()

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True 

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3

        x = min(max(0,x),sw - sprite_w)
        y = min(max(0,y),sh - sprite_h )

        if x ==0: current_colour = colours['blue']
        elif x == sw - sprite_w: current_colour=colours['yellow']
        elif y == 0: current_colour = colours['red']
        elif y == sh - sprite_h:
            current_colour = colours['green'] 
        else:
            current_colour = colours['white']

        screen.fill((0,0,0))
        pygame.draw.rect(screen,current_colour,(x,y,sprite_w,sprite_h))
        pygame.display.flip()
        clock.tick(90)

    pygame.quit()

if __name__ =="__main__":
    main()

    