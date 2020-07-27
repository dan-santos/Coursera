things = [2, 5, 9]

yourlist = [value * 2 for value in things]

print(yourlist)

# [retorno for iterador in lista/dicionario/tupla (condicional)]

things = [3, 4, 6, 7, 0, 1]
#chaining together filter and map:
# first, filter to keep only the even numbers
# double each of them
print(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things)))

# equivalent version using list comprehension
print([x*2 for x in things if x % 2 == 0])