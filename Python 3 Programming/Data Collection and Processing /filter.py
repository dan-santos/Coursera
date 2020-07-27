def keep_evens(nums):
    new_list = []
    for num in nums:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))

#-----------------------------------------------
#filter: foreach que aplica o condicional passado como parametro para acada elemento da lista
#se a resposta for True, esse elemento é armazenado dentro de uma nova "lista" que será retornada
#Não devolve uma lista apesar de se comportar como uma. É recomendável o casting

def keep_evens(nums):
    new_seq = filter(lambda num: num % 2 == 0, nums)
    return list(new_seq)

print(keep_evens([3, 4, 6, 7, 0, 1]))