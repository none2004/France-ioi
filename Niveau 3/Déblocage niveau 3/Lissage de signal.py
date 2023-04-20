
nbMesures = int(input())
diffMax = float(input())
Mesures = []
for loop in range(nbMesures):
    Mesures.append(float(input()))
n=0
result = True
for loop in range(len(Mesures)-1):
    if abs(Mesures[loop]-Mesures[loop+1]) < diffMax:
        k+=1
if k == nbMesures-1:
    result=False

while result:
    New = []
    for loop in Mesures:
        New.append(loop)
    for i in range(1,len(Mesures)-1):
        Mesures[i] = (New[i-1]+New[i+1])/2
    n+=1
    k=0
    for loop in range(len(Mesures)-1):
        if abs(Mesures[loop]-Mesures[loop+1]) < diffMax:
            k+=1
    if k == nbMesures-1:
        result=False

print(n)
