n1 = int(input("add number: \n"))
n2 = int(input("add number: \n"))

if (n1 > n2):
    n1, n2 = n2, n1
add = 0 

for a in range(n1 + 1, n2):
    add = add + a
print(f"la suma es {add} ")