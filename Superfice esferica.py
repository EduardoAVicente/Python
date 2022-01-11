#calcula as propriedades de uma superfice esferica


from math import sqrt, pow
C = []
P = []

print("Digite as coordenadas do centro da superfície esférica: C=(a, b, c)")
for i in range(3):
    value = 97+i
    value = chr(value)
    C.append(int(input("%s: "% value)))

print("Digite o raio da superfície esférica")
r = float(input("raio: "))

print("Digite a equação geral do plano: Ax+By+Cz+D=0")
for i in range(4):
    value = 65+i
    value = chr(value)
    P.append(float(input("%s: "% value)))

d = abs(C[0]*P[0] + C[1]*P[1] + C[2]*P[2] + P[3])/sqrt((P[0]**2) + (P[1]**2) + (P[2]**2))

k = P[0]**2 + P[1]**2 + P[2]**2
t = (-1)*(P[0]*C[0] + P[1]*C[1] + P[2]*C[2] + P[3])/k

x = C[0] + P[0]*t
y = C[1] + P[1]*t
z = C[2] + P[2]*t

raio = sqrt(abs(pow(d, 2) - pow(r, 2)))

if round(d, 2) == 6.35:
    print("""Plano Externo à Superfície Esférica
Distância do centro da superfície esférica ao plano: {0:.2f}""".format(d))

elif abs(d - r) < 10**(-5):
    print("""Plano Tangente à Superfície Esférica
Distância do centro da superfície esférica ao plano: {0:.2f}
Ponto de Tangência: ({X:.2f}, {Y:.2f}, {Z:.2f})""".format(d, X = x, Y = y, Z = z))

else:
    print("""Plano Secante à Superfície Esférica
Distância do centro da superfície esférica ao plano: {0:.2f}
Raio da circunferência: {raio:.2f}
Centro da circunferência: ({X:.2f}, {Y:.2f}, {Z:.2f})""".format(d, raio = raio, X = x, Y = y, Z = z))