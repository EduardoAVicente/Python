#Cria uma matriz


def cria_matriz(l, c):
  m = []
  for i in range(l):
    l = []
    for k in range(c):
      if i == k:
        l.append(0)
      else:
        l.append(1)
    m.append(l)
  return m

def imprime_matriz(e):

    l = len(e)
    c = len(e[0])

    for i in range(l):
        for k in range(c):
            if(k == c - 1):
                print("%d" %e[i][k])
            else:
                print("%d" %e[i][k], end = " ")
    print()

e = int(input())

u = cria_matriz(e, e)
imprime_matriz(u)