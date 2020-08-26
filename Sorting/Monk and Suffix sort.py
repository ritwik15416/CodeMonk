s,k = input().split(" ")
lst = []
k = int(k)
for i in range(len(s)):
    lst.append(s[i:])
lst.sort()
print(lst[k-1])
