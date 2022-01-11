#Calcula a aresta de um dodecaedro e icosaedro


import math
f= input("Você deseja calcular o volume do dodecaedro ou icosaedro: ")
a= int(input("Digite o valor da aresta a em metros: "))
c=0
if f == "dodecaedro":
  c= (((15+(7*(math.sqrt(5))))/4))*(a**3)
  print("O volume de um dodecaedro regular com 1.00 de aresta é: %.2f" %c)
if f == "icosaedro":
  c=((3*(5/12))+(math.sqrt(5)*(5/12)))*(a**3)
  print("O volume de um icosaedro regular com 1.00 de aresta é: %.2f" %c)