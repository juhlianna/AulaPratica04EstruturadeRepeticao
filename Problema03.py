#um cinema cobra precos diferentes para os ingressos de acordo coma idade de uma pessoas. se a pessoa tiver menos de 3 de idade, o ingresso sera gratuito, se tiver entre 3 e 12 anos, o ingresso custara R$15, se tiver mais de 12 anos , custara R$ 30
total = 0
dinheiro = 0

while True:
    idade = input('qual sua idade?')
    if idade == 'sair':
        break

    idade = int(idade)
    total += 1
    if idade < 3:
        ingresso = 0
        print('o ingresso é gratuito')
    else:
        if idade > 12:
            ingresso = 30
            print('o ingresso custa R$ 30')
        else:
            ingresso = 15
            print('o ingresso custa R$ 15')
dinheiro += ingresso

media = dinheiro / total
print('Total de pessoas: {}'.format(total))
print('Total arrecadado: {}'.format(dinheiro))
print('Média arrecadada: {} '.format(media))








