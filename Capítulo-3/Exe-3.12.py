#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Celular: 11 94100-2656
#
#Exercício 3.12 - Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
#######################################################################################################################################################################

#O usuário irá digitar a distância da viagem, que será armazenado na variável Distancia.
Distancia = float(input("Digite a distância da viagem: "))
#O usuário irá digitar a velocidade média do carro na viagem, que será armazenada na variável VeloMedia.
VeloMedia = float(input("Digite a velocidade média do carro: "))

#Será realizado um calculo para saber o tempo de viagem, o resultado irá ser armazenado na variável TempoViagem.
TempoViagem = Distancia / VeloMedia

#Será impresso na tela o tempo de viagem.
print(f"O tempo de viagem será de {TempoViagem}")
