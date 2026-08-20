# OPERADORES DE ATRIBUIÇÃo
from sqlalchemy.sql.operators import truediv

num = 15
print(num)

num = num + 2
print(num) # 17

num += 2
print(num) # 19

# OPERADORES RELACIONAIS
print() #pular linha
print(6 == 3) # booleano
print(6 > 3)
print(6 < 3)

idade = 20
print(idade == 20)

maior_idade = idade >= 18
print(maior_idade)

#OPERADORES LOGICOS
#LOGICA E (and)
print()

verifica_email = False
verifica_senha = True

login = verifica_email and verifica_senha
print(login)

if not login:
    print("Entrar no programa")

print()
# NOTAS...
nota_final = int(input("Digite sua nota: "))

if nota_final < 4:
    print("Reprovado")
elif nota_final < 6:
    print("Recuperação")
else:
    print("Aprovado")


print("FIM")