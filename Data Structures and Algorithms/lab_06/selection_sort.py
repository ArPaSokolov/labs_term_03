s = list(map(int, input("Enter list of numbers: ").split()))

for i in range(0, len(s)):
        for n in range(i+1, len(s)):
            if s[n] < s[i]:
                s[n], s[i] = s[i], s[n]

print("Sorted list: ", *s)
