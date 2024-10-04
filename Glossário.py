#######################################################################################################################################################################
#Função PRINT - Informa que vamos exibir algo na tela.

print("Hello, World!")

#######################################################################################################################################################################
#Função LEN - Retorna o número de caracteres na string.

nome = "Kauê"
len(nome)
len("Kauê")

#######################################################################################################################################################################
#Concatenação de Strings - O conteúdo de variáveis string podem ser somados.

nome = "Kauê"
sobrenome = "Oliveira"

nome + " " + sobrenome

#######################################################################################################################################################################
#Composição de Strings - Colocar o contéudo ou valor das variáveis em uma mesma frase.

nome = "Kauê"
sobrenome = "Oliveira"
idade = 21

print("%s %s tem %d de idade." %(nome, sobrenome, idade))
print("{} {} tem {} de idade." .format(nome, sobrenome, idade))
print(f"{nome} {sobrenome} tem {idade} de idade.")

#######################################################################################################################################################################
#Fatiamento de Strings - Definimos quais caracteres da string irão aparecer

nome = "Kauê"

nome[0:2]

#######################################################################################################################################################################
#Função Input - Entrada de dados

nome = str(input("Digite o seu nome: "))

print(nome)

#######################################################################################################################################################################
#Estrutura de condição If Else - Se a condição for verdadeira, faça algo, senão:

idade = int(input("Digite sua idade"))

if idade >= 18:
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.")

#Estrutura de condição If Else aninhado
num1 = 5
num2 = 10

if num1 == num2:
    print(f"Número iguais")
else:
    if num1 > num2:
        print(f"{num1} é o maior número")
    else:
        print(f"{num2} e o maior número")

if num1 == num2:
    print(f"Número iguais")
elif num1 > num2:
    print(f"{num1} é o maior número")
else:
    print(f"{num2} e o maior número")
#######################################################################################################################################################################

