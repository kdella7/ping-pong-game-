#imported turtle module
import turtle

wind=turtle.Screen() # inthialize screen
wind.title('ping pong by khaled ')#set the title of the window
wind.setup(width=800,height=600)#set the dimention
wind.bgcolor('black')#set screen colour
wind.tracer(0)#stops the window from automaticly update

#paddle1
paddle1=turtle.Turtle()#intialize turtle object
paddle1.speed(0) #set the speed
paddle1.shape('square')#set the shape
paddle1.shapesize(stretch_len=1,stretch_wid=5)#strech the shape to meet the size
paddle1.color('blue')#set the couler
paddle1.penup()#stops the object from drawing lines
paddle1.goto(-350,0)#set the dimention of the object
# paddle2
paddle2=turtle.Turtle()
paddle2.speed(0)
paddle2.color('red')
paddle2.shape('square')
paddle2.shapesize(stretch_wid=5,stretch_len=1)
paddle2.penup()
paddle2.goto(350,0)
#ball
ball=turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.speed(0)
ball.penup()
ball.goto(0,0)
ball.dx=0.3
ball.dy=0.3

#score 
score1=0
score2=0
score =turtle.Turtle()
score.speed=(0)
score.color('white')
score.hideturtle()
score.penup()
score.goto(0,260)
score.write('player1: 0  player2: 0', align='center',font =('Courier',24,'normal'))

#functions
#the first baddle
def paddle1_up ():
    y=paddle1.ycor()#get y coordonate of paddle1
    y+=20           #set y to increase by 20
    paddle1.sety(y) #set the y of new coordonate    
def paddle1_down():
    y=paddle1.ycor()
    y-=20           #set the y to decrease by 20
    paddle1.sety(y)
    
#the second paddle 
def paddle2_up():
    y=paddle2.ycor()
    y+=20
    paddle2.sety(y)
def paddle2_down():
    y=paddle2.ycor()
    y-=20
    paddle2.sety(y) 
       
#key binding
wind.listen() #told window to expect input 
#up first paddles
wind.onkeypress(paddle1_up,'w') #when pressed w paddle1 will invoke
#down first paddle
wind.onkeypress(paddle1_down,'s')
#up second paddle
wind.onkeypress(paddle2_up,'Up')
##down second paddle
wind. onkeypress(paddle2_down,'Down')


while True: #main game loop
    wind.update() #update the game every time the loop runs
#move the ball    
    ball.setx(ball.xcor()+ball.dx)# ball starts at 0 every time and every time loops run --->1 in xaxis
    ball.sety(ball.ycor()+ball.dy)# ball starts at 0 every time and every time loops run --->1 in yaxis

#border check  top border=300 pixel , buttom border =-300 pixel , ball is 20 pixel
    if ball.ycor()>290: #if ball is at top border
        ball.sety(290)#set y cordonate at 290
        ball.dy*=-1 # reverse direction of the ball
        
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    
    if ball.xcor()>390: # if ball is at right border
        ball.goto(0,0) #return ball to the center
        ball.dx*=-1    #reverse x  ball direction
        score1+=1
        score.clear()
        score.write('player1: {}  player2: {}'.format(score1,score2), align='center',font =('Courier',24,'normal'))
    
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1 
        score2+=1
        score.clear()  
        score.write('player1: {}  player2: {}'.format(score1,score2), align='center',font =('Courier',24,'normal'))
        
    #collision betwwen ball and paddele
    if (ball.xcor()>340 and ball.xcor()<350) and( ball.ycor()<paddle2.ycor()+40 and ball.ycor()>paddle2.ycor()-40):
        ball.setx(340)
        ball.dx*=-1
     
    if (ball.xcor()<-340 and ball.xcor()>-350) and( ball.ycor()<paddle1.ycor()+40 and ball.ycor()>paddle1.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1
       
    
