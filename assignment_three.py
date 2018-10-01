# Flint Eller
# 9/24/18
# This program draws a flower based on user input

import turtle


def get_length_hexagon():
    """
    asks user the length of the hexagon
    :return: side length
    """
    length = float(input("What is the side length of the hexagon?"))
    return length


def get_petal_color():
    """
    asks user the petal color
    :return: petal color
    """
    petal_color = input("What color should the flower petals be?")
    return petal_color


def get_center_color():
    """
    asks user center color
    :return: center color
    """
    center_color = input("What color should the center of the flower be?")
    return center_color


def draw_hex(length, color):
    """
    draws a hexagon with side length and color chosen by user
    :param length:
    :param color:
    :return:
    """
    turtle.color(color)
    turtle.begin_fill()
    for x in range(6):
        turtle.forward(length)
        turtle.right(60)
    turtle.end_fill()


def draw_flower():
    """
    Draws side six hexagons as petals around one hexagon in center all using user's color and side length
    :return:
    """
    # This draws the center hexagon
    length_hex = get_length_hexagon()
    petal_color = get_petal_color()
    draw_hex(length_hex, get_center_color())
    # Move to the correct location and draw a hexagon for petal
    turtle.penup()
    turtle.left(120)
    turtle.forward(length_hex)
    turtle.right(60)
    turtle.forward(length_hex)
    turtle.right(60)
    turtle.pendown()
    draw_hex(length_hex, petal_color)
    turtle.penup()
    turtle.forward(length_hex)
    turtle.right(60)
    turtle.forward(length_hex)
    turtle.left(60)
    turtle.pendown()
    draw_hex(length_hex, petal_color)
    turtle.penup()
    turtle.left(240)
    turtle.forward(length_hex)
    turtle.left(60)
    turtle.forward(length_hex)
    turtle.left(60)
    turtle.pendown()
    draw_hex(length_hex, petal_color)
    turtle.penup()
    turtle.left(240)
    turtle.forward(length_hex)
    turtle.right(60)
    turtle.forward(length_hex)
    turtle.left(180)
    turtle.pendown()
    draw_hex(length_hex, petal_color)
    turtle.penup()
    turtle.left(120)
    turtle.forward(length_hex)
    turtle.left(60)
    turtle.forward(length_hex)
    turtle.left(180)
    turtle.pendown()
    draw_hex(length_hex, petal_color)
    turtle.penup()
    turtle.left(120)
    turtle.forward(length_hex)
    turtle.right(60)
    turtle.forward(length_hex)
    turtle.right(60)
    turtle.pendown()
    draw_hex(length_hex, petal_color)


def main():
    draw_flower()


main()


turtle.exitonclick()
