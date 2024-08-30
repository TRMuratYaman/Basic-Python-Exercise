from turtle import Turtle,Screen
import random

# Set Up the Screen
screen = Screen()
screen.title("Catch the Turtle Game")
screen.setup(width=1920, height=1080)
screen.bgcolor("light blue")
FONT = ("Arial", 30, "normal")
score = 0
grid_size = 10
turtle_list = []
game_over = False

# Create Score Turtle
score_turtle = Turtle()

# Create Countdown turtle
countdown_turtle = Turtle()

# Set Score Turtle
def set_score_turtle():
   score_turtle.color("dark blue")
   score_turtle.hideturtle()
   score_turtle.penup()
   y = (screen.window_height() / 2) * 0.9
   score_turtle.goto(0, y)
   score_turtle.write(arg="Score:", move=False, align="center", font=FONT)


# Set Countd own Turtle
def set_countdown_turtle(time):
   global game_over
   countdown_turtle.color("dark blue")
   countdown_turtle.hideturtle()
   countdown_turtle.penup()
   y = (screen.window_height() / 2) * 0.9
   countdown_turtle.goto(0, y - 50)
   countdown_turtle.clear()

   if time > 0:
      countdown_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
      screen.ontimer(lambda : set_countdown_turtle(time - 1), 1000)
   else:
      game_over = True
      hide_turtles()
      countdown_turtle.clear()
      countdown_turtle.write(arg="Game Over !", move=False, align="center", font=FONT)


# Create Random Turtles
def make_random_turtles():

     for i in range(20):
        x = random.randint(-50, 50)
        y = random.randint(-50, 50)

        t = Turtle(shape="turtle")

        def click_turtle(x, y):
           global score
           score += 1
           score_turtle.clear()
           score_turtle.write(arg = f"Score: {score}", align="center", font=FONT)


        t.onclick(click_turtle)
        t.color("green")
        t.turtlesize(2)
        t.penup()
        t.goto(x * grid_size, y * grid_size)
        turtle_list.append(t)

# Hide the Turtles
def hide_turtles():
   for t in turtle_list:
      t.hideturtle()

# Show the Turtles Randomly
def show_turtles_randomly():
   if not game_over:
      hide_turtles()
      random.choice(turtle_list).showturtle()
      screen.ontimer(show_turtles_randomly, 500)

def game_start():
   screen.tracer(0)
   set_score_turtle()
   make_random_turtles()
   hide_turtles()
   show_turtles_randomly()
   set_countdown_turtle(10)
   screen.tracer(1)
   screen.mainloop()


game_start()