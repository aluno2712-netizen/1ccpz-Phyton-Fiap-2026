#Operadores lógicos
#Or, and, not
#Lógica, and

print()

verifica_email= True
verifica_senha= True

login = verifica_email and verifica_senha
print(login)

if login:
    print("Entrar no sistema")

if not login:
    print("Ow... seja mais inteligente! Loga ai...")

print()

nota_final= 3

if nota_final < 4:
    print('Reprovado')
elif nota_final < 6:
    print("Recuperação")
else:
    print("Aprovado")

print("Fim")
