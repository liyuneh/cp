k = int(input())
updates = [list(map(int, input.split(','))) ]

diff = [0] * k

for l, r, val in updates:
    diff[l] += val
    if r + 1 < k:
        diff[r + 1] -= val

running_sum = [0] * k
r = 0
for i in range(k):
    r += diff[i]
    running_sum[i] = r

print(running_sum)
