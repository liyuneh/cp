n = int(input())
def k_pos(k: int):
    counter  = 0
    a = 0
    while counter < k:
        a = a + 1
        if a % 3 != 0 and a % 10 != 3:
            counter += 1
    return a
for i in range(n):
    k = int(input())
    print(k_pos(k))