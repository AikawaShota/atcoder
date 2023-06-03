from math import sqrt


def infection(x1, y1, x2, y2):
    return float(sqrt((x1 - x2)**2 + (y1 - y2)**2))


n, d = map(int, input().split(" "))
coordinate = []
for _ in range(n):
    x, y = map(int, input().split(" "))
    coordinate.append([x, y])

infected = [False for _ in range(n)]
infected[0] = True
for i in range(n - 1):
    for j in range(1, n):
        if infection(coordinate[i][0], coordinate[i][1], coordinate[j][0], coordinate[j][1]) <= d:
            if infected[i]:
                infected[j] = True

for x in infected:
    if x:
        print("Yes")
    else:
        print("No")
