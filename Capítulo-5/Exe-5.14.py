#######################################################################################################################################################################
#Nome : Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Número: 11 94100-2656
#
#Exercício 5.14 - Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução,
#exiba a quantidade de números digitados, assim como a soma e a média aritmética.
#######################################################################################################################################################################

#Variável contador.
x = 0
#Variável acumuladora.
soma = 0

#Enquanto o laço While for verdadeiro, o laço continuará a realizar tudo que estiver dentro dele.
while True:
    #O usuário irá digitar um número inteiro.
    num = int(input("Digite um número inteiro: "))
    #Será somado os números digitados, que será armazenado na variável soma.
    soma = soma + num

    #O valor da variável x será incrementado.
    x += 1
    #Se o valor da variável num for igual a zero, ele fará uma média aritmética com os valores digitados e o laço será parado.
    if num == 0:
        #Calculo para saber a média dos números digitados.
        media = soma / x
        #O laço será parado.
        break

#Será impresso na tela a quantidade de números a ser digitado.
print(f"A quantidade de números foi de {x}.")
#Será impresso na tela a média aritmética dos números digitados.
print(f"A média aritmética dos números é de {media}.")
