#Setup
import turtle as trtl
trtl.clearscreen()

screen = trtl.Screen()
trtl.title("Tic Tac Toe")
screen.setup(800,800)

turnCount = 0
XandO = ['none','none','none','none','none','none','none','none','none']
text_style = ("Arial", 100, "bold")
winner_text_style = ("Arial", 24, "bold")
gameOver = False
#Create boxes for Xs and Os

box0 = trtl.Turtle()
box0.speed(0)
box0.penup()
box0.color('white')
box0.shape('square')
box0.turtlesize(6.5)
box0.goto(-133.2,133.2)

box1 = trtl.Turtle()
box1.speed(0)
box1.penup()
box1.color('white')
box1.shape('square')
box1.turtlesize(6.5)
box1.goto(0,133.2)

box2 = trtl.Turtle()
box2.speed(0)
box2.penup()
box2.color('white')
box2.shape('square')
box2.turtlesize(6.5)
box2.goto(133.2,133.2)

box3 = trtl.Turtle()
box3.speed(0)
box3.penup()
box3.color('white')
box3.shape('square')
box3.turtlesize(6.5)
box3.goto(-133.2,0)

box4 = trtl.Turtle()
box4.speed(0)
box4.penup()
box4.color('white')
box4.shape('square')
box4.turtlesize(6.5)

box5 = trtl.Turtle()
box5.speed(0)
box5.penup()
box5.color('white')
box5.shape('square')
box5.turtlesize(6.5)
box5.goto(133.2, 0)

box6 = trtl.Turtle()
box6.speed(0)
box6.penup()
box6.color('white')
box6.shape('square')
box6.turtlesize(6.5)
box6.goto(-133.2,-133.2)

box7 = trtl.Turtle()
box7.speed(0)
box7.penup()
box7.color('white')
box7.shape('square')
box7.turtlesize(6.5)
box7.goto(0,-133.2)

box8 = trtl.Turtle()
box8.speed(0)
box8.penup()
box8.color('white')
box8.shape('square')
box8.turtlesize(6.5)
box8.goto(133.2,-133.2)

#Def Functions
def drawLines():
  count = 0
  while count < 2:
    count += 1
    grid.penup()
    if count == 1:
      grid.backward(66.6)
    else:
      grid.forward(133.3)
    grid.left(90)
    grid.pendown()
    grid.forward(200)
    grid.backward(400)
    grid.forward(200)
    grid.penup()
    grid.right(90)

'''
Grid Layout:

012
345
678
'''

def drawXandO(x,y):
  global turnCount
  global XandO
  global gameOver
  if turnCount % 2 == 0:
    marker = 'X'
  else:
    marker = "O"
  if not gameOver:
    if y >= 69:
      if x <= -69:
        box0.hideturtle()
        if marker == 'X':
          box0.color('red')
        else:
          box0.color('blue')
        box0.backward(50)
        box0.right(90)
        box0.forward(75)
        box0.left(90)
        box0.write(marker, font = text_style)
        XandO[0] = marker
      elif x >= 69:
        box2.hideturtle()
        if marker == 'X':
          box2.color('red')
        else:
          box2.color('blue')
        box2.backward(50)
        box2.right(90)
        box2.forward(75)
        box2.left(90)
        box2.write(marker, font = text_style)
        XandO[2] = marker
      else:
        box1.hideturtle()
        if marker == 'X':
          box1.color('red')
        else:
          box1.color('blue')
        box1.backward(50)
        box1.right(90)
        box1.forward(75)
        box1.left(90)
        box1.write(marker, font = text_style)
        XandO[1] = marker
    elif y <= -69:
      if x <= -69:
        box6.hideturtle()
        if marker == 'X':
          box6.color('red')
        else:
          box6.color('blue')
        box6.backward(50)
        box6.right(90)
        box6.forward(75)
        box6.left(90)
        box6.write(marker, font = text_style)
        XandO[6] = marker
      elif x >= 69:
        box8.hideturtle()
        if marker == 'X':
          box8.color('red')
        else:
          box8.color('blue')
        box8.backward(50)
        box8.right(90)
        box8.forward(75)
        box8.left(90)
        box8.write(marker, font = text_style)
        XandO[8] = marker
      else:
        box7.hideturtle()
        if marker == 'X':
          box7.color('red')
        else:
          box7.color('blue')
        box7.backward(50)
        box7.right(90)
        box7.forward(75)
        box7.left(90)
        box7.write(marker, font = text_style)
        XandO[7] = marker
    else:
      if x <= -69:
        box3.hideturtle()
        if marker == 'X':
          box3.color('red')
        else:
          box3.color('blue')
        box3.backward(50)
        box3.right(90)
        box3.forward(75)
        box3.left(90)
        box3.write(marker, font = text_style)
        XandO[3] = marker
      elif x >= 69:
        box5.hideturtle()
        if marker == 'X':
          box5.color('red')
        else:
          box5.color('blue')
        box5.backward(50)
        box5.right(90)
        box5.forward(75)
        box5.left(90)
        box5.write(marker, font = text_style)
        XandO[5] = marker
      else:
        box4.hideturtle()
        if marker == 'X':
          box4.color('red')
        else:
          box4.color('blue')
        box4.backward(50)
        box4.right(90)
        box4.forward(75)
        box4.left(90)
        box4.write(marker, font = text_style)
        XandO[4] = marker
    turnCount += 1
    winCondition()

def winCondition():
  global gameOver
  #Top Row
  if XandO[0] == XandO[1] and XandO[0] == XandO[2]:
    if XandO[0] == 'X':
      gameOver = True
      drawVictoryLine(-200,138, 'red')
      declareWinner("X")
    elif XandO[0] == 'O':
      gameOver = True
      drawVictoryLine(-200,138, 'blue')
      declareWinner("O")
  #Middle Row
  if XandO[3] == XandO[4] and XandO[3] == XandO[5]:
    if XandO[3] == 'X':
      gameOver = True
      drawVictoryLine(-200,5, 'red')
      declareWinner("X")
    elif XandO[3] == 'O':
      gameOver = True
      drawVictoryLine(-200,5, 'blue')
      declareWinner("O")
  #Bottom Row
  if XandO[6] == XandO[7] and XandO[6] == XandO[8]:
    if XandO[6] == 'X':
      gameOver = True
      drawVictoryLine(-200,-130, 'red')
      declareWinner("X")
    elif XandO[6] == 'O':
      gameOver = True
      drawVictoryLine(-200,-130, 'blue')
      declareWinner("O")
  #Left Column
  if XandO[0] == XandO[3] and XandO[0] == XandO[6]:
    if XandO[0] == 'X':
      gameOver = True
      declareWinner("X")
      drawVictoryLine(-140,200, 'red')
    elif XandO[0] == 'O':
      gameOver = True
      drawVictoryLine(-140,200, 'blue')
      declareWinner("O")
  #Middle Column
  if XandO[1] == XandO[4] and XandO[1] == XandO[7]:
    if XandO[1] == 'X':
      gameOver = True
      declareWinner("X")
      drawVictoryLine(-7.5,180, 'red')
    elif XandO[1] == 'O':
      gameOver = True
      drawVictoryLine(-7.5,180, 'blue')
      declareWinner("O")
  #Right Column
  if XandO[2] == XandO[5] and XandO[2] == XandO[8]:
    if XandO[2] == 'X':
      gameOver = True
      declareWinner("X")
      drawVictoryLine(125,200, 'red')
    elif XandO[2] == 'O':
      gameOver = True
      declareWinner("O")
      drawVictoryLine(125,200, 'blue')
  #Top Left to Bottom Right Diagonal
  if XandO[0] == XandO[4] and XandO[0] == XandO[8]:
    if XandO[0] == 'X':
      gameOver = True
      declareWinner("X")
      drawVictoryLine(-195,195, 'red')
    elif XandO[0] == 'O':
      gameOver = True
      drawVictoryLine(-195,195, 'blue')
      declareWinner("O")
  #Bottom Left to Top Right Diagonal
  if XandO[2] == XandO[4] and XandO[2] == XandO[6]:
    if XandO[2] == 'X':
      gameOver = True
      drawVictoryLine(-200,-195, 'red')
      declareWinner("X")
    elif XandO[2] == 'O':
      gameOver = True
      drawVictoryLine(-200,-195, 'blue')
      declareWinner("O")

def drawVictoryLine(x,y,color):
  victoryLine = trtl.Turtle()
  victoryLine.hideturtle()
  victoryLine.penup()
  victoryLine.goto(x,y)
  victoryLine.color(color)
  victoryLine.pensize(5)
  victoryLine.pendown()
  if y == 200:
    victoryLine.right(90)
    victoryLine.forward(400)
  elif y == -195:
    victoryLine.left(45)
    victoryLine.forward(550)
  elif y == 195:
    victoryLine.right(45)
    victoryLine.forward(550)
  elif y == 180:
    victoryLine.right(90)
    victoryLine.forward(380)
  else:
    victoryLine.forward(400)
  


def declareWinner(winner):
  winnerWriter = trtl.Turtle()
  winnerWriter.hideturtle()
  winnerWriter.color('purple')
  winnerWriter.penup()
  winnerWriter.goto(-53, 180)
  winnerWriter.write(winner + " WINS", font=winner_text_style)

#Draw Grid
grid = trtl.Turtle()
grid.speed(0)
grid.hideturtle()
grid.pensize(3)
drawLines()
grid.goto(0,0)
grid.left(90)
drawLines()

#Click boxes
box0.onclick(drawXandO)
box1.onclick(drawXandO)
box2.onclick(drawXandO)
box3.onclick(drawXandO)
box4.onclick(drawXandO)
box5.onclick(drawXandO)
box6.onclick(drawXandO)
box7.onclick(drawXandO)
box8.onclick(drawXandO)

trtl.Screen().mainloop()