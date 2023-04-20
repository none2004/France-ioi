def doublon(chaine):
    i=0
    while len(chaine)-1 > i :
        if chaine[i] == chaine[i+1]:
            chaine = chaine[:i] + chaine[(i+2):]
            if i > 0:
                i=i-1
        else:
            i=i+1
    print(chaine)

doublon(input())
