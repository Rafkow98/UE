def funkcja_listy(l1: list, l2: list) -> list:
    for i in l2:
        if i not in l1:
            l1.append(i)
    l1 = [i**3 for i in l1]
    return l1


lista1 = [1, 23, 5, 3, 2, 4, 5, 2]
lista2 = [1, 2, 5, 11, 5, 4, 9, 8]
print(funkcja_listy(lista1, lista2))
