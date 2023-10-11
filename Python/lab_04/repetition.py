words = input("Enter: ").split()

stat = dict()

stat = dict()
for x in words:
     stat[x] = stat.get(x, 0) + 1

for i in stat:
    print(stat[i], end=" ")

# input: abc bcd abc abd abd dcd abc
# output: 3 1 2 1
# input: aaa bbb ccc
# output: 1 1 1
# input: abc abc abc
# output: 3
