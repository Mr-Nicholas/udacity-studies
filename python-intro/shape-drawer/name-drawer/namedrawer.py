import turtle

# create an instance of Turtle to draw letters
drawer = turtle.Turtle()
drawer.shape("arrow")
drawer.color("black")
drawer.speed(0.5)

# create a function that instantialises the Turtle class
def draw_name():
    # creates the window
    window = turtle.Screen()
    window.bgcolor("yellow")

    # sets the start point
    set_startpoint()
    # calls the first letter to be drawn
    draw_letter("H")
    # sets startpoint of second letter
    set_secondpoint()
    # calls the second letter to be drawn
    draw_letter("G")

    window.exitonclick()

# sets the startpoint
def set_startpoint():
    drawer.penup()
    drawer.setposition(-100, 50)
    drawer.pendown()
    drawer.left(90)

def set_secondpoint():
    drawer.penup()
    drawer.setposition(0, 50)
    drawer.pendown()
    drawer.left(180)

# draw the letter H
def draw_letter(letter):
    if letter == "H":
        drawer.forward(100)
        drawer.back(50)
        drawer.right(90)
        drawer.forward(50)
        drawer.left(90)
        drawer.forward(50)
        drawer.right(180)
        drawer.forward(100)
    elif letter == "G":
        drawer.forward(100)
        drawer.right(90)
        drawer.forward(30)
        drawer.back(30)
        drawer.right(90)
        drawer.forward(100)
        drawer.left(90)
        drawer.forward(50)
        drawer.left(90)
        drawer.forward(30)
        drawer.left(90)
        drawer.forward(30)
        drawer.back(30)
    else:
        raise ValueError("Input is not the letter H or G")

# call the draw function
draw_name()
