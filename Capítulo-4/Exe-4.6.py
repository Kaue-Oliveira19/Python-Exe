#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Celular: 11 94100-2656
#
#Exercício 4.6 - Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$0,50 por km para
#viagens de até de 200km, e R$0,45 para viagens mais longas.
#######################################################################################################################################################################

#O usuário irá digitar a distância da viagem em kilometros, que será armazenada na variável KmDesejados.
KmDesejados = float(input("Digite a distância da viagem em KM: "))

#Se a distância for menor ou igual a 200, será calculado o preço da passagem.
if KmDesejados <= 200:
    #Calculo do valor da passagem, que será armazenado na variável ValorPassagem.
    ValorPassagem = KmDesejados * 0.50
    #Será impresso na tela o valor da passagem.
    print(f"Valor da passagem: R${ValorPassagem}")
#Se a distância da viagem não for menor ou igual a 200, será feito um outro calculo com um valor diferente.
else:
    #Calculo do valor da passagem, que será armazenado na variável ValorPassagem.
    ValorPassagem = KmDesejados * 0.45
    #Será impresso na tela o valor da passagem.
    print(f"Valor da passagem: R${ValorPassagem}")
