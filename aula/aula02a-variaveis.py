print("Olá mundo")

print (7 + 4)
print("7" + "4")  # Contatenação de strings

'''
comentario de múltiplas linhas
'''

# VARIÁVEIS
nome = "Brenno" # str
idade = 17 # int
peso = 70.2 #float

print(nome, idade, peso)
print(f"oiii, {nome}!!")

# INPUTS - SIMULAÇÃO DE FORMULARIOS NO CMD
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

nova_idade = idade + 1
print(nome, idade)
print(nova_idade)


# Exercícios
nome = input("Digite seu nome")
print(f"Seja bem vindo {nome}")

dia_nascimento = int(input("Digite seu dia de nascimento"))
mes_nascimento = int(input("Digite seu mes de nascimento: "))
ano_nascimento = int(input("Digite seu ano de nascimento: "))
print(f"Voce nasceu dia {dia_nascimento} de {mes_nascimento} do ano de {ano_nascimento}")