s = list(input("Enter list of numbers: ").split())

max_n = min_n = int(s[0])
min_i = max_i = 0
for i in range(len(s)):
    if max_n < int(s[i]):
        max_i = i
        max_n = int(s[i])
    if min_n > int(s[i]):
        min_i = i
        min_n = int(s[i])

s[max_i], s[min_i] = s[min_i], s[max_i]

print("New list: ", *s) # 100 23 48 2 38 188 499 47
