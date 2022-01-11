#Programa ue compara uma sequência a uma reta




#importar biblioteca matematica
from math import *

#Variaveis
z = [0]
ok = []
eps = 0.2
pos =-1
#f = True

#entrada de dados
M = int(input("Digite a quantidade de termos da sequência: ")
        )  #primeiro usuario inserindo os termos(int)

w = complex(input("Digite w: ").replace(" ", "").replace(",", "."))

eps = float(input("Insira o ε: "))

#Calcular Sequência
for i in range(M):
    z.append(z[i]**2 + w)
#Comparar a reta
for k in range(M):
    condicao = True
    for i in range(k+1,M+1):
        if abs(z[k] - z[i]) >= eps:
            condicao = False
    ok.append(condicao)

print(z,len(z))


pos =-1
print(ok)
for k in range(len(ok)):
  if ok[k]==True:
    pos = k
    break
if pos == -1:
    print("Não há índice a partir do qual um elemento e seus subsequentes estejam a uma distancia menor a menor que: ", eps)
else:
    print("Menor indice procurado é: ", pos)

#Mostrar nome dos integrantes do Projeto
for i in range(5):
    print()
print(" João Pedro Firmino Brandão dos Santos RA:22.121.031-3\n",
      "Arthur de Olim Perestrelo RA:22.121.019-8\n",
      "Eduardo Antunes Vicente RA:22.121.010-7")