arr = []
for _ in range(int(input())):
    arr.append(input())
print(0)
for i in range(len(arr)-1):
    c = 0
    ch = arr[0:i+1]
    for j in ch:
        if arr[i+1] > j:
            c += 1
    print(c)
