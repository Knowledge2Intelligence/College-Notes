string = input("Enter String : ")
string = string.casefold()
rev_string = reversed(string)

if list(string) == list(rev_string):
    print("It is palindrome")
else:
    print("It is not palindrome")