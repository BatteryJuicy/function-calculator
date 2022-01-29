from math import sqrt

def func(equation):
    points_set = []
    def_set = int(input("absolute range of x values to compute: "))
    x = def_set
    if equation.lower() == "linear":
        a = float(input("tangent of the line: "))
        b = float(input("displacement:"))

        for i in range(-def_set, def_set):
            points_set.append((i, a * i + b))
        print("intersects with x'x at (" + str(-b/a) + ",0)")
        print("intersects with y'y at (0," + str(b) + ")")
    elif equation.lower() == "quadratic":
        print("the formula is: f(x) = a(x - b)^2 + c")
        a = float(input("(a) factor: "))
        b = float(input("(b) horizontal displacement: "))
        c = float(input("(c) Vertical displacement: "))
        
        for i in range(-def_set, def_set):
            points_set.append((i, a(i - b)**2 + c))
        d = b**2 - 4*a*c
        if d >= 0:
            x_intersection1 = (sqrt(d) - b) / (2*a)
            x_intersection2 = (-sqrt(d) - b) / (2*a)
            print("intersects with x'x at (", str(x_intersection1) + ",0)" + "and at (" + str(x_intersection2) + ",0)")
        else:
            print("no intersection point with x'x")
        print("intersects with y'y at (0," + str(a*(b**2) + c) + ")")
    else:
        print("The only equations available are: 'linear', 'quadratic'.")
    print(points_set)

    
func("quadratic")