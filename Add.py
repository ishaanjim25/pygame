import pygame

pygame.init()
SW,SH = 500,500
display_surface = pygame.display.set_mode((SW,SH))

pygame.display.set_caption("Adding images and text")

bg = pygame.transform.scale(pygame.image.load('C:/Users/jimin/OneDrive/Desktop/Python/Pygame/background.png').convert(),(SW,SH))

peguin = pygame.transform.scale(pygame.image.load('C:/Users/jimin/OneDrive/Desktop/Python/Pygame/hello penguin.png').convert_alpha(),(200,200))

p_rect= peguin.get_rect(center=(SW//2,SH//2+110)) 

def game_loop():

    clock = pygame.time.Clock()
    done = True
    while  done:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
            done = False

        display_surface.blit(bg,(0,0))
        display_surface.blit(peguin,p_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if  __name__ =='__main__':
   game_loop()
