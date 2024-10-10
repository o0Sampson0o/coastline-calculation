import turtle
import csv
R = 200

# read the csv file of lat and lon
def read_csv(file):
    with open(file) as csvfile:
        readCSV = list(csv.reader(csvfile, delimiter=','))
        del readCSV[0]
        for i in range(len(readCSV)):
            readCSV[i] = [float(readCSV[i][0]), float(readCSV[i][1])]
        return readCSV
    
# draw the graph given the points in the csv file using turtle
def draw_graph(points, color="black"):
    turtle.ht()
    turtle.color(color)
    turtle.penup()
    turtle.goto(R * (points[0][1] - 121), R * (points[0][0] - 23.5))
    turtle.pendown()
    for i in range(len(points)):
        turtle.goto(R * (points[i][1] - 121), R * (points[i][0] - 23.5))
    turtle.penup()


screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)

points = read_csv('data.csv')
draw_graph(points)

turtle.done()