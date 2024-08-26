#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Celular: 11 94100-2656
#
#Exercício 2.5 - Escreva um programa que calcule a soma de três variáveis e imprima o resultado na tela.
#######################################################################################################################################################################

#Será pedido para o usuário digitar três números.
print("Digite três número para a soma: ")
#O usuário irá digitar um número, que será armazenado na variável Num1.
Num1 = float(input())
#O usuário irá digitar um número, que será armazenado na variável Num2.
Num2 = float(input())
#O usuário irá digitar um número, que será armazenado na variável Num3.
Num3 = float(input())

#Será feito um calculo, que será armazenado na variável Calculo.
Calculo = Num1 + Num2 + Num3

#Será impresso na tela o resultado da soma.
print(f"{Num1} + {Num2} + {Num3} = {Calculo}")
