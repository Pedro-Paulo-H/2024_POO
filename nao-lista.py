from calendar import c
from this import d


print("Digite quatro valores inteiros")
valor1 = int(input())
valor2 = int(input())
valor3 = int(input())
valor4 = int(input())

x = []
if valor1 % 2 == 0: x.append(valor1)
if valor2 % 2 == 0: x.append(valor2)
if valor3 % 2 == 0: x.append(valor3)
if valor4 % 2 == 0: x.append(valor4)

if len (x) == 0: print("Nenhum numero par foi encontrado")
else: print(f"O maior numero par é {max (x)}")

