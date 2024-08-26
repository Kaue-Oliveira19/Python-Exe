#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Celular: 11 94100-2656
#
#Exercício 3.9 - Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundo.
#######################################################################################################################################################################

#O usuário irá digitar a quantidade de dias, que será armazenada na variável Dias.
Dias = int(input("Digite a quantidade de dias: "))
#O usuário irá digitar a quantidade de horas, que será armazenado na variável Horas.
Horas = int(input("Digite a quantidade de horas: "))
#O usuário irá digitar a quantidade de minutos, que será armazenada na variável Minutos.
Minutos = int(input("Digite a quantidade de minutos: "))
#O usuário irá digitar a quantidade de segundos, que será armazenada na variável Segundos.
Segundos = int(input("Digite a quantidade de segundos"))

#Será armazenado na variável TotalSegundos a quantidade total de segundos dos dias, horas, minutos e segundos.
TotalSegundos = Segundos + (Minutos * 60) + (Horas * 3600) + (Dias * 86400)

#Será impresso na tela o resultado de segundos totais.
print(f"O total de segundos é {TotalSegundos}")
