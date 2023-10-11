s = list(input("Enter list of numbers: ").split())

new_s = list()
flag = 0
for i in range(len(s) - 1):
    if s[i] > s[i + 1]:
        new_s.append(s[i])
        flag = 1
if flag == 0:
    new_s = s[-1]

print("the list: ", *new_s)
