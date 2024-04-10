import pygame
from sys import exit
import surface_regular
import surface_text
import surface_characters
from random import randint, choice
import asyncio
# Neccesary. Start Pygame and initiate images, sounds and stuff like that


async def main():

    class Player(pygame.sprite.Sprite):
    
        def __init__(self):
            super().__init__()
            player_walk1 = pygame.image.load('first_game\\graphics\\Player\\player_walk_1.png').convert_alpha()
            player_walk2 = pygame.image.load('first_game\\graphics\\Player\\player_walk_2.png').convert_alpha()
            self.player_walk = [player_walk1, player_walk2]
            self.player_index = 0
            self.player_jump = pygame.image.load('first_game\\graphics\\Player\\jump.png').convert_alpha()

            self.image = self.player_walk[self.player_index]
            self.rect = self.image.get_rect(midbottom = (200,300))
            self.gravity = 0

            self.jump_sound = pygame.mixer.Sound('first_game\\audio\\jump.mp3')
            self.jump_sound.set_volume(0.3)

        def playerInput(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
                self.gravity= -20
                self.jump_sound.play()
        
        def applyGravity(self):
            self.gravity += 1
            self.rect.y += self.gravity
            if self.rect.bottom >=300:
                self.rect.bottom = 300

        def animation_frame(self):
            if self.rect.bottom > 300:
                self.image = self.player_jump
            else:
                self.player_index +=0.1
                if self.player_index >= len(self.player_walk): self.player_index = 0
                self.image = self.player_walk[int(self.player_index)]
        
        def update(self):
            self.playerInput()
            self.applyGravity()
            self.animation_frame()

    class Obstacle(pygame.sprite.Sprite):
        def __init__(self,type):
            super().__init__()
            
            if type == 'fly':
                fly1 = pygame.image.load('first_game\\graphics\\Fly\\Fly1.png').convert_alpha()
                fly2 = pygame.image.load('first_game\\graphics\\Fly\\Fly2.png').convert_alpha()
                self.frames = [fly1, fly2]
                y_pos = 210
            elif type == 'snail':
                snail1 = surface_characters.snail1()
                snail2 = surface_characters.snail2()
                self.frames = [snail1, snail2]
                y_pos = 300

            self.animation_index = 0    
            self.image = self.frames[self.animation_index]
            self.rect = self.image.get_rect(midbottom = (randint(900,1100), y_pos))
        
        def animationState(self):
            self.animation_index += 0.1
            if self.animation_index >= len(self.frames): self.animation_index = 0
            self.image = self.frames[int(self.animation_index)]

        def destroy(self):
            if self.rect.x <=-100:
                self.kill()

        def update(self):
            self.animationState() 
            self.rect.x -=10
            self.destroy()

        
            

    def displayScore():
        current_time = int((pygame.time.get_ticks() - start_time)/1000)
        score_surf = pygame.font.Font('first_game\\font\\Pixeltype.ttf', 32).render (f'Score: {current_time}', False, (64,64,64))
        score_rect = score_surf.get_rect(center = (400,50))
        screen.blit(score_surf, score_rect)
        return current_time

    def obstacleMovement(obstacle_list):
        if obstacle_list:
            for obstacle_rect in obstacle_list:
                obstacle_rect.x -= 5
                
                if obstacle_rect.bottom == 300:
                    screen.blit(snail_surf, obstacle_rect)
                else:
                    screen.blit(fly_surf, obstacle_rect)
            
            obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -50]
            return obstacle_list    
        else: return []

    def collisions(player, obstacles):
        if obstacles:
            for obstacles_rect in obstacles:
                if player.colliderect(obstacles_rect): return False
        
        return True

    def collisionSprite():
        collide_list = pygame.sprite.spritecollide(player.sprite, obstacle_group,False)
        
        if collide_list:
            obstacle_group.empty()
            return False
        else: return True

    def player_animation():
        global player_surf,player_index

        if player_rect.bottom < 300:
            player_surf = player_jump
        else:
            player_index +=0.1
            if player_index >= len(player_walk): player_index = 0
            player_surf = player_walk[int(player_index)]

        #animation when walk
        #animation when jump


    #Pygame method
    pygame.init()
    game_active = False
    start_time = 0
    score = 0
    #------Creating a CLOCK or FPS moduler-----------
    clock = pygame.time.Clock()
    #------Creting a tittle-------------------
    pygame.display.set_caption('Kirita')
    #-------Creating a play surface ----------
    screen_width,screen_height  = 800,400
    screen = pygame.display.set_mode((screen_width,screen_height))
    bg_music = pygame.mixer.Sound('first_game\\audio\\music.wav')
    bg_music.set_volume(0.5)
    bg_music.play(loops=-1)

    #Groups
    player = pygame.sprite.GroupSingle()
    player.add(Player())

    obstacle_group = pygame.sprite.Group()

    # ---------------Surfaces------------
    sky_surface = surface_regular.imageBackground('first_game\\graphics\\Sky.png').convert()
    ground_surface = surface_regular.imageBackground('first_game\\graphics\\ground.png').convert()

    text_surface = surface_text.surfaceText('My Game')

    score_rect = surface_text.surfaceText('Score').get_rect(center = (400,50))

    #--------Creating Characters---------------

    #Enemy
    snail1 = surface_characters.snail1()
    snail2 = surface_characters.snail2()
    snail = [snail1, snail2]
    snail_index = 0
    snail_surf = snail[snail_index]

    fly1 = pygame.image.load('first_game\\graphics\\Fly\\Fly1.png').convert_alpha()
    fly2 = pygame.image.load('first_game\\graphics\\Fly\\Fly2.png').convert_alpha()
    fly = [fly1, fly2]
    fly_index = 0
    fly_surf = fly[fly_index]

    obstacle_rect_list = []

    #Player
    player_walk1 = surface_characters.player()
    player_walk2 = pygame.image.load('first_game\\graphics\\Player\\player_walk_2.png').convert_alpha()
    player_index = 0
    player_jump = pygame.image.load('first_game\\graphics\\Player\\jump.png').convert_alpha()

    player_walk = [player_walk1, player_walk2]
    player_surf = player_walk[player_index]
    player_rect = player_surf.get_rect(midbottom = (80,300))
    player_gravity = 0

    #Intro Screen
    player_stand = pygame.image.load('first_game\\graphics\\Player\\player_stand.png').convert_alpha()
    player_stand = pygame.transform.scale2x(player_stand)
    player_stand_rect = player_stand.get_rect(center = (400,200))


    #--------Timer---------------
    obstacle_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(obstacle_timer, 900 )

    snail_animation_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(snail_animation_timer, 500)

    fly_animation_timer = pygame.USEREVENT + 3
    pygame.time.set_timer(fly_animation_timer, 200)

    #--------Create a While Loop to run the screen---------------

    while True:

        for event in pygame.event.get(): #-- gets all pygame player inputs
            if event.type == pygame.QUIT: #-- synonymous: Close X on windows
                    pygame.quit()
                    exit()

            if game_active:
                if event.type == pygame.KEYDOWN and player_rect.bottom >= 300: 
                    if event.key == pygame.K_SPACE:
                        player_gravity = -20
            else:
                if event.type == pygame.KEYDOWN: 
                    game_active = True
                    start_time = pygame.time.get_ticks()

            if game_active:
                if event.type == obstacle_timer : 
                    obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail'])))
                    # if randint(0,2):
                    #     obstacle_rect_list.append(snail_surf.get_rect(midbottom = (randint(900,1100),300)))
                    # else:
                    #     obstacle_rect_list.append(fly_surf.get_rect(midbottom = (randint(900,1100),210)))

                if event.type == snail_animation_timer:
                    if snail_index == 0: snail_index = 1
                    else: snail_index=0
                    snail_surf = snail[snail_index]

                if event.type == fly_animation_timer:
                    if fly_index == 0: fly_index = 1
                    else: fly_index=0
                    fly_surf = fly[fly_index]

        #draww all our elements
        #update everything
        if game_active:
            screen.blit(sky_surface,(0,0)) #-- Put a surface over the main window
            screen.blit(ground_surface,(0,300))
            score = displayScore()
        
            
            #Player
            # player_gravity +=1
            # player_rect.right = 100
            # player_animation()
            # screen.blit(player_surf, player_rect)
            # player_rect.y += player_gravity
            # if player_rect.bottom >= 300: player_rect.bottom = 300

            player.draw(screen)
            player.update()

            #Obstacle Movement
            # obstacle_rect_list = obstacleMovement(obstacle_rect_list)

            obstacle_group.draw(screen)
            obstacle_group.update()

            # Collision with enemy
            # game_active = collisions(player_rect, obstacle_rect_list)
            game_active = collisionSprite()
        
        else:
            screen.fill((94,129,162))

            font = pygame.font.Font('first_game\\font\\Pixeltype.ttf', 42)
            text_intro = font.render('Press Any Key', False, 'White').convert_alpha()
            text_intro_rect = text_intro.get_rect(center = (400, 350))

            game_name = font.render('Pixel Runner', False, 'White').convert_alpha()
            game_name_rect = game_name.get_rect(center = (400,50))

            game_score = font.render(f'Your Score: {score}', False, 'White').convert_alpha()
            game_score_rect = game_score.get_rect(center = (400,350))

            screen.blit(player_stand, player_stand_rect)
            screen.blit(game_name,game_name_rect)

            if score == 0: screen.blit(text_intro, text_intro_rect)
            else: screen.blit(game_score, game_score_rect)
            
            obstacle_rect_list.clear()
            player_rect.midbottom = (20,300)
            player_gravity = 0
        
        await asyncio.sleep(0)

        pygame.display.update() #--This method display the screen created before.
        fps = 60 #-- times per sec
        clock.tick(fps) #-- This method tells to the loop no to run more than FPS

asyncio.run( main())