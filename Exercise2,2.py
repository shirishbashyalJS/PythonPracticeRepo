import  math
# Write a program that asks the user for the radius of a circle and the prints out the area of the circle.
radius = int(input("Enter radius of a circle: "))
area = math.pi * (radius ** 2)
print("The area of a circle having radius: "+str(radius)+ " is: "+str(area))
