import turtle

def draw_square(size, color, sides):
    pen.color(color)
    for i in range(sides):
        pen.forward(size)
        pen.left(360/sides)

pen = turtle.Turtle()

draw_square(140, "red", 7)




turtle.mainloop()
    