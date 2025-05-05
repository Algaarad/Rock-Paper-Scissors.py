# faire pierre papier ciseau

import random

def ppc (choix):
    assert choix == "Pierre" or choix == "Papier" or choix == "Ciseaux"
    lst = ["Pierre", "Papier", "Ciseaux"]
    r = random.randint(1,2)
    if choix == lst[0]:
        if r == 1:
            return "Papier"
    if choix == lst[1]:
        if r == 1:
            return "Ciseaux"
    if choix == lst[2]:
        if r == 1:
            return "Pierre"
    return random.choice(lst)


print(ppc("Pierre"))
