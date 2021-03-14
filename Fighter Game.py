import pygame
import random
import math
from os import path
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
WIDTH = 800
HEIGHT = 800




#Initialise Pygame
pygame.init()


# --------------------- Classes --------------------- #

class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()

        #Makes a wall with size 40x40
        self.image = pygame.image.load("WallImage.jpg").convert()
        self.rect=self.image.get_rect()

        #Make the wall where we pass in the x and y paramaters
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



class Player(pygame.sprite.Sprite):
         def __init__(self):
             super().__init__()
             self.health = 100
             self.score = 0
             self.kills = 0
             self.coins = 0
             self.damage = 5
             self.x_speed = 0
             self.y_speed = 0

             #Set player image and location
             self.image = pygame.image.load("PlayerGuy.png").convert()
             self.image.set_colorkey(BLACK)
             self.rect=self.image.get_rect()
             self.rect.x=500
             self.rect.y=700

         def move(self,x,y):

             #Adds the movement values to the x and y of player
             self.x_speed += x
             self.y_speed += y

         def update(self):

            #Moves the player on x-axis
            self.rect.x += self.x_speed

            #Check if player collides with an object in wall_list, if it does, add to player_hit_list.
            player_hit_list = pygame.sprite.spritecollide(player, wall_list, False)

            for wall in player_hit_list:
                if player.x_speed > 0:                  #if the player is moving right and it hits a wall
                    player.rect.right = wall.rect.left  #Set right edge of player to left edge of wall to stop it going through
                elif player.x_speed < 0:                #Same as above, but the opposite (moving left)
                    player.rect.left = wall.rect.right

            #Moves player on y-axis
            self.rect.y += self.y_speed

            #Check if player collides with an object in wall_list, if it does, add to
            # player_hit_list.
            player_hit_list = pygame.sprite.spritecollide(player, wall_list, False)

            for wall in player_hit_list:
                if player.y_speed > 0: #if player is moving down and hits a wall,
                    player.rect.bottom = wall.rect.top #set bottom of player to top of wall
                elif player.y_speed < 0: # Same as above but opposite (moving up)
                    player.rect.top = wall.rect.bottom


class Bullet(pygame.sprite.Sprite):
    def __init__(self,mouse_x,mouse_y):
        super().__init__()

        self.image = pygame.image.load("bullet.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.damage = 10


        speed = 5
        self.rect.x = player.rect.x        #Make the bullet spawn where the player is at
        self.rect.y = player.rect.y

        x_difference = mouse_x - WIDTH/2         #Calculate distance between mouse and player
        y_difference = mouse_y - HEIGHT/2          #for angle calculations below

        angle = math.atan2(y_difference, x_difference); #Works out gradient, and then the angle of the line
        self.x_change = math.cos(angle) * speed         #Multiply the angle with
        self.y_change = math.sin(angle) * speed
        self.x = self.rect.x                            #self.rect.x and self.rect.y are integers
        self.y = self.rect.y                            #this results in highly inaccurate aiming,
                                                        #the bullets don't go where the mouse is.
    def update(self):                                   #self.x and self.x are floating points
                                                        #which allows for more accuracy in calculations
        self.x += self.x_change
        self.y += self.y_change
        self.rect.x = int(self.x)                       #convert final answer back to integers
        self.rect.y = int(self.y)                       #since rect can't be float

class Enemy(pygame.sprite.Sprite):

    def __init__(self,x,y):

        super().__init__()

        self.health = 20
        self.score = 10
        self.damage = 5
        self.speed = 1
        self.distance = 0
        self.image= pygame.image.load("enemy.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_speed = 0
        self.y_speed = 0


class Portal(pygame.sprite.Sprite):

    def __init__(self,x,y):

        super().__init__()

        self.image = pygame.image.load("nether.png").convert()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Coin(pygame.sprite.Sprite):

    def __init__(self,x,y):

        super().__init__()

        self.image = pygame.image.load("coin1.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



class EnemyBullet(pygame.sprite.Sprite):

    def __init__(self,x,y):

        super().__init__()

        self.image = pygame.image.load("enemybullet.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.damage = 3

        self.speed = 8
        self.rect.x = x       #Make the bullet spawn where the player is at
        self.rect.y = y

        x_difference = player.rect.x - self.rect.x       #Calculate distance between player and enemy
        y_difference = player.rect.y - self.rect.y    #for angle calculations below

        self.angle = math.atan2(y_difference, x_difference); #Works out gradient, and then the angle of the line
        self.x_change = math.cos(self.angle) * self.speed         #Multiply the angle with
        self.y_change = math.sin(self.angle) * self.speed
        self.x = self.rect.x                            #self.rect.x and self.rect.y are integers
        self.y = self.rect.y                            #this results in highly inaccurate aiming,
                                                        #the bullets don't go where the mouse is.
    def update(self):                                   #self.x and self.x are floating points
                                                        #which allows for more accuracy in calculations
        self.x += self.x_change
        self.y += self.y_change
        self.rect.x = int(self.x)                       #convert final answer back to integers
        self.rect.y = int(self.y)                       #since rect can't be float


class Camera(pygame.sprite.Sprite):


    def __init__(self,w,h):
        
        super().__init__()
        
        self.camera = pygame.Rect(0,0,w,h) #Sets a camera rectangle of size 800x800 (size of window)
                                           #Numbers keep track of how far the camera is from the start
        self.width = w
        self.height = h

    def movement(self, hello):
         return hello.rect.move(self.camera.topleft) #Moves the sprites around the same as the camera movement

    def update(self, player):
        x = (player.rect.x*-1) + 400  #Keeps the player centered. Multiply by -1 because camera needs
        y = (player.rect.y*-1) + 400  #to move in oppposite direction to make it look like it's moving.

        self.camera = pygame.Rect(x,y, self.width, self.height)


#                     Powerups 

class AddHealth(pygame.sprite.Sprite):

    def __init__(self,x,y):

        super().__init__()

        self.health = 15
        self.addhealth = 10
        self.distance = 0
        self.image=pygame.image.load("addhealth.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        
class ExtraDamage(pygame.sprite.Sprite):

    def __init__(self,x,y):

        super().__init__()

        self.health = 15
        self.distance = 0
        self.image=pygame.image.load("extradamage.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


        



# --------------------------------------------------- #





# ---------------------- Functions ---------------------- #



# ------------------------------------------------------ #




# ------------- Pygame lists ------------- #

all_sprites_list = pygame.sprite.Group()

player_list = pygame.sprite.Group()
player_hit_list = pygame.sprite.Group()

enemy_list = pygame.sprite.Group()
enemy_hit_list = pygame.sprite.Group()

enemy_bullet_list = pygame.sprite.Group()
enemy_bullet_hit_list = pygame.sprite.Group()

wall_list = pygame.sprite.Group()
wall_hit_list = pygame.sprite.Group()

bullet_list = pygame.sprite.Group()
bullet_hit_list = pygame.sprite.Group()

portal_list = pygame.sprite.Group()
portal_hit_list = pygame.sprite.Group()

coin_list = pygame.sprite.Group()
coin_hit_list = pygame.sprite.Group()


            #Powerups

powerup_list = pygame.sprite.Group()

addhealth_list = pygame.sprite.Group()
addhealth_hit_list = pygame.sprite.Group()

extradamage_list = pygame.sprite.Group()
extradamage_hit_list = pygame.sprite.Group()


# ---------------------------------------- #




# Set the width and height of the screen [width, height]
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Fighter Game")
startscreen_image = pygame.image.load("background.jpg").convert()


#Variables needed to be set before main loop

enemy_kills = 0
coins_left = 0
level = 0
seconds_alive = 0

extradamage_start_time = 0
extradamage_time_left = 0
extra_damage = False

directory = path.dirname(__file__) #Get the path to the file

pausescreen = False
newlevel = False
pause = False
done = False
startscreen = True
powerup = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


#Top

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:     #Making the player move.
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:     #If you want to go left, you -3 from the x coordinate.
                player.move(-3,0)
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.move(3,0)
            elif event.key == pygame.K_UP or event.key == pygame.K_w:     #If you want to go up, you -3 from the y coordinate
                player.move(0,-3)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.move(0,3)
            elif event.key == pygame.K_p:
                pausescreen = True
                player.x_speed = 0
                player.y_speed = 0

            elif event.key == pygame.K_SPACE:
                pos = pygame.mouse.get_pos()        #Get mouse position
                mouse_x = pos[0]                    #Get x coordinate of mouse position
                mouse_y = pos[1]                    #Get y coordinate of mouse position

                bullet = Bullet(mouse_x, mouse_y)
                bullet_list.add(bullet)
                all_sprites_list.add(bullet)

        elif event.type == pygame.KEYUP:      #Making the player stop
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:    #Since you want the player to stop, you have to do the opposite
                player.move(3,0)              #action as above so that 0 gets added to the x or y
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.move(-3,0)
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                player.move(0,3)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.move(0,-3)

    #Saving highscore to textfile
    try:
        HIGHSCORE_FILE = open("highscore.txt", 'r')
        highscore = int(HIGHSCORE_FILE.read())
        HIGHSCORE_FILE.close()
    except:
        highscore = 0



    while startscreen == True:
        pause = True
        for event in pygame.event.get():        #Exit the startscreen if the user hits space
            if event.type == pygame.QUIT:
                startscreen = False
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player = Player()
                    player_list.add(player)
                    all_sprites_list.add(player)
                    startscreen = False
                    pause = False
        screen.blit(startscreen_image, [0,0])
        font = pygame.font.SysFont("Arial", 50)


        #Set the text
        start_text = font.render("Fighter Game", True, WHITE, BLACK)
        instruction_text = font.render("Use your mouse to aim,", True, WHITE, BLACK)
        instruction_text2 = font.render("Press Space to shoot", True, WHITE, BLACK)
        instruction_text3 = font.render("Use arrow keys or WASD to move", True,WHITE,BLACK)
        space_text= font.render("Press Space to Play", True, WHITE, BLACK)
        hs_text = font.render("Highscore: " + str(highscore), True,WHITE,BLACK)

        #Blit the text to the screen
        screen.blit(start_text, [400-(start_text.get_width() // 2), 200])
        screen.blit(instruction_text, [400-(instruction_text.get_width() // 2), 300])
        screen.blit(instruction_text2, [400-(instruction_text2.get_width() // 2), 400])
        screen.blit(instruction_text3, [400-(instruction_text3.get_width() // 2), 500])
        screen.blit(space_text, [400-(space_text.get_width() // 2), 600])
        screen.blit(hs_text, [(400-hs_text.get_width() // 2), 700])
        pygame.display.update()


    while pausescreen == True:

        for event in pygame.event.get():        #Exit the startscreen if the user hits space
            if event.type == pygame.QUIT:
                pausescreen = False    #Exit the game if the player presses exit
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pausescreen = False

        screen.fill(BLACK)
        font = pygame.font.SysFont("Arial", 50)
        pausetext = font.render("Game Paused, Press P to continue", True, WHITE, BLACK)
        screen.blit(pausetext, [400-(pausetext.get_width() //2), 300])
        pygame.display.update()






    # -------- Create level at the start of the game, and also if the player dies -------- #


    if level == 0 and pause == False:
        for coin in coin_list:
            coin_list.remove(coin)
        for enemy in enemy_list:
            enemy_list.remove(enemy)


        # KEY
        # 0 = Nothing
        # 1 = Wall
        # 2 = Enemy
        # 3 = Portal
        # 4 = Coins

        maps = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,0,0,1,0,0,4,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,0,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,0,0,0,0,0,0,0,0,2,1,1,1,1,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,0,0,4,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,0,0,2,0,2,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1],
                [1,1,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,0,2,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,1,0,0,0,3,3,1,1,1,1,1],
                [1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,3,3,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


        for y in range(24):
            for x in range(26):
                if maps[y][x] == 1:
                    wall=Wall(x*100, y*100)
                    all_sprites_list.add(wall)
                    wall_list.add(wall)

        for y in range(24):
            for x in range(26):
                if maps[y][x] == 2:
                    enemy=Enemy(x*100, y*100)
                    all_sprites_list.add(enemy)
                    enemy_list.add(enemy)




        'Portal is created in while loop dependant on specific conditions'


        randomcoin = random.randrange(1,4)
        for y in range(24):
            for x in range(26):
                if maps[y][x] == 4:
                    coin=Coin(x*100, y*100)
                    all_sprites_list.add(coin)
                    coin_list.add(coin)
        level += 1



    # ------------------------------------------------------------------------------------ #



    lastxpos = player.rect.x
    lastypos = player.rect.y

    all_sprites_list.update()

    camera = Camera(WIDTH,HEIGHT) #Create an instantiation of camera class
    camera.update(player)    #Update the camera so that the player moves around.



    # ------- Player Death ------ #

    if player.health <= 0:

        for event in pygame.event.get():        #Exit the startscreen if the user hits space
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    startscreen = True

        screen.blit(startscreen_image, [0,0])

        font = pygame.font.SysFont("Arial", 50)
        death_text = font.render("You died", True, WHITE, BLACK)
        restart_text = font.render("Press space to go to the main menu", True, WHITE, BLACK)
        screen.blit(death_text, [400-(death_text.get_width() // 2), 300])
        screen.blit(restart_text, [400-(restart_text.get_width() // 2), 400])

    #Remove all existing sprites
        for wall in wall_list:
            wall_list.remove(wall)
        for wall in all_sprites_list:
            all_sprites_list.remove(wall)

        for coin in coin_list:
            coin_list.remove(wall)
        for coin in coin_list:
            all_sprites_list.remove(coin)

        for enemy in enemy_list:
            enemy_list.remove(enemy)
        for enemy in all_sprites_list:
            all_sprites_list.remove(enemy)

        for bullet in bullet_list:
            bullet_list.remove(bullet)
        for bullet in all_sprites_list:
            bullet_list.remove(bullet)

        #Reset all player statistics for restart
        player_list.remove(player)
        all_sprites_list.remove(player)
        level = 0




        pygame.display.update()

    # --------------------------- #


                    # --- Collisions --- #

    # -------- Collision between bullet and wall -------- #

    while len(bullet_list) > 3:             #Makes it so that only 3 bullets can be on the screen at a time
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    for bullet in bullet_list:              #Remove bullet if it collides with wall
        if pygame.sprite.spritecollide(bullet, wall_list, False):
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    # --------------------------------------------------- #



    # -------- Collision between player and bullets ------- #


    #Player bullet collision with enemy
    for bullet in bullet_list:                                                  #If a bullet collides with enemy,
        enemy_hit_list = pygame.sprite.spritecollide(bullet, enemy_list, False) #Add to enemy_hit_list

        for enemy in enemy_hit_list:
            enemy.health -= bullet.damage       #Take away health from enemy and add score to player
            player.score += bullet.damage
            all_sprites_list.remove(bullet)     #Remove the bullet after collision
            bullet_list.remove(bullet)


    #Enemy bullet collision with wall
    for enemybullet in enemy_bullet_list:
        if pygame.sprite.spritecollide(enemybullet, wall_list, False):  #If enemy bullet collides with a wall, remove it
            all_sprites_list.remove(enemybullet)
            enemy_bullet_list.remove(enemybullet)

    #Enemy bullet collision with player

    player_hit_list = pygame.sprite.spritecollide(player, enemy_bullet_list, False)

    for enemybullet in player_hit_list:

        player.health -= enemybullet.damage
        all_sprites_list.remove(enemybullet)
        enemy_bullet_list.remove(enemybullet)
        player_hit_list.remove(enemybullet)



    # -------------------------------------------------------------- #
    


    # ------------------ Powerup Collisions ------------------ #

    
    #Addhealth powerup
        
    if len(addhealth_list) > 0:

        addhealth_hit_list = pygame.sprite.spritecollide(player, addhealth_list, False)
            
        for addhealth in addhealth_hit_list:
            
            player.health += addhealth.addhealth
            all_sprites_list.remove(addhealth)
            powerup_list.remove(addhealth)
            addhealth_list.remove(addhealth)


    #-----------------


    #Extra damage powerup
            
    if len(extradamage_list) > 0:
        
        extradamage_hit_list = pygame.sprite.spritecollide(player, extradamage_list, False)

        #Set this variable to true, used for blitting the powerups on the screen so player can see which powerups are active
        extra_damage = True                                         
         

        for extradamage in extradamage_hit_list:
            
            #Remove the collided sprite
            all_sprites_list.remove(extradamage)                    
            powerup_list.remove(extradamage)
            extradamage_list.remove(extradamage)

            #Set the start timer so that the powerup can remove itself later
            extradamage_start_time = pygame.time.get_ticks()

                
    #If the powerup is active,
    if extra_damage == True: 

        #Start the timer for how long it has left
        extradamage_time_left = (pygame.time.get_ticks() - extradamage_start_time)/1000 

        #Increase the bullet damage
        for bullet in bullet_list:
            bullet.damage = 20

        player.damage = 20


    #Once the powerup has reached the set time, reverse the extra damage
    if extradamage_time_left > 20:
        extra_damage = False
        bullet.damage = 10
        player.damage = 5


    #-------------------


    

    # ------------- Coins and Coin collisions ------------- #

    player_hit_list = pygame.sprite.spritecollide(player, coin_list, False)

    for coin in player_hit_list:
        player.coins += 1
        coin_list.remove(coin)
        all_sprites_list.remove(coin)
        coins_left -= 1




    # ----------- Enemy movement, shooting at player wall collision, player collision ---------- #

    player_hit_list = pygame.sprite.spritecollide(player, enemy_list, False)

    for enemy in enemy_list:

        #Enemy x movement
        enemy.x_speed = player.rect.x-enemy.rect.x  #Calculate horizontal distance from player to enemy
        enemy.y_speed = player.rect.y-enemy.rect.y  #Calculate vertical distance
        enemy.distance = math.sqrt((enemy.x_speed**2) + (enemy.y_speed**2)) #Calculate actual distance using pythagorus' theorum
            
        if enemy.distance <= 600 and enemy.distance >= 400:         #Depending on distance, change speed
            enemy.rect.x += enemy.x_speed/400

        elif enemy.distance <= 400:
            enemy.rect.x += enemy.x_speed/200                       #The closer the enemy, the slower it'll go

        elif enemy.distance <= 50:
            enemy.x_speed = 0
                
        if enemy.distance <= 600 and enemy.distance >= 400:         #Depending on distance, change speed
            enemy.rect.x += enemy.x_speed/400

        elif enemy.distance <= 400:
            enemy.rect.x += enemy.x_speed/200                       #The closer the enemy, the slower it'll go

        elif enemy.distance <= 50:
            enemy.x_speed = 0
                        

        #Enemy x wall collision
        for wall in wall_list:
            enemy_hit_list = pygame.sprite.spritecollide(wall, enemy_list, False)   #Same as player collision.

            for enemy in enemy_hit_list:                #If moving right and you hit a wall, set the right edge of the enemy to left edge of wall
                if enemy.x_speed > 0:                   #to stop it moving any further.
                    enemy.rect.right = wall.rect.left
                elif enemy.x_speed < 0:
                    enemy.rect.left = wall.rect.right


        #Enemy y movement
        if enemy.distance <= 600 and enemy.distance >= 400:                 #The X and Y movements must be done seperately to avoid huge glitches
            enemy.rect.y += enemy.y_speed/400                               #Calculating seperately allows for much smoother movement, and for the code to actual work

        elif enemy.distance <= 400:
            enemy.rect.y += enemy.y_speed/200

        elif enemy.distance <= 50:
            enemy.y_speed = 0

        #Enemy Y wall collision
        for wall in wall_list:
            enemy_hit_list = pygame.sprite.spritecollide(wall, enemy_list, False)

            for enemy in enemy_hit_list:

                if enemy.y_speed > 0:
                    enemy.rect.bottom = wall.rect.top
                elif enemy.y_speed < 0:
                    enemy.rect.top = wall.rect.bottom



        #Take health from both the enemy, and the player if they collide.
                    
        for enemy in player_hit_list:
            enemy.health -= player.damage
            player.health -= enemy.damage
            player.score += enemy.score

        if pygame.sprite.spritecollide(player, enemy_list, False):
           player.rect.x = lastxpos         #Bounce the player back if it collides with an enemy
           player.rect.y = lastypos

        enemyx = enemy.rect.x
        enemyy = enemy.rect.y
        playerx = player.rect.x
        playery = player.rect.y

        distance = math.sqrt((playerx-enemyx)**2 + (playery-enemyy)**2)  #Calculate distance from player to enemy in pixels using pythagorus
        
        if distance <= 600:                         #If player is within 400 pixels of enemy, enemy will shoot at player
            randomv = random.randint(1,20)          #Shoot on average twice a second
            if randomv == 1:
                enemybullet = EnemyBullet(enemy.rect.x+40, enemy.rect.y+20) #Makes bullet spawn in the middle of enemy
                enemy_bullet_list.add(enemybullet)
                all_sprites_list.add(enemybullet)



        #Enemy Death
                
        if enemy.health <= 0:       #Remove the enemy if it has died
            
            spawnpowerup = 1 #random.randint(1,4)                      #1 in 4 chance of spawning a powerup
            if spawnpowerup == 1:

                #Addhealth powerup
                randompowerup = 2 #random.randint(1,4)                 #Randomly choose which powerup is spawned
                
                if randompowerup == 1:                                 #This powerup adds health to the enemy
                
                    addhealth = AddHealth(enemy.rect.x,enemy.rect.y)    #
                    
                    addhealth_list.add(addhealth)
                    powerup_list.add(addhealth)
                    all_sprites_list.add(addhealth)
                    
                    addhealth_start_ticks = pygame.time.get_ticks() #Update the start of the timer
        
                #-----------------


                #Extra damage powerup
                elif randompowerup == 2:

                    extradamage = ExtraDamage(enemy.rect.x,enemy.rect.y)    #Create a 

                    extradamage_list.add(extradamage)
                    powerup_list.add(extradamage)
                    all_sprites_list.add(extradamage)

                    extradamage_start_ticks = pygame.time.get_ticks()
                


            
            #Remove the enemy after we get the coordinates                    
            all_sprites_list.remove(enemy)
            enemy_list.remove(enemy)
            enemy_kills += 1


    
            
    #Remove powerups after they're 10 seconds old
    
    seconds_alive_addhealth = 0
    seconds_alive_extradamage = 0
    
    for addhealth in addhealth_list:
        
        seconds_alive_addhealth = (pygame.time.get_ticks() - addhealth_start_ticks)/1000    #Get the time since the sprite has been created
            
        if seconds_alive_addhealth >= 5:                                         #Remove the health powerup if it has been left for more than the set time
            addhealth_list.remove(addhealth)
            powerup_list.remove(addhealth)
            all_sprites_list.remove(addhealth)

    for extradamage in extradamage_list:

        seconds_alive_extradamage = (pygame.time.get_ticks() - extradamage_start_ticks)/1000

        if seconds_alive_extradamage >= 5:
            extradamage_list.remove(extradamage)
            powerup_list.remove(extradamage)
            all_sprites_list.remove(extradamage)

            
            

    # ---------------------------------------------------------------------------------------------------------------- #

    
    
                
    # ------------------------- Next Levels ------------------------- #



    if len(enemy_list) == 0 and len(coin_list) == 0:  #If there are no enemies, coins (meaning player has beaten level), create new level
        
         oldhealth = player.health #Save old player stats before deleting them and making a new player instance
         oldscore = player.score
         oldkills = player.kills
         oldcoins = player.coins
         oldlevel = level

    
         if len(portal_list) == 0:
             for y in range(24):                         #Create portal
                 for x in range(26):
                    if maps[y][x] == 3:
                        portal=Portal(x*100, y*100)
                        all_sprites_list.add(portal)
                        portal_list.add(portal)

         portal_hit_list = pygame.sprite.spritecollide(player, portal_list, False)

         if len(portal_hit_list) != 0 and player.x_speed == 0 and player.y_speed == 0: #Remove everything from current level if the player goes into portal
                for wall in all_sprites_list:
                    all_sprites_list.remove(wall)
                for wall in wall_list:
                    wall_list.remove(wall)
                    all_sprites_list.remove(player)
                    player_list.remove(player)

                for bullet in bullet_list:
                    bullet_list.remove(bullet)
                for bullet in all_sprites_list:
                    all_sprites_list.remove(bullet)

                for portal in portal_list:      #Remove the portal once the player has collided with it
                    portal_list.remove(portal)  #So that it can be created in the next levels
                for portal in all_sprites_list:
                    all_sprites_list.remove(portal)
                for portal in portal_hit_list:
                    portal_list.remove(portal)





                 # KEY
                 # 0 = Nothing
                 # 1 = Wall
                 # 2 = Enemy
                 # 3 = Portal
                 # 4 = Coins
                 # 5 = Player spawnpoint


                randommap = random.randint(1,4)


                if randommap == 1:

                    maps = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,1,0,0,0,0,2,0,0,2,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,2,0,1,0,0,0,0,0,0,0,0,0,2,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,4,0,0,1,1,1,1,1,0,0,0,0,4,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,4,0,0,0,1,0,0,2,0,0,2,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,2,0,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,2,0,0,0,1,0,0,0,0,0,0,4,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1,1,1,1,1],
                            [1,1,1,1,0,0,1,1,1,1,1,0,0,2,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,2,0,0,2,0,0,1,0,2,0,0,2,0,0,0,0,3,3,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,3,3,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

                elif randommap == 2:

                    maps = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,2,0,0,0,0,2,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,2,0,0,0,0,1,0,0,2,0,4,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,4,0,0,2,0,1,0,0,2,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,2,1,0,0,0,0,0,0,2,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,4,0,0,0,1,0,0,0,0,0,2,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,4,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,2,0,2,0,2,1,0,0,0,0,2,0,0,3,3,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,3,3,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

                elif randommap == 3:

                    maps = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,0,0,2,0,1,0,0,0,0,2,1,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,2,1,0,0,2,0,1,0,0,0,0,0,1,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,2,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,4,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,1,1,0,0,4,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,1,1,1,1,1],
                            [1,1,1,1,0,0,2,1,1,1,1,1,1,1,1,0,0,0,4,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,2,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,2,0,0,2,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,2,1,0,0,0,1,0,0,0,0,0,3,3,1,1,1,1,1],
                            [1,1,1,1,0,0,2,0,4,0,0,0,0,2,0,0,0,0,0,0,3,3,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

                elif randommap == 4:

                    maps = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,0,0,2,0,0,0,0,0,0,2,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,0,4,0,0,0,0,0,0,0,0,0,0,2,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,0,0,2,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,0,0,1,1,0,0,0,4,0,1,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,2,4,0,0,0,0,0,0,2,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,1,1,0,0,0,0,2,0,0,1,1,1,1,1,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,0,2,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,2,0,0,0,0,1,1,1,1,0,2,0,0,1,1,1,1,1],
                            [1,1,1,1,0,2,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,1,2,0,0,1,0,2,0,4,0,3,3,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,3,3,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


                player = Player()
                player_list.add(player)
                all_sprites_list.add(player)
                player.health = oldhealth
                player.score = oldscore
                player.kills = oldkills
                player.coins = oldcoins
                level = oldlevel + 1


                #Adding in features for new levels
                for y in range(24):
                    for x in range(26):
                        if maps[y][x] == 1:
                            wall=Wall(x*100, y*100)
                            all_sprites_list.add(wall)
                            wall_list.add(wall)


                for y in range(24):
                    for x in range(26):
                        if maps[y][x] == 2:
                            randomenemy = random.randint(1,4)
                            if randomenemy == 1:
                                enemy=Enemy(x*100, y*100)
                                all_sprites_list.add(enemy)
                                enemy_list.add(enemy)

                for y in range(24):
                    for x in range(26):
                        if maps[y][x] == 4:
                            coin=Coin(x*100, y*100)
                            all_sprites_list.add(coin)
                            coin_list.add(coin)
                            

    # -------------------------------------------------------- #



    # ----------------- Displaying things on screen --------------- #
    
    ' -- Highscore + Player Scoreboard + Level information -- '
    if player.score > highscore:
        highscore = player.score

        try:
            HIGHSCORE_FILE = open("highscore.txt", 'w')
            HIGHSCORE_FILE.write(str(player.score))
            HIGHSCORE_FILE.close()
        except:
            1 + 1



    if pause == False and player.health > 0:      #Only display the scoreboard if the player is alive and the game is playing
        screen.fill(BLACK)
        for sprite in all_sprites_list:                           #The same as all_sprites_list.draw, however now,
            
            screen.blit(sprite.image, camera.movement(sprite))  #we're drawing it compared to where the camera is rather than the window itself
            

                                                                #rather than the start screen
    

        pygame.draw.line(screen, BLACK, [0,784],[800,784],50)
        #Displaying health, score, etc to user

        font = pygame.font.SysFont("hiraginosansgb", 30, True)
        text = font.render("Health: " + str(player.health) + " Score: " + str(player.score) + " Kills: " + str(enemy_kills) + " Coins: " + str(player.coins), True, WHITE)
        text_x = (400-(text.get_width() // 2))
        text_y = 768
        screen.blit(text, [text_x, text_y])    #Blitting scoreboard

        font = pygame.font.SysFont("Aerial", 30, False, False)

        highscore_text = font.render("Highscore: " + str(highscore), False, WHITE)
        enemy_remain_text = font.render("Enemies Remaining: " + str(len(enemy_list)), False, WHITE)
        coin_remain_text = font.render("Coins Remaining: " + str(len(coin_list)), False, WHITE)

        font = pygame.font.SysFont("Aerial", 60, False, False)
        level_text = font.render("Level: " + str(level), False, WHITE)

        screen.blit(highscore_text, [0,0])
        screen.blit(enemy_remain_text, [0,30])
        screen.blit(coin_remain_text, [0,60])

        screen.blit(level_text, [(400 - (level_text.get_width() // 2)), 0])
        
        




    pygame.display.flip()

    clock.tick(60)

    # --------------------------------------------------------------- #

# Close the window and quit.
pygame.quit()
