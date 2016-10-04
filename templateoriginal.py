import pygame
import random

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275
# class Minions(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.speed_x = 5
#         self.speed_y = 5
def main():
    # declare the size of the canvas
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    # initialize the pygame framework
    pygame.init()

    # create screen
    screen = pygame.display.set_mode((width, height))

    # set window caption
    pygame.display.set_caption('HerovsGoblin')

    # create a clock
    clock = pygame.time.Clock()

    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################


    bgimg = pygame.image.load('images/background.png').convert_alpha()

    heroimg = pygame.image.load('images/hero.png').convert_alpha()

    monsterimg = pygame.image.load('images/monster.png').convert_alpha()

    monster_x = 250
    monster_y = 150
    monsterwidth = 30
    monsterheight = 32
    monsterspeedx = 5
    monsterspeedy = 0
    hero_x = 230
    hero_y = 230
    herospeedx = 4
    herospeedy = 4


    change_direction_countdown = 30
    # game loop
    stop_game = False

    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_DOWN:
                    hero_y += 5
                elif event.key == KEY_UP:
                    hero_y -= 5
                elif event.key == KEY_LEFT:
                    hero_x -= 5
                elif event.key == KEY_RIGHT:
                    hero_x += 5
            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################
        # In the game logic section, check to see if the x position of the monster is greater than the window width, if so, set it back to 0.

        pygame.display.update()
        monster_x += monsterspeedx
        monster_y += monsterspeedy


        # if monster_x + (monsterwidth * 2) > width:
        #     monsterspeedx = -monsterspeedx
        # if monster_y + (monsterheight * 2) > height:
        #     monsterspeedy = -monsterspeedy
        # if monster_x - monsterwidth < 0:
        #     monsterspeedx = -monsterspeedx
        # if monsterspeedy - monsterheight < 0:
        #     monsterspeedy = -monsterspeedy

        if monster_x + monsterspeedx > width:
            monster_x = 0
        if monster_y + monsterspeedy > height:
            monster_y = 0
        if monster_x + monsterspeedx < 0:
            monster_x = width
        if monster_y + monsterspeedy < 0:
            monster_y = height

        change_direction_countdown -= 1
        if change_direction_countdown <= 0:
            change_direction_countdown = 30
            rand = random.randint(0, 3)
            monsterspeedx = 0
            monsterspeedy = 0
            if rand == 0:
                monsterspeedy = 5
            elif rand == 1:
                monsterspeedy = -5
            elif rand == 2:
                monsterspeedx = 5
            else:
                monsterspeedx = -5

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################
        screen.blit(bgimg, (0,0))
        screen.blit(heroimg, (230,230))
        screen.blit(monsterimg, (monster_x, monster_y))
        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
