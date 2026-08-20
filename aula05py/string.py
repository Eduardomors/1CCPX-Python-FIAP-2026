# texto = "fiap paulista"
#
# print(texto[0])
# print(texto[1])
# print(texto[2])
# print(texto[3])
#
# tamanho_texto = len(texto)
# print(tamanho_texto)
#
# # for i in range(tamanho_texto):
# #     print(f"texto[{i}] = (texto{i})")
#
# for c in texto:
#     print(c)
lista_frutas = ["morango", "maça","uva"]

lista_frutas[0] = "morango"
lista_frutas[1] = "maça"
lista_frutas[2] = "uva"
print(lista_frutas[1])

lista_frutas.append("melancia")
print(lista_frutas[3])

for i in range(len(lista_frutas)):
     print(i)

print()

for fruta in lista_frutas:
    print(fruta)
