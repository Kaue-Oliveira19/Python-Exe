#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Celular: 11 94100-2656
#
#Exercício 3.14 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o
#carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$ 0.15 por km rodado.
#######################################################################################################################################################################

#O usuário irá digitar a quantidade de kilometros que ele andou com o carro, que será armazenado na variável KmPercorridos.
KmPercorridos = float(input("Digite a quantidade de kilometros percorrido pelo carro: "))
#O usuário irá digitar a quantidade de dias que ele alugou o carro, que será armazenado na variável DiasAlugados.
DiasAlugados = int(input("Digite a quantidade de dias que o carro foi alugado: "))

#Será realizado um calculo para saber o preço a ser pago pelo aluguel do carro.
PrecoPagar = (DiasAlugados * 60) + (KmPercorridos * 0.15)

#Será impresso na tela o valor a ser pago pelo aluguel do carro.
print(f"Valor a ser pago: R${PrecoPagar}")
