#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Número: 11 94100-2656
#
#Exercício 6.1 - Modifique o Programa 6.2 para ler 7 notas em vez de 5.
#######################################################################################################################################################################

#Lista chamada notas, onde os valores digitados serão armazenados.
notas = [0, 0, 0, 0, 0, 0, 0]
#Variável acumuladora.
soma = 0
#Variável contadora.
x = 0

#Enquanto o valor da variável número x for menor que 7, o laço While fará tudo que estiver dentro dele.
while x < 7:
    #O usuário irá digar o valores das notas, que será armazenado na lista notas.
    notas[x] = float(input(f"Nota {x}: "))
    #A variável soma irá receber os valores das notas.
    soma += notas[x]
    #O valor da variável x será incrementada.
    x += 1

#A variável x recebe um novo valor.
x = 0

#Enquanto o valor da variável número x for menor que 7, o laço While fará tudo que estiver dentro dele.
while x < 7:
    #Será impresso na tela 
    print(f"Nota {x}: {notas[x]:6.2f}")
    #O valor da variável x será incrementado.
    x += 1
#Será impresso na tela a média das notas.
print(f"Média: {soma / x:5.2f}")
