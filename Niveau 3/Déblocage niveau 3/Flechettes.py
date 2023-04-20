def flechettes(lettre,l,start=0):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ligne = ""
    for i in range(start+1):
        ligne = ligne + alphabet[i]
    for loop in range((l//2+1)-len(ligne)):
        ligne = ligne + alphabet[start]
    reverse = "".join(reversed(ligne[:-1]))
    if start != lettre-1:
         return ligne + reverse + "\n" + str(flechettes(lettre,l,start+1)) + "\n" + ligne + reverse
    else:
        return ligne + reverse
    
lettre = int(input())
l = (lettre*2-1)
print(flechettes(lettre,l))
