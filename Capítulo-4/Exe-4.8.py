#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Celular: 11 94100-2656
#
#Exercício 4.8 - Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma(+), subtração(-),
#multiplicação(*) e divisão(/). Exiba o resultado da operação solicitada.
#######################################################################################################################################################################

#Será impresso uma mensagem ao usuário para digitar dois números.
print("Digite dois números: ")
#Os números digitados serão armazenados nas variáveis Num1 e Num2.
Num1 = float(input())
Num2 = float(input())
#O usuário irá digitar qual operação matemática ele deseja realizar, que será armazenado na variável Operador.
Operador = str(input("Qual operação matemática você deseja realizar(Soma, subtração, multiplicação ou divisão): "))

#Se a variável Operador foi igual as condições estabelecidas, ele irá para o calculo da soma.
if Operador == "Soma" or Operador == "soma":
    #Será feito uma soma com as variáveis Num1 e Num2.
    Soma = Num1 + Num2
    #Será impresso na tela o resultado da soma.
    print(f"Num1 + Num2 = {Soma}")
#Se a variável Operador foi igual as condições estabelecidas, ele irá para o calculo da subtração.
elif Operador == "Subtração" or Operador == "subtração" or Operador == "Subtracao" or Operador == "subtracao":
    #Será feito uma subtração com as variáveis Num1 e Num2.
    Subtracao = Num1 - Num2
    #Será impresso na tela o resultado da subtração.
    print(f"Num1 - Num2 =  {Subtracao}")
#Se a variável Operador foi igual as condições estabelecidas, ele irá para o calculo da multiplicação.
elif Operador == "Multiplicação" or Operador == "multiplicação" or Operador == "Multiplicacao" or Operador == "multiplicacao":
    #Será feito uma multiplicação com as variáveis Num1 e Num2.
    #Será impresso na tela o resultado da multiplicação.
    Multiplicacao = Num1 * Num2
    print(f"Num1 * Num2 = {Multiplicacao}")
#Se a variável Operador foi igual as condições estabelecidas, ele irá para o calculo da divisão.
elif Operador == "Divisão" or Operador == "divisão" or Operador == "Divisao" or Operador == "divisao":
    #Será feito uma divisão com as variáveis Num1 e Num2.
    Divisao = Num1 / Num2
    #Será impresso na tela o resultado da divisão.
    print(f"Num1 / Num2 = {Divisao}")
