#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: laueoliveira3002@gmail.com - Celular: 11 94100-2656
#
#Exercício 3.10 - Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e
#do novo salário.
#######################################################################################################################################################################

#O usuário irá digitar o valor do salário, que será armazenado na variável Salario.
Salario = float(input("Digite o valor do salário: "))
#O usuário irá digitar o valor da porcentagem de aumento de salário, que será armazenado na variável Porcentagem. 
Porcentagem = int(input("Digite o valor da porcentagem de aumento: "))

#Será realizado um calculo para saber o valor do salário novo com aumento, o resultado será armazenado na variável NovoSalario.
NovoSalario = Salario + (Salario * (Porcentagem / 100))

#Será impresso na tela o novo valor do salário.
print(f"O valor do novo salário é de R${NovoSalario}")
