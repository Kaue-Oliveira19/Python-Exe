#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Número: 11 94100-2656
#
#Exercício 6.2 - Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.
#######################################################################################################################################################################

#Listas.
L1 = []
L2 = []
L3 = []
#Variável contador.
x = 0

#Enquanto o laço While for verdadeiro, será feito tudo que estiver dentro dele.
while True:
    #Será pedido ao usuário para digitar números inteiros, que será armazenado na variável elem.
    elem = int(input("Lista 1 - Digite números inteiros. A ação será para quando for digitado 0: "))
    #Se o número digitado pelo usuário for igual a zero, o laço while termina.
    if elem == 0:
        break
    #Os valores da variável elem são colocados na lista L1. 
    L1.append(elem)

#Enquanto o laço While for verdadeiro, será feito tudo que estiver dentro dele.
while True:
    #Será pedido ao usuário para digitar números inteiros, que será armazenado na variável elem.
    elem = int(input("Lista 2 - Digite números inteiros. A ação será para quando for digitado 0: "))
    #Se o número digitado pelo usuário for igual a zero, o laço while termina.
    if elem == 0:
        break
    #Os valores da variável elem são colocados na lista L2.
    L2.append(elem)

#É feito a soma das lista, e os valores serão armazenados na lista L3.
L3 = L1 + L2

#Será impresso na tela do usuário os valores da lista L3.
print(L3)
        
