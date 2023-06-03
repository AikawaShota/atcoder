n = input()
n_length = len(n)

if n_length < 4:
    print(n)
elif n_length < 5:
    print(n[:3] + "0"*1)
elif n_length < 6:
    print(n[:3] + "0"*2)
elif n_length < 7:
    print(n[:3] + "0"*3)
elif n_length < 8:
    print(n[:3] + "0"*4)
elif n_length < 9:
    print(n[:3] + "0"*5)
else:
    print(n[:3] + "0"*6)
