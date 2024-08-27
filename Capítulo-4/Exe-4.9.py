#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gamil.com - Celular: 11 94100-2656
#
#Exercício 4.9 - Escreva um programa para aprovar o empréstimo  bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a
#quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar
#dividido pelo número de meses a pagar.
#######################################################################################################################################################################

#O usuário irá digitar o valor da casa, que será armazenado na variável ValorCasa.
ValorCasa = float(input("Digite o valor da casa: "))
#O usuário irá digitar o valor do salário, que será armazenado na variável Salario.
Salario = float(input("Digite o valor do seu salário: "))
#O usuário irá digitar a quantidade de anos que ele quer pagar a casa, que será armazenado na variável AnosPagar.
AnosPagar = int(input("Digite a quantidade de anos que você desaja pagar a casa: "))

#Será realizado um calculo para saber o valor das prestações, que irá ser armazenado na variável Prestacao.
Prestacao = ValorCasa / (AnosPagar * 12)

#Se 30% do salário for menor do que a prestação da casa, o empréstimo não é concedido.
if Salario * (30 / 100) < Prestacao:
    #Será impresso na tela que o empréstimo não foi concedido.
    print("Empréstimo não concedido!")
#Se 30% do salário for maior que a prestação da casa, o empréstimo é concedido.
else:
    #Será impresso na tela que o empréstimo foi concedido e também irá ser mostrado o valor da prestação da casa.
    print(f"Emprétimo concedido. As prestações serão de R${Prestacao:5.2f}")
