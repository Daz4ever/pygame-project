import pygame
import random
import math
# import time

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275
ENTER = 13

class Minions(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = 5

    def render(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def update(self, width, height):
        self.x += self.speedx
        self.y += self.speedy

        if self.x > width:
            self.x = 0
        if self.y > height:
            self.y = 0
        if self.x < 0:
            self.x = width
        if self.y < 0:
            self.y = height

    def change_direction(self):

        rand = random.randint(0, 3)
        self.speedx = 0
        self.speedy = 0
        if rand == 0:
            self.speedy = 5
        elif rand == 1:
            self.speedy = -5
        elif rand == 2:
            self.speedx = 5
        else:
            self.speedx = -5

class Monster(Minions):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.speedx = 0
        self.speedy = 0
        self.img = pygame.image.load('images/monster.png').convert_alpha()


class Hero(Minions):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 32
        self.speedx = 0
        self.speedy = 0
        self.img = pygame.image.load('images/hero.png').convert_alpha()

    def collides(self, monster):
        return distance(self)

    def heroupdate(self):
        self.x += self.speedx
        self.y += self.speedy
        if self.x > 450:
            self.x = 450
        if self.x < 30:
            self.x = 30
        if self.y > 415:
            self.y = 415
        if self.y < 30:
            self.y = 30

class Goblin(Minions):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 32
        self.speedx = 0
        self.speedy = 0
        self.img = pygame.image.load('images/goblin.png').convert_alpha()

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
    monster = Monster(140, 115)
    hero = Hero(250, 250)
    goblin = Goblin( 350, 350)

    bgimg = pygame.image.load('images/background.png').convert_alpha()






    pygame.mixer.init()
    win_sound = pygame.mixer.Sound('sounds/win.wav')

    # now = time.time()
    # time_till_direction_change = now + 2

    change_direction_countdown = 30
    # game loop
    stop_game = False
    game_over = False
    game_over_lose = False

    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            if event.type == pygame.KEYDOWN:
                if event.key == ENTER:
                    game_over = False
                if event.key == ENTER:
                    game_over_lose = False

            if event.type == pygame.KEYDOWN:
                if event.key == KEY_DOWN:
                    hero.speedy += 2
                elif event.key == KEY_UP:
                    hero.speedy -= 2
                elif event.key == KEY_LEFT:
                    hero.speedx -= 2
                elif event.key == KEY_RIGHT:
                    hero.speedx += 2
            if event.type == pygame.KEYUP:
                if event.key == KEY_DOWN:
                    hero.speedy = 0
                elif event.key == KEY_UP:
                    hero.speedy = 0
                elif event.key == KEY_LEFT:
                    hero.speedx = 0
                elif event.key == KEY_RIGHT:
                    hero.speedx = 0
            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################
        # In the game logic section, check to see if the x position of the monster is greater than the window width, if so, set it back to 0.
        hero.heroupdate()

        if math.sqrt((hero.x - monster.x) ** 2 + (hero.y - monster.y) ** 2) < 32:
            game_over = True

        if math.sqrt((hero.x - goblin.x) ** 2 + (hero.y - goblin.y) ** 2) < 32:
            game_over_lose = True
        # (another way to do the 2 second time interval movement change for the monster)
        # now = time.time()
        # if now >= time_till_direction_change:
        #     time_till_direction_change = now + 1
        # rand = random.randint(0, 3)
        # monster.speedx = 0
        # monster.speedy = 0
        # if rand == 0:
        #     monster.speedy = 5
        # elif rand == 1:
        #     monster.speedy = -5
        # elif rand == 2:
        #     monster.speedx = 5
        # else:
        #     monster.speedx = -5




        # if monster_x + (monsterwidth * 2) > width:
        #     monsterspeedx = -monsterspeedx
        # if monster_y + (monsterheight * 2) > height:
        #     monsterspeedy = -monsterspeedy
        # if monster_x - monsterwidth < 0:
        #     monsterspeedx = -monsterspeedx
        # if monsterspeedy - monsterheight < 0:
        #     monsterspeedy = -monsterspeedy
        monster.update(512, 480)
        goblin.update(512, 480)


        change_direction_countdown -= 1
        if change_direction_countdown <= 0:
            change_direction_countdown = 60
            monster.change_direction()
            goblin.change_direction()


        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################
        screen.blit(bgimg, (0, 0))

        if game_over:
            font = pygame.font.Font(None, 25)
            text = font.render('You Win! Play Again? Hit Enter', True, (0, 0, 0))
            screen.blit(text, (80, 230))
            win_sound.play()
        elif game_over_lose:
            font = pygame.font.Font(None, 25)
            text = font.render('You Lose! Play Again? Hit Enter', True, (0, 0, 0))
            screen.blit(text, (80, 230))

        else:
            monster.render(screen)
            hero.render(screen)
            goblin.render(screen)
        # update the canvas display with the currently drawn frame


            # game_over = True

        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
