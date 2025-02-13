def large2():
    a = int(input("Enter a integer:"))
    b = int(input("Enter a integer:"))

    if a > b:
        print(f"{a} is the greatest integer and {b} is the smallest integer")
    elif a < b:
        print(f"{b} is the greatest integer and {a} is the smallest integer")
    else:
        print(f"Both integers are equal")

def large3():
    a = int(input("Enter a integer:"))
    b = int(input("Enter a integer:"))
    c = int(input("Enter a integer:"))

    if a > b and a > c:
        print(f"{a} is the largest integer")
    elif b > a and b > c:
        print(f"{b} is the largest integer")
    else:
        print(f"{c} is the largest integer")

def odd():
    num = int(input("Enter a number:"))
    if num%2 == 0:
        print(f"{num} is even number")
    else :
        print(f"{num} is odd number")

def div_10():
    num = int(input("Enter a number:"))
    if num%10 == 0:
        print(f"{num} is divisible by 10")
    else :
        print(f"{num} is not divisible by 10")

def age():
    age = int(input("Enter your age:"))
    if age >= 18:
        print("Major")
    else:
        print("Minor")

def size():
    num = input("Enter the integer:")

    a = len(num)
    print(f"The number of digits in {num} is {a}")

def leap():
    year = int(input("Enter a year:"))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

def triangle():
    a = int(input("Enter the first angle of the triangle:"))
    b = int(input("Enter the second angle of the triangle:"))
    c = int(input("Enter the third angle of the triangle:"))

    if a + b + c == 180:
        print("It is a valid triangle")
    else :
        print("It is not a valid triangle")

def absolute():
    num = float(input("Enter a number:"))
    print(f"Absolute value is {abs(num)}")

absolute()

def rectangle():
    length = int(input("Enter the length of the rectangle:"))
    width = int(input("Enter the width of the rectangle:"))
    area = length * width
    perimeter = 2*(length + width)

    if area > perimeter:
        print("Area of rectangle is greater than perimeter")
    else :
        print("Perimeter of rectangle is greater than perimeter")

def line():
    x1 = int(input("Enter x-coordinate of first point:"))
    y1 = int(input("Enter y-coordinate of first point:"))
    x2 = int(input("Enter x-coordinate of second point:"))
    y2 = int(input("Enter y-coordinate of second point:"))
    x3 = int(input("Enter x-coordinate of third point:"))
    y3 = int(input("Enter y-coordinate of third point:"))

    if ((x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)) == 0:
        print("The points are in straight line")
    else:
        print("The points are not in straight line")

def circle():
    x1 = int(input("Enter x-coordinate of center:"))
    y1 = int(input("Enter y-coordinate of center:"))
    x = int(input("Enter x-coordinate of point:"))
    y = int(input("Enter y-coordinate of point:"))
    r = int(input("Enter radius of circle:"))

    distance = ((x - x1) * 2 + (y - y1) * 2) ** 0.5
    if distance <= r:
        print("Point is inside the circle")
    elif distance == r:
        print("Point is on the circle")
    else:
        print("Point is outside the circle")

def marks():
    math = int(input("Enter math marks:"))
    science = int(input("Enter science marks:"))
    social = int(input("Enter social marks:"))

    total = math + science + social
    average = total / 3
    print(f"Total marks: {total}")
    print(f"Average marks: {average}")

    if average >= 80 and average <=100:
        print("Grade: O")
    elif average >= 70 and average < 80:
        print("Grade: A+")
    elif average >= 60 and average < 70:
        print("Grade: A")
    elif average >= 55 and average < 60:
        print("Grade: B+")
    elif average >= 50 and average < 55:
        print("Grade: B")
    elif average >= 45 and average < 50:
        print("Grade: C")
    elif average >=40 and average < 45:
        print("Grade: P")
    elif average >= 0 and average < 40:
        print("Grade: F")
    else :
        print("NA")

    if average <= 39 :
        print("Failed in all subjects")
    else :
        print("Passed in all subjects")

