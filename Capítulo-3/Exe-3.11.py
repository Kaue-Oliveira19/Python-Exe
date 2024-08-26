#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Celular: 11 94100-2656
#
#Exercício 3.11 - Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
#######################################################################################################################################################################

#O usuário irá digitar o valor da mercadoria, que será armazenado na variável ValorMercadoria.
ValorMercadoria = float(input("Digite o valor da mercadoria: "))
#O usuário irá digitar o percentual de desconto, que será armazenado na variável PercDesconto.
PercDesconto = int(input("Digite o percentual de desconto: "))

#Será realizado um calculo para saber o valor do desconto, que irá ser armazenado na variável ValorDesconto.
ValorDesconto = ValorMercadoria * (PercDesconto / 100)
#Será realizado um calculo para saber o novo valor da mercadoria com desconto, que será armazenado na variável ValorPagar.
ValorPagar = ValorMercadoria - ValorDesconto

#Será impresso na tela o valor do desconto e o novo valor da mercadoria.
print(f"Valor do desconto: R${ValorDesconto} - Valor a pagar: R${ValorPagar}")
