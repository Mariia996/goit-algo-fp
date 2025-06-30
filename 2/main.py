import turtle
import math

def draw_pythagoras_tree(t, order: float, size: int):
    """ Малює дерево Піфагора"""

    if size > 0:
        # Основна гілку
        t.forward(order)
        # Поточне положення і кут
        pos = t.position()
        angle = t.heading()

        # Права гілка
        t.left(45)
        draw_pythagoras_tree(t, order * math.sqrt(2) / 2, size - 1)
        t.setposition(pos)
        t.setheading(angle)

        # Ліва гілку
        t.right(45)
        draw_pythagoras_tree(t, order * math.sqrt(2) / 2, size - 1)
        t.setposition(pos)
        t.setheading(angle)
        t.backward(order)

def main():
    """Основна функція для запуску програми."""
    depth = int(input("Введіть рівень рекурсії: "))
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.color("green")
    t.hideturtle()
    t.speed(0)
    t.left(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()
    draw_pythagoras_tree(t, 100, depth)
    turtle.done()

if __name__ == "__main__":
    main()
