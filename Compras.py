#Calcula as parcelas e o desconto de um produto automaticamente


v = float(input("Digite o valor da compra: "))
p = float(input("Digite a quantidade de parcelas: "))
d= 0
if p == 1:
  d= v*0.1
if p == 2:
  d= v*0.05
if p == 3:
  d= v*0.05
if v >=5000:
  d = d+(v*0.05)
c= v-d
t= c/p
print("Desconto total: %.2f" %d)
print("Valor final da compra com desconto: %.2f" %c)
print("Cada parcela será de: %.2f" %t)