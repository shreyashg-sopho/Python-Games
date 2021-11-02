import pygame
import random

score=0
red= (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black=(0,0,0)
grey=(175,175,175)
white=(255,255,255)

pygame.init()



display_width=1000
display_height=400
dino_y_default=260
dino_max=160
dino_x=100
dino_y = dino_y_default
dino_width=40
dino_height=40
flag = 0
tree_x=display_width
tree_y=260
tree_width=20
tree_height=40
move_speed = -10
tree_count=0

tree_x_1 = display_width + 450
tree_width_1=30
tree_height_1= 30
tree_y_1 = 270


bird_x = display_width + 750
bird_width = 25
bird_height=15
bird_y = 240


blackline_y=300
dino_y_change=0
change_height=10
FPS = 30


def ifColission (object_x, object_y,object_width , object_height , dino_x, dino_y, dino_height , dino_width):
   print("incollision")
   if (object_x <=dino_x + dino_width  and  object_x >= dino_x) or (object_x + object_width <= dino_x + dino_width and object_x+ object_width >=dino_x):
     print("pass 1 cleared")
     if ( object_y <= dino_y + dino_width  and object_y >= dino_y) or ( object_y + object_height <= dino_y + dino_width  and object_y >= dino_y):
         print("pass 2 cleared")
         global gameexit
         gameexit = True


clock=pygame.time.Clock()
gamedisplay = pygame.display.set_mode ((display_width, display_height))
gameexit=False

while not gameexit:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           gameexit= True
       elif event.type == pygame.KEYDOWN:
           if event.key == pygame.K_SPACE:
               if  dino_y == dino_y_default :
                  dino_y_change =  -change_height
           if dino_y_change == 0:
               if event.key == pygame.K_DOWN:
                      flag =0
                      dino_y = dino_y + dino_height/2
                      dino_height = dino_height / 2
                      print( "DOWN", dino_y , dino_height)

       elif event.type == pygame.KEYUP:
           if flag == 0:
               if event.key == pygame.K_DOWN:
                      dino_height = dino_height * 2
                      dino_y = dino_y - dino_height/2
                      flag=1
                      print("UP  ", dino_y, dino_height)
                      print("\n")


   if dino_y == dino_max:
       dino_y_change = change_height
   if dino_y == dino_y_default and dino_y_change > 0:
       dino_y_change = 0


   if tree_x < 0:
       tree_x= random.randrange(display_width, display_width + 200)
       tree_count= tree_count+1
       if tree_count%5 == 4:
            move_speed += -1

   if tree_x_1 < 0 and bird_x <0:
       random_variable = random.randint(0,10)
       if random_variable == 5:
           bird_x = random.randrange( tree_x + 400 ,  tree_x + 700)
           bird_y = random.randrange (235, 290)
       else:
           tree_x_1= random.randrange(tree_x  + 400 , tree_x + 700)
           tree_count= tree_count+1

   tree_x += move_speed
   tree_x_1 += move_speed
   bird_x += move_speed
   dino_y += dino_y_change

   gamedisplay.fill(white)
   gamedisplay.fill(grey, rect=[dino_x, dino_y ,dino_width, dino_height])
   gamedisplay.fill(grey, rect=[tree_x, tree_y, tree_width, tree_height])
   gamedisplay.fill(grey, rect=[tree_x_1, tree_y_1 , tree_width_1, tree_height_1])
   gamedisplay.fill(red, rect=[bird_x, bird_y, bird_width, bird_height])
   pygame.draw.line(gamedisplay, black, (0,blackline_y),(display_width,blackline_y))
   pygame.display.update()
   score = score+1

   ifColission(tree_x, tree_y, tree_width, tree_height,dino_x, dino_y ,dino_width, dino_height)
   ifColission(tree_x_1, tree_y_1, tree_width_1, tree_height_1, dino_x, dino_y, dino_width, dino_height)
   ifColission(bird_x, bird_y, bird_width, bird_height, dino_x, dino_y, dino_width, dino_height)



   clock.tick(FPS)
pygame.quit()
