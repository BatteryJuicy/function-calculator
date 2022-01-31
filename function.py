from math import sqrt
import matplotlib.pyplot as plt

def func(equation, a, b, c, def_set):
    """(type of function(quadratic or linear), a, b, c, distance of O(0,0) and x (±))"""
    points_set = []
    if equation.lower() == "linear":
        print("the formula is: f(x) = a*x + b")

        for i in range(-def_set, def_set + 1):
            points_set.append((i, a * i + b))
        print("intersects with x'x at (" + str(-b/a) + ",0)")
        print("intersects with y'y at (0," + str(b) + ")")

    elif equation.lower() == "quadratic":
        print("the formula is: f(x) = a*(x - b)^2 + c")
        
        for i in range(-def_set, def_set + 1):
            points_set.append((i, a*(i - b)**2 + c))

        d = b**2 - 4*a*c
        if d > 0:
            x_intersection1 = (sqrt(d) - b) / (2*a)
            x_intersection2 = (-sqrt(d) - b) / (2*a)
            print("intersects with x'x at (", str(x_intersection1) + ",0)" + "and at (" + str(x_intersection2) + ",0)")
        elif d == 0:
            x_intersection = (sqrt(d) - b) / (2*a)
            print("touches x'x at (", str(x_intersection) + ",0)")
        else:
            print("no intersection point with x'x")
        print("intersects with y'y at (0," + str(a*(b**2) + c) + ")")
    return(points_set)

def graph(points_list):
    """graphs the points of the function specified using the func() method."""
    def cords(lst, cord):
        result = []
        for i in range(len(lst)):
            result.append(lst[i][cord])
        return result

    x_cords = cords(points_list, 0)
    y_cords = cords(points_list, 1)

    plt.plot(x_cords, y_cords)
    plt.show()
