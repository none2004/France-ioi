def creationMatrix(TailleMatrix):
    Matrix=[]
    for loop in range(TailleMatrix[0]):
        Matrix.append([input().replace(" ","")])
    print(Matrix)
    return(Matrix)

def carreMax(TailleMatrix,Matrix,caractère="0"):
    Max = 0
    MaxX=0
    MaxY=0
    for x in range(TailleMatrix[1]-1):
        for y in range(TailleMatrix[0]-1):
            if Matrix[x][0][y]==caractère:
                if x != TailleMatrix[1]-1 or y != TailleMatrix[0]-1:
                    while Matrix[Colonnes][0][Lignes]==caractère:
                        while Matrix[Colonnes][0][Lignes]==caractère:#mettre en place un double MaxX pour pouvoir comparer les 2 et garder le plus petit faire la même pour Y
                            print(Colonnes,Lignes)
                            MaxX+=1
                            Lignes+=1
                        if MaxX!=0:
                            
                        MaxY+=1
                        Colonnes+=1
            if MaxY>Max:
                Max = MaxY
            MaxX = 0
            MaxY = 0
    print(Max)


    
Taille = input()
Taille = (int(Taille[0]),int(Taille[2]))

carreMax(Taille,creationMatrix(Taille))
