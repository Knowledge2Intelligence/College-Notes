def circulate(A,N):
    for i in range(1,N+1):
        B=A[i:]+A[:i]
        print("Circulation ",i," = ",B)
    return
A = [91,92,93,94,95]
N = int(input("Enter n : "))
circulate(A,N)