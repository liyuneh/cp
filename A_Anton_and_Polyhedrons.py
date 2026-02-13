t = int(input())
dict = {"Icosahedron":20, "Tetrahedron":4, "Cube":6, "Dodecahedron":12, "Octahedron":8}
sum1 = 0
for _ in range(t):
    s = input()
    sum1 += dict[s]
print(sum1)