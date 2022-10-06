#Ping Pong game
import turtle

#Screen  t
t = turtle.Screen()
t.title("Ping Pong")
t.setup( width = 1000, height = 600)

#Light or Dark Mode
info = turtle.textinput("Dark Mode","Y/N")
if info == "Y":
    pad_col = "white"
    scr_col = "black"
    ball_col = "cyan"
else:
    pad_col = "black"
    scr_col = "white"
    ball_col = "red"
    
t.bgcolor(scr_col)  


#Right Paddle  rp
rp = turtle.Turtle()
rp.speed(0)
rp.shape("square")
rp.shapesize(stretch_wid=5, stretch_len=1)
rp.color(pad_col)
rp.penup()
rp.goto(400, 0)


#Left Paddle  lp
lp = turtle.Turtle()
lp.speed(0)
lp.shape("square")
lp.shapesize(stretch_wid=5, stretch_len=1)
lp.color(pad_col)
lp.penup()
lp.goto(-400, 0)


#Ball bl
bl = turtle.Turtle()
bl.speed(40)
bl.shape("circle")
bl.color(ball_col)
bl.penup()
bl.goto(0,0)
bl.dx = 5
bl.dy = -5


#Score
left_ply = 0
right_ply = 0

#Score Board sb
sb= turtle.Turtle()
sb.speed(0)
sb.color("blue")
sb.penup()
sb.hideturtle()
sb.goto(0, 260)
sb.write("Left Player : 0     RightPlayer : 0", align = "center", font=("Courier",15,"normal"))



#Paddle Move pd
def lpup():
    a = lp.ycor()
    a += 20
    lp.sety(a)

def lpdown():
    a = lp.ycor()
    a -= 20
    lp.sety(a)

def rpup():
    a = rp.ycor()
    a += 20
    rp.sety(a)

def rpdown():
    a = rp.ycor()
    a -= 20
    rp.sety(a)


#Keys
t.listen()
t.onkeypress(lpup, "w")
t.onkeypress(lpdown, "s")
t.onkeypress(rpup, "Up")
t.onkeypress(rpdown, "Down")

while True:
    t.update()
    bl.setx(bl.xcor()+bl.dx)
    bl.sety(bl.ycor()+bl.dy)

    #Boundary
    #Vertical
    if bl.ycor() > 300:
        bl.sety(300)
        bl.dy *= -1

    if bl.ycor() < -300:
        bl.sety(-300)
        bl.dy *= -1

    #Horizontal
    if bl.xcor() > 500:
        bl.goto(0,0)
        bl.dy *= -1
        left_ply += 1
        sb.clear()
        sb.write("Left Player : {}     RightPlayer : {}".format(left_ply, right_ply),
                 align = "center", font=("Courier",15,"normal"))

    if bl.xcor() < -500:
        bl.goto(0,0)
        bl.dy *= -1
        right_ply += 1
        sb.clear()
        sb.write("Left Player : {}     RightPlayer : {}".format(left_ply, right_ply),
                 align = "center", font=("Courier",15,"normal"))
        
    
    #Paddle collision with ball
    if(bl.xcor() > 360 and bl.xcor() < 370 )and (bl.ycor() < rp.ycor()+40 and bl.ycor()> rp.ycor()-40):
        bl.setx(360)
        bl.dx *= -1

    if(bl.xcor() < -360 and bl.xcor() > -370 )and (bl.ycor() < lp.ycor()+40 and bl.ycor()> lp.ycor()-40):
        bl.setx(-360)
        bl.dx *= -1
    

    

