#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Número: 11 94100-2656
#
#Exercício 5.7 - Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.
#######################################################################################################################################################################

#O usuário irá digitar o número da tabuada que ele quer saber, que será armazenada na variável tabuada.
tabuada = int(input("Digite o número da tabuada que você quer saber: "))
#O usuário irá digitar o início da tabuada, que será armazenado na variável iniTabuada.
iniTabuada = int(input("Digite o início da tabuada: "))
#O usuário irá digitar o final da tabuada, que será armazenado na variável fimTabuada.
fimTabuada = int(input("Digite o final da tabuada: "))

#Enquanto o valor da variável iniTabuada for menor ou igual ao valor da variável fimTabuada, o laço fará tudo que estiver dentro do While.
while iniTabuada <= fimTabuada:
    #Será feito o calculo da tabuada.
    resultado = tabuada * iniTabuada
    #Será impresso na tela o resultado da variável.
    print(f"{tabuada} X {iniTabuada} = {resultado}")
    #A variável iniTabuada será incrementada.
    iniTabuada = iniTabuada + 1
