#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Número: 11 94100-2656
#
#Exercício 5.9 - Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto. Utilize apenas os operadores de
#soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos retirar
#o divisor do dividendo. Logo, 20 / 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.
#######################################################################################################################################################################

#Variável contadora.
y = 0

#Será impresso na tela uma mensagem dizendo para o usuário digitar dois números.
print("Digite dois números: ")
#A variável num1 receberá o primeiro valor digitado pelo usuário.
num1 = float(input())
#A variável num2 receberá o segundo valor digitado pelo usuário.
num2 = float(input())

#A variável x receberá o valor da variável num2.
x = num2
#A variável resultado receberá o valor da variável num1.
resultado = num1

#Enquanto o valor da variável num1 for maior do que o valor da variável x, ele continuará com laço.
while num1 >= x:
    #Será feito uma subtração, o novo valor ficará armazenada na variável resultado.
    resultado =  resultado - num2
    #A variável y funcionará como um contator, para saber quantas vezes a condição do laço foi verdadeiro.
    y = y + 1
    #O valor da variável da x será incrementado.
    x = x + num2

#Será impresso na tela o resultado da divisão.
print(f"{num1} / {num2} = {y:5.2f}")
