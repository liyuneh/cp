n = int(input())
arr = list(map(int, input().split()))
arr.sort()
arr1 = [i for i in range(1, n + 1)]
seen = set(arr)
for i in range(len(arr1)):
    if arr1[i] not in seen:
        print(arr1[i])
