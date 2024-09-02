#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Número: 11 94100-2656
#
#Exercício 5.6 - Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2 = 4...
#######################################################################################################################################################################

#Variável contador
x = 1
#O usuário irá digitar o número da tabuada que ele quer saber, que será armazenado na variável tabuada.
tabuada = int(input("Digite o número da tabuada que você quer saber: "))

#Enquanto x for menor ou igual a 10, o laço While continuará a realizar tudo que estiver dentro dele.
while x <= 10:
    #Será feito o calculo de multiplicação, que será armazenado na variável calculo.
    calculo = tabuada * x
    #Será impresso na tela o resultado da tabuada.
    print(f"{tabuada} X {x} = {calculo}")
    #A variável x será incrementada.
    x = x + 1

