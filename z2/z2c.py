def parzyste(liczby):
    for liczba in liczby:
        if liczba % 2 == 0:
            print(liczba)


parzyste(range(0, 10, 1))
