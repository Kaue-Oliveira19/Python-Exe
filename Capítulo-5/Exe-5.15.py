#######################################################################################################################################################################
#Nome : Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Número: 11 94100-2656
#
#Exercício 5.15 - Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade
#comprada. Utilize a tabela de códigos a seguir para obter o preço de cada produto:
#
# | Cógigo | Preço |
# |   1    | 0,50  |
# |   2    | 1,00  |
# |   3    | 4,00  |
# |   5    | 7,00  |
# |   9    | 8,00  |
#
#Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve gerar a mensagem de erro "Código inválido".
#######################################################################################################################################################################

#Variável acumuladora.
total = 0

#Enquanto o laço While for verdadeiro, o laço continuará a fazer tudo que estiver dentro dele.
while True:
    #O usuário irá digitar o código do produto, que será armazenado na variável codProduto.
    codProduto = int(input("Digite o código do produto: "))
    #Se o código do produto for igual a 0, o programa irá mostrar uma mensagem e também vai parar o laço While.
    if codProduto == 0:
        #Será impresso na tela uma mensagem com o total da compra.
        print(f"O total das compras foi de R${total:.2f}")
        #O programa para.
        break
    #O usuário irá digitar a quantidade do produto, que será armazenado na variável qtdCompra.
    qtdComprada = int(input("Digite a quantidade do produto: "))

    #Se o código do produto for igual a 1, será rodado tudo que estiver dentro desta condição.
    if codProduto == 1:
        #Será calculado o total da compra, que será armazenado dentro da variável total.
        total = total + qtdComprada * 0.50
    #Se o código do produto for igual a 2, será rodado tudo que estiver dentro desta condição.
    elif codProduto == 2:
        #Será calculado o total da compra, que será armazenado dentro da variável total.
        total = total + qtdComprada * 1.00
    #Se o código do produto for igual a 3, será rodado tudo que estiver dentro desta condição.
    elif codProduto == 3:
        #Será calculado o total da compra, que será armazenado dentro da variável total.
        total = total + qtdComprada * 4.00
    #Se o código do produto for igual a 5, será rodado tudo que estiver dentro desta condição.
    elif codProduto == 5:
        #Será calculado o total da compra, que será armazenado dentro da variável total.
        total = total + qtdComprada * 7.00
    #Se o código do produto for igual a 9, será rodado tudo que estiver dentro desta condição.
    elif codProduto == 9:
        #Será calculado o total da compra, que será armazenado dentro da variável total.
        total = total + qtdComprada * 8.0
    #Se o código do produto não for igual as outras condições, será rodado tudo que estiver dentro do Else.
    else:
        #Será impresso na tela dizendo que o código digitado é inválido.
        print("Código inválido.")
        
