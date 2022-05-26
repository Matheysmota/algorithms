#Os comentários representam como o algoritmo ficaria no primeiro looping

myList = [5, 4 , 4, 6, 7, 15, 1, 3] --> [5, 5] -> 4,5....

n = len(myList) #8
for i in range(1, n): #i variando de (1 até n) e somando de 1 em 1
    key = myList[i] #key vai receber o valor 4
    j = i - 1 #j vai receber o valor 0, ou seja j representa a primeira posição
    while j >= 0 and myList[j] > key: #enquanto 0 for maior ou igual a 0 && 5 > 4
        myList[j + 1] = myList[j] # a segunda posição (5) recebe o valor da primeira posição (4)
        j = j - 1 #a posição 0 recebe o valor -1
    myList[j+1] = key #a primeira posição recebe 4
    print(myList)
