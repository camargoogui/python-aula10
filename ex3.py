print("Numero de linhas: ")
linhas = int(input())
print("Numero de colunas: ")
colunas = int(input())

for b in range(0, linhas):
    for i in range(0, colunas):
        print(i + 1, end="")
    print("")