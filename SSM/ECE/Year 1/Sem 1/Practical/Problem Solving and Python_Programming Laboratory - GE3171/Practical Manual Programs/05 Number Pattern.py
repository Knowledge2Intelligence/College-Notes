N = 5
for i in range(1,N+1):
    for k in range(1, N+1-i):
        print(' ', end = ' ')
    for j in range(1,i+1):
        print(j, end = ' ')
    for l in range(i-1,0,-1):
        print(l, end = ' ')
    print()