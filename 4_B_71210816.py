nilaiN = int(input("input : "))
print("Output : ")
for x in range(nilaiN):
    for y in range (nilaiN):
        if(y == (nilaiN-1)) or (x == (nilaiN-1)) or (x + y == (nilaiN-1)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()