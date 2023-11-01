""" Nagyon fontos, hogy a fájl neve ne turtle.py legyen, mert akkor ezt a hibaüzenetet fogod kapni:
AttributeError: partially initialized module 'turtle' has no attribute 'Turtle' (most likely due to a circular import). Did you mean: 'turtle'?"""

""" import turtle

t = turtle.Turtle()
t.forward(100)
t.right(90)
t.forward(100)
input()
 """
import turtle
import random

player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200, 100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200, -100)

player_one.goto(300, 60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200, 100)
player_two.goto(300, -140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200, -100)

die = [1, 2, 3, 4, 5, 6]

for i in range(20):
    if player_one.pos() >= (300, 100):
        print("Player One Wins!")
        break
    elif player_two.pos() >= (300, -100):
        print("Player Two Wins!")
        break
    else:
        player_one_turn = input("Press 'Enter' to roll the die ")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        player_one.fd(20*die_outcome)
        player_two_turn = input("Press 'Enter' to roll the die ")
        d = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        player_two.fd(20*die_outcome)