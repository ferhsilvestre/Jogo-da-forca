secreto = 'python'
digitadas = []
chances = 3

while True:
    if chances < 1:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ').lower()

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra "{letra}" existe na palavra secreta!')
    else:
        print(f'A letra "{letra}" NÃO existe na palavra secreta!')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    
    if secreto_temporario == secreto: 
        print(f'Você ganhou! A palavra era {secreto_temporario.capitalize()}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario.capitalize()}')
    
    if letra not in secreto:
        chances -= 1
    
    print(f'Você ainda tem {chances} chances.')
    print()