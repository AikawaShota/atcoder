# TLE
t = int(input())
numbers = [int(input()) for _ in range(t)]
for i in numbers:
    for j in range(i+1, 1, -1):
        if popcount(j) == 3:
            print(j)
            break
    else:
        print(-1)
