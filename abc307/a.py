n = int(input())
steps = [int(x) for x in input().split(" ")]
print(steps)

for _ in range(n):
    count = 0
    for i in range(7):
        count += steps.pop(0)
    print(count, end=" ")
