n = int(input())
strings = []
for _ in range(n):
    strings.append(input())

for i in range(n - 1):
    for j in range(i + 1, n):
        if (strings[i] + strings[j] == (strings[i] + strings[j])[::-1] or
                strings[j] + strings[i] == (strings[j] + strings[i])[::-1]):
            print("Yes")
            break
    else:
        continue
    break
else:
    print("No")
