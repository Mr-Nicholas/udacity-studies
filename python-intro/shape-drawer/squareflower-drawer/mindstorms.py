import turtle

'''
This simple program draws multiple geometric shapes using Python's Turtle Class
'''
def draw_shapes():
    # create a window for the graphics
    window = turtle.Screen()
    window.bgcolor("white")

    # create an instance of Turtle to draw a square
    heath = turtle.Turtle()
    heath.shape("turtle")
    heath.color('red')
    heath.speed(10)

    # create an instance of Turtle to draw a circle
    craig = turtle.Turtle()
    craig.shape("circle")
    craig.color("pink")
    craig.speed(4)

    # create an instance of Turtle to draw a circle
    sally = turtle.Turtle()
    sally.color("orange")
    sally.shape("arrow")

    # call the square method and rotate it to create a circle
    for i in range(36):
        draw_square(heath)
        heath.left(10)
    
    
    # uncomment the below to draw a circle or triangle with an additional instance
    # craig.circle(100)
    # draw_triangle(sally)

    window.exitonclick()
    
def draw_square(turtle_name):
    # while loop draws the square
    count = 0
    while (count < 4):
        turtle_name.forward(100)
        turtle_name.right(90)
        count += 1
        
def draw_triangle(turtle_name):
    turtle_name.forward(100)
    turtle_name.left(90)
    turtle_name.forward(100)
    turtle_name.left(135)
    turtle_name.forward(140)

# calls the shapes to be drawn    
draw_shapes()
