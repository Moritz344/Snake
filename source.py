import pygame
import random
import time
import sys

pygame.init()

x = 800
y = 600
screen = pygame.display.set_mode((x,y))
clock = pygame.time.Clock()
pygame.display.set_caption("Snake")

# Farben
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,128,0)
blue = (0,0,255)
light_green = (144,238,144)
darker_green = (1,50,32)
light_dark = (50, 50, 50)
dark_green = (0,100,0)
dark_grey = (50,50,50)
dark_brown = (101,67,33)

# Snake
snake_block = 20
snake_x = x // 2
snake_y = y // 2
snake_speed = 6
snake_speed_max = 6 



snake_list = []
snake_len = 1
# 
direction = "RIGHT"
change_to = direction

# Text
pygame.font.init()
font = pygame.font.SysFont("Minecraft",36)
font_2 = pygame.font.SysFont("Minecraft",60)
font_3 = pygame.font.SysFont("Minecraft",20)

# Score System
score = 0

# bar
bar_x = 600
bar_y = 0

bar_width = 0 # 200
bar_height = 20 # 20



# food
foodx = random.randint(0,x) 
foody = random.randint(0,y)

#ui
def show_menu():
     menu = True
     while menu:
          screen.fill(light_dark)

          # mouse pos
          mouse = pygame.mouse.get_pos()

          # Text
          # collide box
          text_box = pygame.draw.rect(screen,light_green,[300,200,200,50])
          text_box = pygame.draw.rect(screen,light_dark,[300,200,200,50])

          # collision with text and different colors when hover
          if text_box.collidepoint(mouse):
               text_box = pygame.draw.rect(screen,light_dark,[300,200,200,50])
               start_text = font_2.render("Start",True,green)
          else:
               start_text = font_2.render("Start",True,white)

          dest = (300,200)
          screen.blit(start_text,dest)

          # <----

          credit_text_box = pygame.draw.rect(screen,light_dark,[300,360,250,50])

          if credit_text_box.collidepoint(mouse):
               credit_text = font_2.render("Credits",True,green)
          else:
               credit_text = font_2.render("Credits",True,white)


          dest_3 = (300,360)
          screen.blit(credit_text,dest_3)


          # <---          
          quit_text_box = pygame.draw.rect(screen,light_dark,[300,280,150,50])


          if quit_text_box.collidepoint(mouse):
               quit_text = font_2.render("Quit",True,green)
          else:
               quit_text = font_2.render("Quit",True,white)

          dest_2 = (300,280)
          screen.blit(quit_text,dest_2)
          # <----
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit() 
               if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                         menu = False
               if event.type == pygame.MOUSEBUTTONDOWN:
                    if text_box.collidepoint(event.pos):
                         menu = False
                    if quit_text_box.collidepoint(event.pos):
                         sys.exit(0)
                    if credit_text_box.collidepoint(event.pos):
                         print("CREDITS!!!")



              #screen.fill(black)
          pygame.display.update()
          clock.tick(60)


def movement():
          global snake_x,snake_y
          if change_to == "RIGHT":
               snake_x += snake_speed
          elif change_to == "LEFT":
               snake_x -= snake_speed
          elif change_to == "DOWN":
               snake_y += snake_speed
          elif change_to == "UP":
               snake_y -= snake_speed
def drawing_and_collision():
     global snake_len,score,foodx,foody,bar_width,snake_speed,snake_speed_max
     for i in snake_list:
          snake = pygame.draw.rect(screen,white,[i[0],i[1],snake_block,snake_block])
          if snake.colliderect(food):
                    
               #dest_2 = (250 ,300)
               #dest_3 = (275,370)
               foodx = random.randint(0,750)
               foody = random.randint(60,400)
               snake_len += 1
               score += 1
               bar_width += 20
               if bar_width == 200:
                    bar_width = 0
                    #if bar_width == 20 or bar_width == 60 or bar_width == 80 or bar_width == 100:
                         #snake_speed += 1
                         #if snake_speed > 8:
                              #snake_speed = 8 
                              #print("MAX SPEED!")


     

show_menu()

run = True
while run:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               run = False
          if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_d and direction != "LEFT":
                    change_to = "RIGHT"
               elif event.key == pygame.K_a and direction != "RIGHT":
                    change_to = "LEFT"
               elif event.key == pygame.K_w and direction != "DOWN":
                    change_to = "UP"
               elif event.key == pygame.K_s and direction != "UP":
                    change_to = "DOWN"
               elif event.key == pygame.K_ESCAPE:
                    menu = True
                    show_menu()
     screen.fill(dark_green)

     direction = change_to

    


     food = pygame.draw.rect(screen,red,[foodx,foody,20,20])

     # growing snake
     snake_head = [snake_x,snake_y]
     snake_list.append(snake_head)

     # Text
     score_text = font.render(f"Score: {score}",False,white)
     death_text = font_2.render("You died!",False,red)
     small_text = font_3.render("Press ESCAPE to quit",False,white)
     
     # bar
     #bar = pygame.draw.rect(screen,blue,[bar_x,bar_y,bar_width,bar_height])
     #outline = pygame.draw.rect(screen,white,[bar_x,bar_y,200,20],3)

     # collsion with itself
     for i in snake_list[:-1]:
          if i == snake_head:
               run = False
     # 
     if len(snake_list) > snake_len:
          del snake_list[0]

     if snake_x > 780:
         run = False 
     elif snake_x < 0:
          run = False
     if snake_y < 0:
          run = False
     elif snake_y > 590:
          run = False
     

     # drawing text
     dest = (5,0)
     dest_2 = (250 ,300)
     dest_3 = (275,370)
     screen.blit(score_text,dest)

     drawing_and_collision()
     movement()
     clock.tick(60) 
     pygame.display.update()
pygame.quit()