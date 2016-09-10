__author__ = 'yashar'
import turtle


def sierpineski(points, n, t):
    color = ['blue', 'red', 'green', 'white', 'GreenYellow', 'violet', 'orange', 'Maroon']
    draw_triangle(points, color[n], t)
    if n > 0:
        sierpineski([points[0], midpoint(points[0], points[1]), midpoint(points[0], points[2])], n - 1, t)
        sierpineski([points[1], midpoint(points[1], points[0]), midpoint(points[1], points[2])], n - 1, t)
        sierpineski([points[2], midpoint(points[2], points[0]), midpoint(points[2], points[1])], n - 1, t)


def draw_triangle(points, color, t):

    t.fillcolor(color)
    t.up()
    t.goto(points[0][0], points[0][1])
    t.down()
    t.begin_fill()
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[0][0], points[0][1])
    t.end_fill()


def midpoint(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


t = turtle.Turtle()
window = turtle.Screen()
base_points = [[-100, -50], [0, 100], [100, -50]]
sierpineski(base_points, 3, t)
window.exitonclick()

