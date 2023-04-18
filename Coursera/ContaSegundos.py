segundos_str = 11827391 # input("Digite o número em segundos de tempo que quer saber: \n")
total_seg = int(segundos_str)

horas = total_seg // 3600
seg_restante = total_seg % 3600
minutos = seg_restante // 60
seg_restante_final = seg_restante % 60
dias = 0


print(horas, "horas\n", minutos, "Minutos e \n", seg_restante_final, "Segundos")
a = int(input("Qual o valor de a? "))
b = int(input("Qual o valor de b? "))
aux = a
a = b
b = aux
print(a)
print(b)