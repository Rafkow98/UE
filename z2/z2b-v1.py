def lista(l1, l2, l3, l4, l5):
    liczby = [l1, l2, l3, l4, l5]
    liczbymnozone = []
    for liczba in liczby:
        liczbymnozone.append(liczba*2)
    return liczbymnozone


print(lista(3, 5, 4, 24, 5123))
