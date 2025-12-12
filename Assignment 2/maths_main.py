import math_utils as mu

print("select shape to calculate area:")
print("1. Square")
print("2. Circle")
print("3. Rectangle")
print("4. Triangle")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    side_length = float(input("Enter the side length of the square: "))
    area = mu.calc_area_square(side_length)
    print("Area of the square:", area)
elif choice == 2:
    radius = float(input("Enter the radius of the circle: "))
    area = mu.calc_area_circle(radius)
    print("Area of the circle:", area)
elif choice == 3:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = mu.calc_area_rectangle(length, width)
    print("Area of the rectangle:", area)
elif choice == 4:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = mu.calc_area_triangle(base, height)
    print("Area of the triangle:", area)
else:
    print("Invalid choice")