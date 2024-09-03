#######################################################################################################################################################################
#Nome: Kauê Oliveira - Curso: Ciência da Computação - Email: kaueoliveira3002@gmail.com - Número: 11 94100-2656
#
#Exercício 5.10 - Modifique o programa anterior para que aceite respostas com letras maiúsculas e minúsculas em todas as questões.
#######################################################################################################################################################################

#Variáveis
pontos = 0
questao = 1

#Enquanto o valor da variável questao for menor ou igual 3, o laço continuará a funcionar.
while questao <= 3:
    #O usuário irá digitar a resposta, que será armazenado na variável resposta.
    resposta = input(f"Resposta da questão {questao}: ")
    #Se o valor da variável questao for igual a 1 e o valor da variável resposta for igual a "b" ou "B", será feito tudo que tiver dentro da condição.
    if questao == 1 and resposta == "b" or resposta == "B":
        #Será feito uma soma e irá ser armazenado na variável pontos.
        pontos = pontos + 1
    #Se o valor da variável questao for igual a 2 e o valor da variável resposta for igual a "a" ou "A", será feito tudo que tiver dentro da condição.
    if questao == 2 and resposta == "a" or resposta == "A":
        #Será feito uma soma e irá ser armazenado na variável pontos.
        pontos = pontos + 1
    #Se o valor da variável questao for igual a 3 e o valor da variável resposta for igual a "d" ou "D", será feito tudo que tiver dentro da condição.
    if questao == 3 and resposta == "d" or resposta == "D":
        #Será feito uma soma e irá ser armazenado na variável pontos.
        pontos = pontos + 1

    #A variável questao será incrementada.
    questao = questao + 1

#Será impresso na tela a quantidade de pontos.
print(f"O aluno fez {pontos} ponto(s)")
