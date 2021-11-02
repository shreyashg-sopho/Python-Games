import turtle
import math
import random
import os

#SET UP SCRREN
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("SPACE INVADERS")
wn.bgpic("space_invaders_background.gif")


#Register the names
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")


#SET BORDER
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
for side in range (4):
    border_pen.fd(600)
    border_pen.left(90)
border_pen.hideturtle()


#Set Score to 0
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290 , 280)
scorestring = "Score : %s" %score
score_pen.write(scorestring, False, align= "left", font =("Arial", 14, "normal"))
score_pen.hideturtle()


#CREATE THE PLAYER SHIP
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed=15



enemyspeed=2
#Choose the number of enemies
number_of_enemies =5
#Create an empth list
enemies =[]

#Add enemies into the list
for i in range (number_of_enemies):
    #Create Enemies
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x=random.randint(-200 , 200)
    y =random.randint(100, 250)//10 * 10
    enemy.setposition(x, y)

#CREATE THE SHOTS
shot = turtle.Turtle()
shot.color("yellow")
shot.shape("triangle")
shot.penup()
shot.speed(0)
shot.setheading(90)
shot.shapesize(0.5, 0.5)
shot.hideturtle()
shotspeed=30

#BULLET IS READY
#READY - ready to fire
#FIRE -bullet is firing
shotstate= "ready"

#MOVE THE PLAYER LEFT AND RIGHT
def move_left ():
    x  =  player.xcor()
    x -=  playerspeed
    if  x < -280:
        x=-280
    player.setx(x)

def move_right () :
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x= 280
    player.setx(x)

def fire_shot():
    #Declare bullet state as global if itneeds to be changed
    global shotstate
    if shotstate == "ready":
         shotstate = "fire"
         #Moving the shot just above the player
         x = player.xcor()
         y = player.ycor() + 10
         shot.setposition(x,y)
         shot.showturtle()

def isColission (t1,t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) +  math.pow( t1.ycor() - t2.ycor() , 2))
    if distance <= 20:
        return True
    else:
        return False


#CREATE KEYBOARD BINDINGS
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_shot , "space")


#MAIN GAME LOOP
while True:
    for enemy in enemies:
        #MOVE THE ENEMY
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #MOVE THE ENEMY SIDE AND DOWN WAYS
        if enemy.xcor() > 280:
            for  e in enemies:
            #Move all enemies down
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Change enemies direction
            enemyspeed *= -1
        if enemy.xcor() <-280:
            #MOve all enemies down
            for e in enemies:
                y=e.ycor()
                y -= 40
                e.sety(y)
            #Change enemies direction
            enemyspeed *= -1
        if isColission(shot, enemy):
            # RESET THE DHOT STATUS TO READY
            shot.hideturtle()
            shotstate = "ready"
            shot.setposition(0, -400)
            # Reset the enemy
            x = random.randint (-200, 200)
            y = (random.randint ( 100 , 250))//10 * 10
            enemy.setposition( x , y)
            #Update the enemy
            score += 10
            scorestring = "Score : %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        if isColission(enemy, player):
            player.hideturtle()
            enemy.hideturtle()
            print("GAME OVER")
            break

    #Moving the shot
    if shotstate== "fire":
        y = shot.ycor()
        y += shotspeed
        shot.sety(y)

    #CHECK IF THE SHOT HAS REACHED THE TOP
    if shot.ycor() > 275:
        shot.hideturtle()
        shotstate = "ready"






turtle.mainloop()
