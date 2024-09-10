#######################################################################################################################################################################
#Nome : Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Número: 11 94100-2656
#
#Exercício 5.16 - Execute o Programa 5.1 para os seguintes valores 501, 745, 384, 2, 7 e 1.
#######################################################################################################################################################################

#O usuário irá digitar um valor, que será armazenado na variável valor.
valor = int(input("Digite o valor a pagar: "))
#Variável onde será armazenada a quantidade de cédulas.
cedulas = 0
#
atual = 50
#
apagar = valor

#Enquanto a condição for verdadeira, o laço While será rodado.
while True:
    #Se o valor da variável atual for menor ou igual ao valor da variável apagar, a condição será rodada.
    if atual <= apagar:
        #O valor da variável apagar será incrementado.
        apagar -= atual
        #O valor da variável cedulas será incrementado.
        cedulas += 1
    #Se a condição if for falsa, a condição else será rodada.
    else:
        #Será impresso na tela a quantidade de cédulas e o valor das cédulas.
        print(f"{cedulas} cédula(s) de R${atual}")
        #Se o valor da variável apagar for igual a 0, será rodado tudo que estiver dentro da condição.
        if apagar == 0:
            #O programa será finalizado.
            break
        #Se o valor da variável atual for igual a 50, será tudo rodado dentro da condição if.
        if atual == 50:
            #A variável atual receberá o valor de 20.
            atual = 20
        #Se o valor da variável atual for igual a 20, será tudo rodado dentro da condição if.    
        elif atual == 20:
            #A variável atual receberá o valor de 10.
            atual = 10
        #Se o valor da variável atual for igual a 10, será tudo rodado dentro da condição if.    
        elif atual == 10:
            #A variável atual receberá o valor de 5.
            atual = 5
        #Se o valor da variável atual for igual a 5, será tudo rodado dentro da condição if.    
        elif atual == 5:
            #A variável atual receberá o valor de 1.
            atual = 1
        #O valor da variável cedulas receberá o valor de 0.
        cedulas = 0
