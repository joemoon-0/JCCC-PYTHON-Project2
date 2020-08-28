##
# Joe Moon
# PROJECT - Using Turtle and our class examples, create a program with the following components:
# 1 - Window is at least 300x300
# 2 - Title of window is "Last Python Project"
# 3 - 3 objects of class turtle are created
# 4 - Each object has 1 keyboard.
# 5 - Each object has 1 other event implemented.
# 6 - Each object is a different color
# 7 - Each object's keyboard, other event, and color change must be different from the other objects
# 8 - Clear will clear the screen

'''   INSTRUCTIONS
** OBJECTIVE: Get the turtle through the aperture and onto the bulls-eye **

turtle1 = Power Bar / Launch Button
>> Key: "space" = commence launch
>> Drag: select launch strength

turtle2 = Launch Object Manipulation
>> Key: "left" and "right" arrows = adjust launch angle
>> Drag: adjust elevation

turtle3 = Apperature
>> Key: open/close the apperature
>> Drag: adjust positioning
'''

import turtle

''' Global Variables '''
powerLevel = 50      # Launch power
turtleHeight = 0     # Initial launch height
launchVector = 90    # Initial launch angle
xHole = 0            # X-coord for aperture
yHole = 0            # Y-coord for aperture
appState = 0         # Aperture open/close state

def main(): 
   interface()       # Create user interface
   instructions()    # Print instructions

   # Position the turtles
   turtle1.penup()
   turtle1.setposition(0, 120)
   turtle1.left(90)
   turtle1.pendown()   
   turtle2.penup()
   turtle2.setposition(-110, -100)
   turtle2.left(90)
   turtle2.pendown()   
   
   # Modify the turtles' features
   turtle1.color("black", "red")
   turtle1.shape("classic")   
   turtle1.resizemode("user")
   turtle1.shapesize(2, 2)   
   
   turtle2.color("white", "green")
   turtle2.shape("turtle")   
   turtle2.resizemode("user")
   turtle2.shapesize(1, 1)      
 
   turtle3.color("black", "black")
   turtle3.shape("circle")
   turtle3.resizemode("user")
   turtle3.shapesize(2, 2, 3)      
      
   
   # Bind the events
   turtle1.ondrag(adjustPower, 1)
   turtle2.ondrag(adjustturtleHeight, 1)
   turtle3.ondrag(adjustApp, 1)
   
   win.onkey(leftTilt, "Left")      # turtle2 - Tilt turtle upward (left)
   win.onkey(rightTilt, "Right")    # turtle2 - Tilt turtle downward (right)
   win.onkey(openApp, "Up")         # turtle3 - Open apperature
   win.onkey(closeApp, "Down")      # turtle3 - Close apperature
   win.onkey(launch, "space")       # turtle1 - Initiate launch
   win.onkey(clearScreen, "c")      # Clears the screen
   
   # Tell window to listen to events
   win.listen()
   
   # Wait for user to close window
   win.mainloop()   

def setWindow():
   WIN_WIDTH = 400
   WIN_HEIGHT = 450
   turtle.setup(WIN_WIDTH, WIN_HEIGHT)   
   win = turtle.Screen()
   win.title("LAST PYTHON PROJECT")
   
   return win

def clearScreen():
   win.clearscreen()

def interface():
   control.speed(100)
   control.hideturtle()

   ''' Create Power Bar
   Power Bar is positioned between x-coords: -120 to 120
   Locked on y-coord: 125
   '''
   control.left(90)
   control.penup()
   control.color("black")
   control.pensize(2)
   powerColor = ["blue", "blue violet", "violet", "yellow", "orange", "red"]

   for i in range(0,6):
      control.fillcolor(powerColor[i])
      control.penup()
      control.setposition(-120 + 40 * i, 125)
      control.pendown()
      control.begin_fill()
      control.right(90)
      control.forward(40)
      control.left(90)
      control.forward(10)
      control.left(90)
      control.forward(40)
      control.left(90)      
      control.forward(10)   
      control.end_fill()
      control.right(180)      # reorientate for each box
   
   ''' Create Launch Post
   Launch Post is positioned between y-coords: -120 to 30
   Locked on x-coord: -130
   '''
   control.penup()
   control.setposition(-130, -120)
   control.color("black")
   control.pensize(2)
   control.pendown()
   control.forward(150)
   
   control.right(90)   
   for i in range(0,6):       # Launch bar hash marks
      control.penup()
      control.setposition(-130, -120 + 30 * i)
      control.pendown()
      control.forward(5)
      
   ''' Create Bulls-eye: Landing zone target area
   Centered on (90, -90)
   '''
   bullsColors = ["blue", "white", "red"]
   
   for i in range(0,3):
      control.fillcolor(bullsColors[i])
      control.penup()
      control.setposition(90, -120 + i * 10)
      control.pendown()      
      control.begin_fill()
      control.circle(30 - i * 10)
      control.end_fill()

   ''' Create Backboard: Restraint area for hole ''' 
   control.penup()
   control.setposition(50, -25)
   control.pendown()
   control.fillcolor("brown")
   control.begin_fill()
   for i in range(0,4):
      control.left(90)
      control.forward(100)
   control.end_fill()

def instructions():
   control.penup()
   control.setposition(-120, 135)
   control.write("- 0 ------- POWER METER ------- 100 -", False, "left", ("Arial",14,"bold"))
   
   control.penup()
   control.setposition(-180, -140)
   control.write("OBJECTIVE: Get the turtle through the OPEN apperature and onto the bulls-eye", False, "left", ("Arial",9,"normal"))   

   control.penup()
   control.setposition(-180, -150)
   control.write(">> UP and DOWN arrows open (white) and close (black) the apperature", False, "left", ("Arial",9,"normal"))   

   control.penup()
   control.setposition(-180, -160)
   control.write(">> Drag the apperature to reposition it within the brown board", False, "left", ("Arial",9,"normal"))

   control.penup()
   control.setposition(-180, -170)
   control.write(">> LEFT and RIGHT arrows adjust the turtle's launch angle", False, "left", ("Arial",9,"normal"))
   
   control.penup()
   control.setposition(-180, -180)
   control.write(">> Drag the RED ARROW to adjust the power meter", False, "left", ("Arial",9,"normal"))

   control.penup()
   control.setposition(-180, -190)
   control.write(">> Drag the TURTLE to adjust the launch height", False, "left", ("Arial",9,"normal"))
   
   control.penup()
   control.setposition(-180, -200)
   control.write(">> SPACE BAR initiates the launch!", False, "left", ("Arial",9,"normal"))      
   
def adjustPower(x, y):
   ''' Translates x-coord of turtle1 into a percentage for trajectory calculations '''
   global powerLevel
   turtle1.penup()
   
   # confine adjustment arrow within power bar x-coords
   if x < -120:
      x = -120
   elif x > 120:
      x = 120
   
   turtle1.goto(x, 120)    # lock turtle1 y-coord
   
   powerLevel = ((x + 120) / 240) * 100  # convert x-coord into percentage
   #print("Power Level: ", powerLevel) 
   
def adjustturtleHeight(x, y):
   ''' Translates y-coord of turtle2 for trajectory calculations '''
   global turtleHeight
   turtle2.penup()
   
   # confine pad height within launch post y-coords
   if y < -120:
      y = -120
   elif y > 30:
      y = 30
   
   turtle2.goto(-110, y)  # lock turtle2 x-coord
   turtleHeight = y                 # store globally
   #print("Pad Height: ", turtleHeight)

def leftTilt():
   global launchVector
   launchVector += 3
   #print("Launch Vector: ", launchVector)
   
   # restrict upper launch angle
   if launchVector > 90:
      launchVector = 90
   else:
      turtle2.left(3)
   
def rightTilt():
   global launchVector
   launchVector -= 3
   #print("Launch Vector: ", launchVector)
   
   # restrict lower launch angle
   if launchVector < -30:
      launchVector = -30
   else:   
      turtle2.right(3)

def adjustApp(x, y):
   ''' Allows movement of the apperature within the constraints of the brown backboard.  Globally returns x and y coordinates on which the apperature is positioned on. '''
   global xHole, yHole
   
   # contain within x-coord of box
   if x < -30:
      x = -30
   elif x > 29:
      x = 29
   
   # contain within y-coord of box
   if y > 55:
      y = 55
   elif y < -4:
      y = -4
      
   xHole = x
   yHole = y
   turtle3.penup()
   turtle3.goto(x, y)

def openApp():
   global appState
   turtle3.fillcolor("white")
   appState = 1      # Apperature opened

def closeApp():
   global appState
   turtle3.fillcolor("black")
   appState = 0      # Apperature closed

def launch():
   global powerLevel, turtleHeight, launchVector, xHole, yHole, appState
   
   # Announce Launch
   turtle1.hideturtle()
   turtle1.penup()
   turtle1.setposition(0, 90)
   turtle1.pendown()
   turtle1.write("LAUNCHING TURTLE!", False, "center", ("Arial",16,"bold"))
   
   ''' CALCULATION VARIABLES
   Turtle x-coord is: -110
   Bulls-eye is centered at: (90, -90)
   The apperature is centered at: (xHole, yHole)
   '''  
   turtle2.penup()
   apperature = False   # Did the turtle go through the apperature?
   bullsEye = False     # Did the turtle land on the bulls-eye?
   
   ''' WHILE loop allows movement so long as turtle is within allowable area '''
   while turtle2.xcor() < 110 and turtle2.ycor() > -110: # extreme limits
      turtle2.forward(1)            # Perpetual motion
      
      if powerLevel > 0:   # Extra boost from power level
         turtle2.right(0)
         powerLevel -= 1
      elif turtle2.heading() > 90 and turtle2.heading() < 280:
         turtle2.right(0)        # Prevents turtle from circling on itself
      else:
         turtle2.right(0.75)           # Gravitational decline
      
      variance = 6   # Tolerance for target area
      xAppUpper = xHole + variance
      xAppLower = xHole - variance
      yAppUpper = yHole + variance
      yAppLower = yHole - variance  
      xBullUpper = 80 + variance
      xBullLower = 80 - variance
      yBullUpper = -90 + variance
      yBullLower = -90 - variance
      
      if turtle2.xcor() >= xAppLower and turtle2.xcor() <= xAppUpper and turtle2.ycor() >= yAppLower and turtle2.ycor() <= yAppUpper:
         if appState == 1:
            apperature = True  # Turtle made it through the open apperature
         else:
            endGame(0)     # Apperature was not opened
      elif turtle2.xcor() > xAppUpper + variance and apperature == False:
         endGame(0)        # Turtle misses the apperature
         break
      elif turtle2.ycor() < -100 and bullsEye == False:
         endGame(0)        # Turtle misses the bulls-eye
         break
      elif turtle2.xcor() >= xBullLower and turtle2.xcor() <= xBullUpper and turtle2.ycor() >= yBullLower and turtle2.ycor() <= yBullUpper:
         bullsEye = True       # Turtle made it onto the bulls-eye
      
      # Win condition      
      if apperature and bullsEye:
         endGame(1)
         break

def endGame(result):
   if result == 1:         # Successful landing
      win.clearscreen()
      win.bgcolor("blue")
      turtle1.color("yellow")
      turtle1.write("Your turtle made it!", False, "center", ("Arial",18,"bold"))   
   else:                   # Turtle's demise
      win.clearscreen()
      win.bgcolor("red")
      turtle1.color("white")
      turtle1.write("Your turtle didn't make it!", False, "center", ("Arial",16,"bold"))
   

# Configure the window, create turtles, and run the program
win = setWindow()
turtle1 = turtle.Turtle()  # Power bar and Launch button
turtle2 = turtle.Turtle()  # Turtle shaped object to be launched
turtle3 = turtle.Turtle()  # Barrier control
control = turtle.Turtle()  # General user interface
main()