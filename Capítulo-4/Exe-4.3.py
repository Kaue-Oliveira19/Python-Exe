#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Celular: 11 94100-2656
#
#Exercício 4.3 - Escreva um programa que leia três números e que imprima o maior e o menor.
#######################################################################################################################################################################

#Irá pedir para o usuário digitar três números.
print("Digite três números: ")
#Os três números serão armazenados nas variáveis Num1, Num2 e Num3.
Num1 = float(input())
Num2 = float(input())
Num3 = float(input())

#Verifica se o valor da variável Num1 é maior do que as variáveis Num2 e Num3.
if Num1 > Num2 and Num1 > Num3:
#Irá imprimir na tela que o valor da variável Num1 é o maior em comparação com as variáveis Num2 e Num3.
    print(f"{Num1} é o maior número.")
#Verifica se o valor da variável Num2 é maior do que as variáveis Num1 e Num3.
if Num2 > Num1 and Num2 > Num3:
#Irá imprimir na tela que o valor da variável Num2 é o maior em comparação com as variáveis Num1 e Num3.
    print(f"{Num2} é o maior número.")
#Verifica se o valor da variável Num3 é maior do que as variáveis Num1 e Num2.
if Num3 > Num1 and Num3 > Num2:
#Irá imprimir na tela que o valor da variável Num3 é o maior em comparação com as variáveis Num1 e Num2.
    print(f"{Num3} é o maior número.")

#Verifica se o valor da variável Num1 é menor do que as variáveis Num2 e Num3.
if Num1 < Num2 and Num1 < Num3:
#Irá imprimir na tela que o valor da variável Num1 é o menor em comparação com as variáveis Num2 e Num3.
    print(f"{Num1} é o menor número.")
#Verifica se o valor da variável Num2 é menor do que as variáveis Num1 e Num3.
if Num2 < Num1 and Num2 < Num3:
#Irá imprimir na tela que o valor da variável Num2 é o menor em comparação com as variáveis Num1 e Num3.
    print(f"{Num2} é o menor número.")
#Verifica se o valor da variável Num3 é menor do que as variáveis Num1 e Num2.
if Num3 < Num1 and Num3 < Num2:
#Irá imprimir na tela que o valor da variável Num3 é o menor em comparação com as variáveis Num1 e Num2.
    print(f"{Num3} é o menor número.")




