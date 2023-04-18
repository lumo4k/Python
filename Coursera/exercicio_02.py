notas = []

for x in range(0, 4):
      notas.append(float(input("Digite a nota: ")))

somaAritmetica = 0

for nota in notas:
    somaAritmetica += nota

somaAritmetica /= 4

print("A média aritmética é", somaAritmetica)