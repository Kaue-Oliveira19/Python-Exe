#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Celular: 11 94100-2656
#
#Exercício 3.15 - Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ela já
#fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
#######################################################################################################################################################################

#O usuário irá digitar a quantidade de cigarros que ele fuma por dia, que será armazenada na variável CigFumandos.
CigFumados = int(input("Digite a quantidade de cigarros fumados por dia: "))
#O usuário irá digitar a quantidade de anos que ele fumou, que será armazenada na variável QtdAnos.
QtdAnos = int(input("Digite a quantidade de anos em que fumou: "))

#Será realizado um calculo para saber quantos dias de vida a pessoa perdeu, que irá ser armazenado na variável DiasPerdidos.
DiasPerdidos = QtdAnos * ((CigFumados * 10) * 365) / 1400

#Será impresso na tela a quantidade de dias de vida perdido.
print(f"Você perdeu {DiasPerdidos:0.0f} dia(s).")
