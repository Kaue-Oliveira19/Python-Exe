#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Celular: 11 94100-2656
#
#Exercício 2.6 - Modifique o programa 2.2, de forma que ele calcule um aumento de 15% para um salário de R$750.
#######################################################################################################################################################################

#Variáveis.
Salario = 750
PercAumento = 15

#Será realizado um calculo para saber o valor do novo salário, que irá ser armazenado na variável AumentoSalario.
AumentoSalario = Salario + (Salario * (PercAumento / 100))

#Será impresso na tela o salário antigo e o novo.
print(f"Salário antigo: R${Salario} - Salário novo: R${AumentoSalario}")
