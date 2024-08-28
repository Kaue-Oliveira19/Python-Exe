#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Celular: 11 94100-2656
#
#Exercício 5.3 - Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, ... 1, 0 e Fogo! na tela.
#######################################################################################################################################################################

#Variável contador.
x = 10

#Enquanto o valor da variável x for menor maior ou igual a 0, o laço continuará realizando tudo que estiver dentro dele.
while x >= 0:
    #Será impresso o valor da variável x.
    print(x)
    #A variável x será subtraída.
    x = x - 1

#Será impresso na tela uma mensagem, depois que o laço while for falso.
print("Fogo!")
