conteudo = [('daniel', 20, 'f santos'),
            ('daniella', 18, ' fc melo'),
            ('aline', 23, 'f santos')]

teste2 = open('teste2.csv', 'w')

teste2.write('Nome, Sobrenome, Idade\n')

for e in conteudo:
    row = ','.join([e[0], e[2], str(e[1])])
    teste2.write(row + '\n')
teste2.close()