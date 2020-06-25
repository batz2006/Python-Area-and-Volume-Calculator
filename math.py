import math
pi = 3.14159265359

def cylinder():
    r = float(input("Please enter radius: "))
    h = float(input("Please enter height: "))
    volume = pi*(r**2)*h
    area = (2*pi*r*h) + (2*pi*(r**2))
    print(f"The area of the cylinder is {area} and the volume is {volume}.")

def rectangle():
    decision = input("Please choose from one of the following: \nRectangle Area (write area) \nRectangular prism volume (write volume)")
    if decision.lower() == "area":
        w = float(input("Please enter width: "))
        l = float(input("Please enter length: "))
        area = w * l
        print(f"The area of the rectangle is {area}.")
    elif decision.lower() == "volume":
        w = float(input("Please enter width: "))
        l = float(input("Please enter length: "))
        h = float(input("Please enter height: "))
        volume = w * l * h
        print(f"The volume of the rectangular prism is {volume}.")

def triangle():
    print("Please choose from one of the following options: ")
    print("Area of triangle (write area)")
    print("Volume of triangular prism (write vtp)")
    print("Volume of pyramid (write vp)")
    decision = input("Please enter your decision: ")

    if decision.lower() == "area":
        b = float(input("Please enter base: "))
        h = float(input("Please enter height: "))
        area = (b*h)/2
        print(f'Area of the triangle is {area}.')
    elif decision.lower() == 'vtp':
        a = float(input("Please enter first base side length: "))
        b = float(input("Please enter second base side length: "))
        c = float(input("Please enter third base side length: "))
        h = float(input("Please enter height: "))

        volume = (0.25*h) * (-a**4 + (2 * ((a * b)**2)) + (2 * ((a * c)**2)) -b**4 +  (2 * ((b*c) **2)) -c**4 )**0.5
        print(f"Volume of the triangular prism is {volume}.")
    elif decision.lower() == 'vp':
        l = float(input("Please enter base length: "))
        w = float(input("Please enter base width: "))
        h = float(input("Please enter height: "))
        volume = (l*w*h)/3
        print(f"Volume of the pyramid is {volume}.")

def cone():
    r = float(input("Please enter radius: "))
    h = float(input("Please enter height: "))
    volume = pi * (r**2) * (h/3)
    print(f"Volume of the cone is {volume}.")

def dodecahedron():
    a = float(input("Please enter edge: "))
    volume = ((15 + (7 * (5)**0.5))/4) * (a**3)
    print(f"Volume of the dodecahedron is {volume}.")

def icosahedron():
    a = float(input("Please enter edge: "))
    volume = ((5 * (3 + (5 ** 0.5)))/12) * (a**3)
    print(f"Volume of the icosahedron is {volume}.")

def octahedron():
    a = float(input("Please enter edge: "))
    volume = ((2**0.5)/(3)) * a**3
    print(f"Volume of the octahedron is {volume}.")
    
def circleAndSphere():
    r = float(input("Please enter radius: "))
    v = (4/3)*(pi)*(r**3)
    a = pi * (r**2)
    print(f"The area of the circle is {a} and the volume of the sphere is {v}.")

def hexagon():
    decision = input("Please tell what action you would like to take: \narea(for hexagon)\nvolume(for hexagonal prism)\n")
    if decision.lower() == 'area':
        a = float(input("Please enter side length: "))
        area = ((3*(3**0.5))/2) * (a**2)
        print(f"The area of the hexagon is {area}.")
    elif decision.lower() == 'volume':
        a  =float(input("Please enter base edge: "))
        h = float(input("Please enter height: "))
        v = ((3*(3**0.5))/2)*(a**2)*(h)
        print(f"The volume of the hexagonal prism is {v}.")

print("Welcome to math.py! Please choose one of the following options to get started.")
print("cylinder")
print("rectangle")
print("triangle")
print("cone")
print("dodecahedron")
print("icosahedron")
print("octahedron")
o = input("Please write here, in the exact way you see, the decision: ")

if o.lower() == "cylinder":
    cylinder()
elif o.lower() == "rectangle":
    rectangle()
elif o.lower() == 'triangle':
    triangle()
elif o.lower() == 'cone':
    cone()
elif o.lower() == "dodecahedron":
    dodecahedron()
elif o.lower() == 'icosahedron':
    icosahedron()
elif o.lower() == 'octahedron':
    octahedron()
elif o.lower() == "circleAndSphere":
    circleAndSphere()
elif o.lower() == "hexagon":
    hexagon()
