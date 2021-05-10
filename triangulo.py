print("Bem-vindo")

n1 = int(input("digite o valor 1: "))
n2 = int(input("digite o valor 2: "))
n3 = int(input("digite o valor 2: "))

def triangulo():
  if (n1 == n2 == n3):
    print("Este é um triangulo Equilátero")
  elif (n1 == n2 != n3):
    print("Este é um triangulo Isósceles")
  elif (n1 != n2 == n3):
    print("Este é um triangulo Isósceles")
  elif (n1 != n2 != n3):
    print("Este é um triangulo Escaleno")
  else:
    print("Tente novamente")

triangulo()
