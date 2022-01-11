digitos = int(input("Digite a ordem da matriz (até ordem 3): "))
if digitos == 1:
    matriz =[[0],[0]]

if digitos == 2:
    matriz =[[0,0],[0,0]]

if digitos == 3:
    matriz =[[0,0,0],[0,0,0],[0,0,0]]




for coluna in range(digitos):
    for linha in range(digitos):
        matriz[coluna][linha] = int(input("Digite o elemento %d %d da matriz: "%(coluna+1,linha+1)))

print("MATRIZ:")
for coluna in range(len(matriz)):
    for linha in range(len(matriz)):
        print(matriz[coluna][linha]," ",end="")
    print("")
