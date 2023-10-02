s = list(map(int, input().split()))

gap = len(s)
while gap > 1:
    gap = gap // 1.3
    for i in range(0, len(s)):
        if s[i] > s[gap]:
            s[i], s[gap] = s[gap], s[i]
print(s)