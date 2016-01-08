import turtle

def draw_shape(turtle_name):
    for i in range(1,5):
        turtle_name.forward(100)
        turtle_name.right(70)
        turtle_name.forward(30)
        turtle_name.right(200)
        turtle_name.forward(150)
        
def draw_misc(): 
    window=turtle.Screen()
    window.bgcolor("orange")

    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.speed(50)
    for i in range (1,37):
        draw_shape(brad)
        brad.right(10)
        
    
    window.exitonclick()


draw_misc()
