#calcula a equação geral do plano


def leponto(w, k=3):
    for i in range(k):
        k = float(input("Digite a %da. coordenada: " % (i+1)))
        w.append(k)
    return w


def prodvet(u, v):
    vet = []
    x = u[1]*v[2] - v[1]*u[2]
    vet.append(x)
    y = v[0]*u[2] - u[0]*v[2]
    vet.append(y)
    z = u[0]*v[1] - v[0]*u[1]
    vet.append(z)
    return vet

def modulo(vetor):
    return vetor[0]**2 + vetor[1]**2 + vetor[2]**2


print("Plano:")

print("Coordenadas do ponto A:")

a = []

leponto(a)

print("Coordenadas do ponto B:")

b = []

leponto(b)

print("Coordenadas do ponto C:")

c = []

leponto(c)

u = (a[0] - b[0], a[1] - b[1], a[2] - b[2])

v = (a[0] - c[0], a[1] - c[1], a[2] - c[2])

prodvetor = prodvet(u, v)

mod = modulo(prodvetor)

if mod:
    d = a[0]*prodvetor[0] + a[1]*prodvetor[1] + a[2]*prodvetor[2]

    if prodvetor[0] < 0:
        prodvetor[0] = - prodvetor[0]
        prodvetor[1] = - prodvetor[1]
        prodvetor[2] = - prodvetor[2]
        d = -d

    print("Equação Geral do plano: ")

    print("ax + by + cz + d = 0")

    print("onde:")

    print("a = %.2f, b = %.2f, c = %.2f e d = %.2f" % (prodvetor[0], prodvetor[1], prodvetor[2], (-1)*d))
else:
    print("Dados Incorretos")