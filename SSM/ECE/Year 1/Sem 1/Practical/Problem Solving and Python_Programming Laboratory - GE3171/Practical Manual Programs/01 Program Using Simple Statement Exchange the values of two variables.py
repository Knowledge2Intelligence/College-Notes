def exchage(x,y):
    x,y=y,x
    print("After exchange of x,y")
    print("x = ",x)
    print("y = ",y)

x = input("Enter value of X : ")
y = input("Enter value of Y : ")
print("Before exchange of x,y")
print("x = ",x)
print("y = ",y)
exchage(x,y)