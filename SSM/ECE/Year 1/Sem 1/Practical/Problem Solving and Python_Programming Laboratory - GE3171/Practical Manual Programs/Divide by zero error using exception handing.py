n = int(input("Enter the value of n : "))
d = int(input("Enter the value of d: "))
c = int(input("Enter the value fo c: "))
try:
    q=n/(d-c)
    print("Quotient",q)
except ZeroDivisionError:
    print("Division by Zero!")