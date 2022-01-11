#calcula o desconto de um trio de produtos

p1 = float(input("Digite o valor do primeiro produto: "))
p2 = float(input("Digite o valor do segundo produto: "))
p3= float(input("Digite o valor do terceiro produto: "))
r = p1+p2+p3
if r >500:
  q = r*0.2
  print("Desconto: %.2f" %q)
if r <= 500:
  q= r*0.1
  print("Desconto: %.2f" %q)