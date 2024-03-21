import turtle


def draw_tree(branch_len, angle, level, t):
    if level > 0:
        t.forward(branch_len)
        t.left(angle)
        draw_tree(branch_len - 15, angle, level - 1, t)
        t.right(2 * angle)
        draw_tree(branch_len - 15, angle, level - 1, t)
        t.left(angle)
        t.backward(branch_len)


def main(level):
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor('white')
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    draw_tree(100, 30, level, t)
    screen.exitonclick()


main(5)
