ClienteNome = input("Digite o nome do cliente: ")
FaturaVencimentoDia = input("Digite o dia de vencimento: ")
FaturaVencimentoMes = input("Digite o mês do vencimentio: ")
FaturaValor = input("Digite o valor da sua fatura: ")


print("Olá, {}\nA sua fatura com vencimento em {} de {} no valor de R$ {} está fechada.".format(ClienteNome, FaturaVencimentoDia, FaturaVencimentoMes, FaturaValor))