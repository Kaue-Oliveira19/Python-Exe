#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Celular: 11 94100-2656
#
#Exercício 4.10 - Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação:
#R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir;
#
#  Preço por tipo e faixa de consumo
######################################
#Tipo        | Faixa(kWh)    | Preço #
#Residencial | Até 500       | R$0,40#
#            | Acima de 500  | R$0,65#
#Comercial   | Até 1000      | R$0,55#
#            | Acima de 1000 | R$0,60#
#Industrial  | Até 5000      | R$0,55#
#            | Acima de 5000 | R$0,60#
#######################################################################################################################################################################

#O usuário irá digitar a quantidade de kWh consumido, que será armazenado na variável kWhConsumido.
kWhConsumido = float(input("Digite a quantidade de kWh consumido: "))
#O usuário irá digitar o tipo de instalação, que será armazenada na variável TipoInstalacao.
TipoInstalacao = str(input("Digite o tipo de instalação (R para Residencial|I para Industrial|C para Comercial): "))

#Se a quantidade de kWh for menor ou igual a 500 e o tipo de instalação for igual a R(Residêncial), irá ser feito um calculo do consumo.
if kWhConsumido <= 500 and TipoInstalacao == "R":
    #Será realizado o calculo do consumo de kWh.
    Consumo = kWhConsumido * 0.40
    #Será impresso na tela o preço a pagar pelo consumo.
    print(f"O seu consumo foi de {Consumo:5.2f}kWh.")
#Se a quantidade de kWh for maior do que 500 e o tipo de instalação for igual a R(Residêncial), irá ser feito um calculo do consumo.
elif kWhConsumido > 500 and TipoInstalacao == "R":
    #Será realizado o calculo do consumo de kWh.
    Consumo = kWhConsumido * 0.65
    #Será impresso na tela o preço a pagar pelo consumo.
    print(f"O seu consumo foi de {Consumo:5.2f}kWh.")
#Se a quantidade de kWh for menor ou igual a 1000 e o tipo de instalação for igual a C(Comercial), irá ser feito um calculo do consumo.
elif kWhConsumido <= 1000 and TipoInstalacao == "C":
    #Será realizado o calculo do consumo de kWh.
    Consumo = kWhConsumido * 0.55
    #Será impresso na tela o preço a pagar pelo consumo.
    print(f"O seu consumo foi de {Consumo:5.2f}kWh.")
#Se a quantidade de kWh for maior do que 1000 e o tipo de instalação for igual a C(Comercial), irá ser feito um calculo do consumo.
elif kWhConsumido > 1000 and TipoInstalacao == "C":
    #Será realizado o calculo do consumo de kWh.
    Consumo = kWhConsumido * 0.60
    #Será impresso na tela o preço a pagar pelo consumo.
    print(f"O seu consumo foi de {Consumo:5.2f}kWh.")
#Se a quantidade de kWh for menor ou igual a 5000 e o tipo de instalação for igual a I(Industrial), irá ser feito um calculo do consumo.
elif kWhConsumido <= 5000 and TipoInstalacao == "I":
    #Será realizado o calculo do consumo de kWh.
    Consumo = kWhConsumido * 0.55
    #Será impresso na tela o preço a pagar pelo consumo.
    print(f"O seu consumo foi de {Consumo:5.2f}kWh.")
#Se a quantidade de kWh for maior do que 5000 e o tipo de instalação for igual a I(Industrial), irá ser feito um calculo do consumo.
elif kWhConsumido > 5000 and TipoInstalacao == "I":
    #Será realizado o calculo do consumo de kWh.
    Consumo = kWhConsumido * 0.60
    #Será impresso na tela o preço a pagar pelo consumo.
    print(f"O seu consumo foi de {Consumo:5.2f}kWh.")
