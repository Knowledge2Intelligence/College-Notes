import math
x1 = int(input("Enter a x1 : "))
y1 = int(input("Enter a y1 : "))
x2 = int(input("Enter a x2 : "))
y2 = int(input("Enter a y2 : "))

distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
print("Ditance = ",distance)