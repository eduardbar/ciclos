num = int(input("ingrese número: \n"))
if num >= 1 and num <= 10:
    for i in range (1, 11):
        producto = num * i
        print (num, "x", i, "=", producto)
else: 
    print("el número debe estar entre 1 y 10")