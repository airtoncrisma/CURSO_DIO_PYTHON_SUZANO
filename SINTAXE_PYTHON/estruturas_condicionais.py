# Identação e Blocos
# def sacar(valor):
#     saldo = 500

#     if saldo >+ valor:
#         print("Valor sacado!")
#         print("Retire o seu dinheiro na boca do caixa.")
#     print("Obrigado por ser nosso cliente, tenha um bom dia!")

# def depositar(valor):
#     saldo = 500
#     saldo += valor
# sacar(400)


# Estruturas condicionais


# saldo = 2000.0
# saque = float(input("INforme o valor do saque: "))

# if saldo >= saque:
#     print("Realizando saque!")

# if saldo < saque:
#     print("Saldo insuficiente!")



MAIOR_IDADE = 18
IDADE_ESPECIAL = 16
idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar CNH.")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")
else:
    print("Ainda não pode tirar CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar CNH.")


