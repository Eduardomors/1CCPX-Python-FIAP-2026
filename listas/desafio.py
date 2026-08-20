idade_usuario = int(input("digite sua idade: "))

if idade_usuario < 16:
    print("Voto Proibido")
elif idade_usuario >= 16 and idade_usuario <= 18:
    print("Voto opcional")
elif idade_usuario >= 18 and idade_usuario <= 70:
    print("Voto obrigatorio")
elif idade_usuario > 70:
    print("Voto opcional")
else:
    print("Erro!!")