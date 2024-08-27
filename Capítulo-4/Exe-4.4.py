#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Celular: 11 94100-2656
#
#Exercício 4.4 - Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumneto. Para salários superiores a R$1.250,00, calcule um aumento de
#10%. Para os inferiores ou iguais, de 15%.
#######################################################################################################################################################################

#O usuário irá digitar o salário do funcionário, que será armazenado na variável Salario.
Salario = float(input("Digite o salário do funcionário: "))

#Se o salário for maior que 1.250, ele receberá um aumento de 10%.
if Salario > 1.250:
    #Irá ser feito o calculo do aumento de salário, que será armazenado na variável SalarioNovo.
    SalarioNovo = Salario + (Salario * (10 / 100))
    #Será impresso na tela o valor do novo salário.
    print(f"Novo Salário: {SalarioNovo:5.2f}")

#Se o salário for menor ou igual a 1.250, ele receberá um aumento de 15%.
if Salario <= 1.250:
    #Irá ser feito o calculo do aumento de salário, que será armazenado na variável SalarioNovo.
    SalarioNovo = Salario + (Salario * (15 / 100))
    #Será impresso na tela o valor do novo salário.
    print(f"Novo Salário: {SalarioNovo:5.2f}")
