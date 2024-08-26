#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Celular: 11 94100-2656
#
#Exercício 3.13 - Escreva um programa que converta uma temperatura digitada em ºC em ºF. A formula para essa conversão é: F = (9 * C / 5 ) + 32
#######################################################################################################################################################################

#O usuário irá digitar a temperatura em Celsius, que será armazenada na variável TempCelsius.
TempCelsius = float(input("Digite a temperatura em Celsius(ºC): "))

#Será realizado um calculo para a conversão de Celsius para Fahrenheit.
TempFahrenheit = (9 * Celsius / 5 ) + 32

#Será impresso na tela a conversão de Celsius para Fahrenheit.
print(f"{TempCelsius}ºC = {TempFahrenheit}ºF")
