n = int(input())
arr = list(map(int, input().split()))
orginal = sorted(arr)
nums = sorted(arr, reverse= True)

freq = {}
seen = set()
keep = []
for i in range(len(nums)):
    if nums[i] not in seen:
        seen.add(nums[i])
        keep.append(nums[i])
for ch in nums:
    freq[ch] = freq.get(ch, 0) + 1
prev = 0
ans = 1
mx = max(keep)
prev = freq[mx]
freq[mx] = 1
for i in range(1, len(keep)):
    x = freq[keep[i]]
    if prev == 1:
        ans += 1
    else:
        ans += prev
    freq[keep[i]] = ans
    prev = freq[keep[i]]

ans1 = [0] * len(arr)
for i in range(len(arr)):
    ans1[i] = freq[arr[i]]
print(*ans1)
