f = open('teste.csv', 'r')
linhas = f.readlines()

cabec = linhas[0]
val = cabec.strip().split(',')
print(val)

for l in linhas[1:]:
    val = l.strip().split(',')
    print('{} | {} | {}'.format(val[0], val[1], val[2]))

f.close()