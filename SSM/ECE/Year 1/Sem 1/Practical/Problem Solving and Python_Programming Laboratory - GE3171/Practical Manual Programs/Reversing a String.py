def reverse(string):
    string = "".join(reversed(string))
    return string

s = input("Enter any string : ")
print("The original string is : ")
print(s)

print("The reversed string(using reversed) is : ", reverse(s))