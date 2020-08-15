import turtle

t = turtle.Turtle()


# Function that draws a figure based on user input
def turtleFigure():
    actions = int(input("Please pick a number of actions for the turtle to do (individual lines): "))
    size = float(input("Please pick a number to scale the size of the drawing (decimals accepted): "))
    angle = float(input("Please choose the turning angle for the turtle in degrees (decimals accepted): "))
    turtleSize = float(input("Please choose the pen size (decimals accepted): "))
    turtleColor = input("Please pick a color for the turtle (hex values accepted): ")

    t.pensize(turtleSize)
    t.pencolor(turtleColor)

    for number in range(actions):
        t.forward(size)
        t.left(angle)
        t.forward(size)



# Function that draws a spiral based on user input
def turtleSpiral():
    actions = int(input("Please pick a number of actions for the turtle to do (individual lines): "))
    size = float(input("Please pick a number to scale the size of the drawing (decimals accepted): "))
    angle = float(input("Please choose the turning angle for the turtle in degrees (decimals accepted): "))
    turtleSize = float(input("Please choose the pen size (decimals accepted): "))
    turtleColor = input("Please pick a color for the turtle (hex values accepted): ")
    sizeMod = float(input("Please choose a number to increase the size by per action (decimals accepted): "))

    t.pensize(turtleSize)
    t.pencolor(turtleColor)

    for number in range(actions):
        size += sizeMod
        t.forward(size)
        t.left(angle)
        t.forward(size)

# The difference between figure and spiral is that spiral has the sizeMod property, increasing the size per action



# Loop that asks the user to pick between creating a figure or a spiral
while True:
    turtleShape = input("Please pick between figure/spiral to determine what the turtle will draw: ").lower()
    if turtleShape == "figure":
        turtleFigure()
        break
    elif turtleShape == "spiral":
        turtleSpiral()
        break
    else:
        print("Invalid choice")


input('Hit enter to end program')