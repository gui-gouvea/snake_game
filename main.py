from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

# Setting up the screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# creating the snake from the class:
snake = Snake()
# creating the food from the Food class
food = Food()
# creating the scoreboard and displaying the current score
score = Scoreboard()

# Moving the snake across the screen, while user changes the direction
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

game_is_on = True
while game_is_on:
    screen.update()  # Refreshes the screen
    time.sleep(0.1)  # delays the screen update
    snake.move()

    # detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.adding_score()

    # Detecting collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() <-290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    # Detecting if the snake collides with the body. If the snakes collides with the body, game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
