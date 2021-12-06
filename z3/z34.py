def czy_wieksza(l1: int, l2: int, l3: int) -> bool:
    if l1 + l2 >= l3:
        return "Suma dwóch pierwszych liczb jest większa lub równa trzeciej"
    else:
        return "Suma dwóch pierwszych liczb jest mniejsza od trzeciej"


print(czy_wieksza(4, 5, 9))
