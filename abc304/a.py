n = int(input())
people = [input().split(" ") for _ in range(n)]
age = [int(people[i][1]) for i in range(n)]
min_age_index = age.index(min(age))
print(*[row[0] for row in people[min_age_index:]], sep="\n")
print(*[row[0] for row in people[:min_age_index]], sep="\n")
