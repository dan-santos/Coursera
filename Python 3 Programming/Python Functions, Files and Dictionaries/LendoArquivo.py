f = open('teste.txt', 'r')

#conteudo = f.read() #lê o arquivo inteiro e armazena em uma string

#l = f.readline()  # lê uma linha de cada vez

ls = f.readlines()
print('{} - {}'.format(ls, type(ls)))

#for line in ls:
    #print(line)

#print('{} - {}'.format(l, type(l)))
#print(conteudo)

f.close()
