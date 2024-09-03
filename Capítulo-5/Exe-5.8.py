#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Número: 11 94100-2656
#
#Exercício 5.8 - Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e
#subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 x 5 = 5 + 5 + 5 + 5
# = 4 + 4 + 4 + 4 + 4.
#######################################################################################################################################################################

#Variável contador.
x = 1
#Variável acumuladora.
calculo = 0

#Será impresso na tela uma mensagem dizendo para o usuário digitar dois números.
print("Digite dois números: ")
#O primeiro número digitado vai ser armazenado na variável num1.
num1 = int(input())
#O segundo número digitado vai ser armazenado na variável num2.
num2 = int(input())

#Enquanto o valor da variável x for menor ou igual do que o valor da variável num2, o laço fará tudo que estiver dentro dela.
while x <= num2:
    #Será feito a soma para saber a multiplicação, que será armazenada na variável calculo.
    calculo = num1 + calculo
    #O valor da variável x será incrementado.
    x = x + 1

#Será impresso na tela o resultado da multiplicação.
print(f"{num1} X {num2} = {calculo}")
