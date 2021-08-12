#Gerador de senhas aleatórias.
import random

#Checagem de input para validação de um número inteiro (incompleto):
quantidade_caracteres = int(input("Que tamanho sua senha deve ter? [Mínimo 8 caracteres] "))
if type(quantidade_caracteres) != int:
    print("Opção invalida. Digite apenas números. Por favor tente novamente.")

#Listas de caracteres que podem ser usados:
caracteres = ['1', '2', '3', '4', '5', '6', '7', '8', '9',\
    'a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',\
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',\
            '$','&','_','-']

#Randomizador que pega caracteres das listas para formar a senha:
nsenha = ''
if quantidade_caracteres <= 8:
    for i in range(8):
        senha = random.choice(caracteres)
        nsenha += senha
    print(f'Sua nova senha é: {nsenha} ')
else:
    for i in range(quantidade_caracteres):
        senha = random.choice(caracteres)
        nsenha += senha
    print(f'Sua nova senha é: {nsenha} ')
