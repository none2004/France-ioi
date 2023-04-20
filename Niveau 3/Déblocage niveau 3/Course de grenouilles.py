def saut(saut,tour,tours,grenouille,nbGrenouilles):
    tours[tour][grenouille-1] = saut
    if tour != 0:
        for s in range(nbGrenouilles):
            tours[tour][s] += tours[tour-1][s]

def Fini(tours):
    for loop in tours[1:-1]:
        M=loop[0],0
        for i in range(1,len(loop)-1):
            print(tours)
            if M[0] <= loop[i]:#faire que quand y'a une égalité ça rajouté rien
                M = loop[i],i
        tours[nbTours][M[1]] +=1
        
nbGrenouilles = int(input())
nbTours = int(input())
tours = []
tour = 1
for loop in range(nbTours+1):
    tours.append([])
    for i in range(nbGrenouilles):
        tours[loop].append(0)

for loop in range(nbTours-1):
    GSaut = input()
    saut(int(GSaut[2:   ]),tour,tours,int(GSaut[0]),nbGrenouilles)
    tour+=1

Fini(tours)
M = -1
for i in range(nbGrenouilles):
    if M < tours[nbTours][i]:
        M = i
print(M+1)
