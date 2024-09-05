#######################################################################################################################################################################
#Nome : Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Número: 11 94100-2656
#
#Exercício 5.11 - Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva
#o total ganho com juros no período.
#######################################################################################################################################################################

#Variável contador.
x = 1
#Variável acumuladora.
totalGanho = 0

#O usuário irá digitar o valor do depósito inicial, que será armazenada na variável depInicial.
depInicial = float(input("Digite o depósito inicial: "))
#O usuário irá digitar o valor da taxa de juros da poupança, que será armazenado na variável taxJuros.
taxJuros = float(input("Digite a taxa de juros da poupança: "))

#Enquanto x for menor ou igual a 24, o laço fará tudo que estiver dentro dele.
while x <= 24:
    #Será feito um calculo para saber o novo valor do depósito inicial com a taxa de juros da poupança, que será armazenado na variável calculo.
    calculo = depInicial + (depInicial * (taxJuros / 100))
    #O valor do depósito inicial com a taxa de juros da poupança dos 24 meses será armazenado na variável totalGanho.
    totalGanho = calculo + totalGanho
    #O valor da variável x irá ser incrementado.
    x = x + 1

#Será impresso na tela do usuário o valor total do depósito inicial com a taxa de juros da poupança dos 24 meses.
print(f"Total ganho com os juros nos primeiros 24 meses: {totalGanho}")
