def add():
    a = int(input("Enter integer:"))
    b = int(input("Enter integer:"))

    print("The addition of both integers is", a + b)

def sub():
    a = int(input("Enter integer:"))
    b = int(input("Enter integer:"))

    print("THe subtraction of both integers is", a - b)

def mul():
    a = int(input("Enter integer:"))
    b = int(input("Enter integer:"))

    print("The multiplication of both integers is", a * b)

def div():
    a = int(input("Enter integer:"))
    b = int(input("Enter integer:"))

    print("The division of both integers is", a/b)

def minutes1():

    hour = int(input("Enter hour: "))
    minutes = hour * 60
    print(f"{hour} hours = {minutes} minutes")

def hour1():
    minutes = int(input("Enter minutes: "))
    hours = minutes / 60

    print(f"{minutes} minutes = {hours} hours")

def rs1():
    dollar = float(input("Enter dollar amount: "))
    rs = dollar * 48

    print(f"{dollar} dollars = {rs} Rs")

def dollar1():
    rs = float(input("Enter Rs amount: "))
    dollar = rs / 48

    print(f"{rs} Rs = {dollar} dollars")

def pounds1():
    dollar = float(input("Enter dollar amount: "))
    rs = dollar * 48
    pound = rs / 70

    print(f"{dollar} dollars = {pound} pounds")

def kg1():
    grams = float(input("Enter grams: "))
    kg = grams / 1000

    print(f"{grams} grams = {kg} kg")

def gram1():
    kg = float(input("Enter kg: "))
    grams = kg * 1000

    print(f"{kg} kg = {grams} grams")

def KB1():
    bytes = int(input("Enter bytes: "))
    KB = bytes / 1024
    MB = KB / 1024
    GB = MB / 1024
    print(f"{bytes} bytes = {KB} KB = {MB} MB = {GB} GB")

def fah():
    celsius = float(input("Enter celsius: "))
    fahrenheit = (celsius * 9/5) + 32

    print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")

def cel():
    fahrenheit = float(input("Enter fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9

    print(f"{fahrenheit} Fahrenheit = {celsius} Celsius")

def interest():
    prn = int(input("ENter ampount:"))
    i = prn/100
    print(f"{prn} amount has {i} interest")

def sq():
    l = float(input("Enter length of square:"))
    A = l**2
    P = 4*l
    print(f"The are and perimeter of square are {A} and {P}")

def rec():
    l = float(input("Enter length:"))
    b = float(input("Enter breadth:"))
    A = l*b
    P = 2*(l + b)
    print(f"The area and perimeter of rectangle are {A} and {P}")

def circle():
    r = float(input("Enter radius:"))
    A = 22/7 * r * r

    print(f"The area of circle is {A}")

def tri():
    h = float(input("Enter height of triangle:"))
    l = float(input("Enter side length of triangle:"))
    A = (h*l)/2

    print(f"The area of triangle is {A}")

def salary():
    gross_salary = float(input("Enter salary"))
    allowances = gross_salary * 0.10
    deductions = gross_salary * 0.03
    net_salary = gross + allowances - deductions
    print(f"Your net salary is {net_salary}")

def sales():
    gross_sales = float(input("Enter sales"))
    discount = gross_sales * 0.10
    net_sales = gross_sales - discount
    print(f"Your net sales is {net_sales}")

def sub():
    sub1 = float(input("Enter maths marks:"))
    sub2 = float(input("Enter science marks:"))
    sub3 = float(input("Enter biology marks:"))
    avg = (sub1 + sub2 + sub3)/3
    total = sub1 + sub2 + sub3

    print(f"Your total and avg marks are respectively {total} and {avg}")

def swap():
    a = int(input("Enter integer:"))
    b = int(input("Enter integer:"))
    print(f"Before swpping a = {a} and b = {b}")
    
    a, b = b, a
    print(f"After swapping a= {a} and b = {b}")

add()
