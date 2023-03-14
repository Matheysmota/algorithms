# exercício 1 - Suponha que você tem uma lista com 128 nomes e esteja fazendo uma pesquisa binária. 
# Qual seria o número máximo de etaps que levaria para encontrar o número desejado, e como seria o
# algoritmo que resolve este problema?

import math

steps = math.log2(128)
list = ["Ana", "Bia", "Cesar", "David", "Elias", "Felipe", "Gabriel", "Hugo", "Isabela", 
        "João", "Karen", "Leandro", "Maria", "Natalia", "Oliver", "Paula", "Queila", "Rafael", 
        "Sofia", "Thiago", "Ursula", "Viviane", "Wagner", "Xavier", "Yago", "Zoe"]
item = "Sofia"

def binary_search_first_exercise(array, item, right=0, left=None):
    if left is None:
        left = len(array)-1
     
    if right <= left:
        mid =  (right + left)//2
        if array[mid] == item:
            return mid
        elif item < array[mid]:
            return binary_search_first_exercise(array, item, right, mid - 1)
        else:
            return binary_search_first_exercise(array, item, mid + 1, left)
        
    return None

index = binary_search_first_exercise(list, item)

if (index == None):
    print("Exercício 1 - Nome não encontrado na lista") 
else:
    print(f"Exercício 1 - O nome {item} está na posição {index} da lista, além disso o número de passos foi {steps}")
