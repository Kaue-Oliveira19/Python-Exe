#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmailo.com - Celular: 11 941000-2656
#
#Exercício 4.2 - Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
#Nesse caso, exiba o valor da multa, cobrando R$5 por km acima de 80 km/h.
#######################################################################################################################################################################

#O usuário irá digitar a velocidade do carro, que será armazenado na variável VeloCarro.
VeloCarro = float(input("Digite a velocidade do carro: "))

#Se a velocidade do carro for maior que 80, ele será multado.
if VeloCarro > 80:
    #Será realizado o calculo para saber o valor da multa, que irá ser armazenado na variável Multa.
    Multa = (VeloCarro - 80) * 5
    #Será impresso na tela uma mensagem, dizendo que o usuário foi multado e também aparecerá o valor da multa.
    print(f"Você foi multado em R${Multa}, por execesso de velocidade.")
