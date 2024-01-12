import pygame, sys
from pygame.locals import KEYUP, QUIT
pygame.init()
play_or_not = False
#font type, Font size
test_font_score = pygame.font.Font(None, 40)
test_font_game_over = pygame.font.Font(None, 100)
test_font_time = pygame.font.Font(None, 40)
screen = pygame.display.set_mode((675, 500))
pygame.display.set_caption('Jump')
clock = pygame.time.Clock()
t = 0
time_left_for_fly_to_come = 5
sky_surface = pygame.Surface((800,400))
sky_surface.fill('light blue')
lava_surface = pygame.Surface((400,200))
lava_surface.fill('red')
test_surfaces = pygame.Surface((700,500))
test_surfaces.fill('dark green')  
test_surfaece = pygame.image.load('graphics/ground.png').convert_alpha()

enemy_snail = pygame.image.load('graphics/enemy.png').convert_alpha()
snail_rec = enemy_snail.get_rect(midbottom = (680,350))
player = pygame.image.load('graphics/player.png').convert_alpha()
player_rec = player.get_rect(midbottom = (80,350))
ground_rec = test_surfaece.get_rect(midbottom = (300,515))
fly = pygame.image.load('graphics/fly.png').convert_alpha()
fly_rec = fly.get_rect(midbottom = (720,150))
fly1 = pygame.image.load('graphics/fly.png').convert_alpha()
fly_rec1 = fly1.get_rect(midbottom = (720,150))
play = pygame.image.load('graphics/play.png').convert_alpha()
Play = pygame.transform.scale(play, (1000,200))
play_rec = Play.get_rect(midbottom = (337,400))

                              #Your text.If you want your text smooth. Colour
text_surface = test_font_score.render('You score is 0', True, 'Black')
text_surface = test_font_game_over.render('Game Over!', True, 'Black')
If_game_is_still_going = 'yes'
position = 680
while True:
    if play_or_not == False:
      if not t >= 1917:
        snail_rec.right -= 3
      if t >= 650:
        if not t >= 2034:
          fly_rec.right -= 3
      if t >= 1000:
        if not t >= 2107:
          fly_rec1.right -= 3
      if fly_rec.x < -150:
        fly_rec.x = 680
        
      if fly_rec1.x < -150:
        fly_rec1.x = 680
          
      if If_game_is_still_going == 'yes':
        t += 1
      text_surfacel = test_font_time.render(f'Score: {t}', True, 'Black')
      for event in pygame.event.get():
          if event.type == QUIT:
              pygame.quit()
              sys.exit()
          if event.type == KEYUP:
             if player_rec.colliderect(ground_rec):
               player_rec.y -= 200
            
      if snail_rec.x < -150:
        snail_rec.x = 680
      screen.blit(sky_surface,(0,0))
      #screen.blit(play,(play_rec))
      screen.blit(test_surfaece,(ground_rec))
      #screen.blit(lava_surface,(20,200)) 
      if If_game_is_still_going == 'no':
        screen.blit(text_surface,(150,150))
      if If_game_is_still_going == 'yes':
        if not t >= 1917:
          screen.blit(enemy_snail,(snail_rec))
        screen.blit(player,(player_rec))
        if not t >= 2034:
          screen.blit(fly,(fly_rec))
        if not t >= 2107:
          screen.blit(fly1,(fly_rec1))
      screen.blit(text_surfacel,(0,0))
      if player_rec.colliderect(snail_rec):
        If_game_is_still_going = 'no'
        print("snail")
      if player_rec.colliderect(fly_rec):
        If_game_is_still_going = 'no'
        print("fly")
      if player_rec.colliderect(fly_rec1):
        If_game_is_still_going = 'no'
        print("fly")
      
      
          
      if not player_rec.colliderect(ground_rec):
        player_rec.y += 1.9
      
      
    
      pygame.display.update()
      clock.tick(60)