#######################################################################################################################################################################
#Nome : Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Número: 11 94100-2656
#
#Exercício 5.13 - Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número de
#meses para que a dívida seja paga, o total pago e o total de juros pago.
#######################################################################################################################################################################

#Variável contator.
x = 1
#Variáveis acumuladoras.
totalJuros = 0
totalPago = 0

#O usuário irá digitar o valor da divída a ser pago, que será armazenado na variável valorDivida.
valorDivida = float(input("Digite o valor da dívida: "))
#O usuário irá digitar o valor do juros mensal a ser pago, que será armazenado na variável jurosMensal.
jurosMensal = float(input("Digite o valor do juros mensal: "))
#O usuário irá digitar o valor que ele quer pagar por mês para quitar a divída, que será armazenada na variável valorPago. 
valorPago = float(input("Digite o valor pretendido a ser pago: "))

#Será feito um calculo para saber a quantidade de meses que a divída será paga, que será armazenada na variável qtdMeses.
qtdMeses = valorDivida / valorPago

#Enquanto x for maior que qtdMeses, o laço While continuará a fazer tudo que estiver dentro dele.
while x <= qtdMeses:
    #Será feito um calculo para saber o valor do juros, que será armazenada na variável juros.
    juros = valorPago * (jurosMensal / 100)
    #Será feito um calculo para saber o total de juros a ser pago, que será armazenado na variável totalJuros.
    totalJuros = totalJuros + juros
    #Será feito um calculo para saber o valor da parcela com juros, que será armazenada na variável valorPagoMes.
    valorPagoMes = valorPago + juros
    #Será feito um calculo para saber o total a ser pago com juros, que será armazenado na variável totalPago.
    totalPago = qtdMeses * valorPagoMes
    #O valor do x será incrementado.
    x = x + 1

#Se a quantidade de meses for maior que 1, será mostrada uma mensagem para o usuário com a quantidade de meses.
if qtdMeses > 1:
    print(f"A dívida será paga em {qtdMeses} meses.")
#Senão for maior que 1, será mostrada uma outra mensagem diferente para o usuário.
else:
    print(f"A dívida será paga em {qtdMeses} mês.")

#Será impresso na tela uma mensagem com o total da divída a ser pago pelo usuário.
print(f"O valor total pago será de R${totalPago}")
#Será impresso na tela uma mensagem com o total de juros a ser pago pelo usuário.
print(f"O valor total de juros pago foi de R${totalJuros}")    
