frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece {} vezes'.format(frase.count('a')))
print('A letra A aprarece na posição {}'.format(frase.find('a')+1))
print('A letra A aparece pela última vez na posição {}'.format(frase.rfind('a')+1))