# coding: utf-8
n = int(input())
numbers = sorted(list(map(int, input().split(" "))), reverse=True)
high_numbers = numbers[0:len(numbers) // 2]
del numbers[0:len(numbers) // 2]
sequence = [None]*n
sequence[::2] = numbers
sequence[1::2] = high_numbers
for i in range(1, n, 2):
    if not sequence[i - 1] < sequence[i] > sequence[i + 1]:
        print("No")
        break
else:
    print("Yes")
