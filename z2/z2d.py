def co_druga(liczby):
    for i, liczba in enumerate(liczby):
        if i % 2 == 1:
            print(liczba)


co_druga(range(0, 10, 1))
