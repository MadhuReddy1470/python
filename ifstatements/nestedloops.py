row = int(input("how many rows:"))
coloumns = int(input("how many coloumns:"))
symbol = input("enter symbol")

for i in range(row):
    for j in range(coloumns):
        print(symbol, end="")
    print()


