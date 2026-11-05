import turtle


def draw_pythagoras_tree(
    branch_length: float,
    level: int,
    pen: turtle.Turtle
) -> None:
    if level == 0:
        return

    pen.forward(branch_length)

    pen.left(45)
    draw_pythagoras_tree(branch_length * 0.7, level - 1, pen)

    pen.right(90)
    draw_pythagoras_tree(branch_length * 0.7, level - 1, pen)

    pen.left(45)
    pen.backward(branch_length)


def main() -> None:
    level = int(input("Введіть рівень рекурсії: "))

    screen = turtle.Screen()
    screen.title("Дерево Піфагора")
    screen.bgcolor("white")

    pen = turtle.Turtle()
    pen.color("green")
    pen.speed(0)
    pen.left(90)
    pen.penup()
    pen.goto(0, -250)
    pen.pendown()

    draw_pythagoras_tree(120, level, pen)

    pen.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()