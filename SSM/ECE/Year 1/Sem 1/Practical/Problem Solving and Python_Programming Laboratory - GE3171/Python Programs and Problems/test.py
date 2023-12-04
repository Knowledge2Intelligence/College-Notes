choice = input("y/n")
while (choice == 'y'):
    print("1. Sum of Digits \n 2. Counting Digits \n 3. Reverse String \n 4. Palindrome or not \n 5. Armstrong or not \n 6. Prime number or not \n 7. Fibonacci Series \n")
    sel = int(input("Enter your choice: "))

    if (sel == 1):
        def sumDigits(no):
            return 0 if no == 0 else int(no % 10) + sumDigits(int(no / 10))
        in_no_for_sum = int(input("Enter Digits: "))
        print(sumDigits(in_no_for_sum))

    elif (sel == 2):
        def countDigits(num):
            count = 0
            while num > 0:
                count += 1
                num = num // 10
            print(count)
        in_no_for_count = int(input("Enter numbers to count: "))
        countDigits(in_no_for_count)

    elif (sel == 3):

        def revDigits(num):
            r =0
            while num != 0:
                digit = num % 10
                r = r * 10 + digit
                num //= 10
            print(r)
        in_for_rev = int(input("Enter some Digits: "))
        revDigits(in_for_rev)

    elif (sel == 4):
        def palin(num):
            rev = 0
            n = 0
            tmp = n
            while n > 0:
                r = n % 10
                rev = rev * 10 + r
                n //= 10
            if (tmp == rev):
                print("The Given number is Palindrome")
            else:
                print("Not palindrome")
        in_for_pali = int(input("Enter Number: "))
        palin(in_for_pali)

    elif (sel == 5):

        def armstrong(nmu):
            sum = 0
            n = 12
            num = n
            while n > 0:
                r = n % 10
                sum = sum * r * r * r
                n //= 10
            if (num == sum):
                print("Armstrong")
            else:
                print("Not Armstrong")

    elif (sel == 6):
        inm = 12
        if inm > 1:
            for i in range(2, int(inm / 2) + 1):
                if (inm % i) == 0:
                    print("not")
                    break
            else:
                print("prime")
        else:
            print("not prime")

    elif (sel == 7):
        def fibo(n):
            i = 0
            f1 = -1
            f2 = 1
            f3 = f1+f2
            while (f3 <= n):
                print(f3)
                f1 = f2
                f2 = f3
                f3 = f1+f3
                i += 1
        in_for_fibo = int(input("Enter the Limit: "))
        fibo(in_for_fibo)

    else:
        print("Invaid Input")
