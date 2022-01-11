#calcula a vazão de agua de um recipiente




v = float(input("Digite a vazão da bomba em l/s: "))
r = float(input("Digite a capacidade do reservatório: "))
t = 0
h = 0
m = 0
s = 0
t = r / v  #calcula o tempo total em segundos
print(t)
h = int((t // 3600))
print(t)
m = int((t / 3600) - (t // 3600))
print(t)

print("Tempo necessário para encher o reservatório: ", end="")
print(h, end="")
print(":", end="")
print(m, end="")
print(":", end="")
print(s, end="")
