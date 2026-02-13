n , k = map(int, input().split())
arr = list(map(int, input().split()))
place = arr[k-1]

count = 0
for i in range(len(arr)):
    if arr[i] >= place and arr[i] > 0:
        count += 1
print(count)