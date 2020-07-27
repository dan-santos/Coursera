with open('teste.txt', 'w') as f:
    f.write('nova linha\n')

f = open('teste.txt', 'r')
print(f.readlines())
f.close()