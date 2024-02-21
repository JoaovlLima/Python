import random
# Exercicio 1
vetor1 = [1,2,3,4,5]

print (str(vetor1))

# Exercicio 2
vetor2 = [1,2,3,4,5,6,7,8,9,10]
vetor2Inverso = vetor2[::-1]
print(str(vetor2Inverso))

# Exercicio 3
vetorNota = [10,8,4,9]

media = sum(vetorNota) / len(vetorNota)
print(str(media))

# Exercicio 4
vetorCarac = ['a','b','d','p','e','q','f','o','l','m']
vetorCons = []
contVogal = 0
contConsoante = 0

for carac in vetorCarac:
    if carac  in ['a', 'e', 'i', 'o', 'u'] :
        contVogal = contVogal+1
    else:
        vetorCons.append(carac)
        contConsoante = contConsoante + 1

print ("Teve um total de "+str(contConsoante)+" consoantes\n e elas são "+str(vetorCons))

# Exercicio 5
vetor5 = []
vetorPar = []
vetorImpar = []
for i in range(20):
    vetor5.append(random.randint(1,100))

print(str(vetor5))

for num in vetor5:
    if num%2 == 0:
        vetorPar.append(num)
    else: vetorImpar.append(num)

print ("Par "+str(vetorPar)+"\nImpar "+str(vetorImpar))
