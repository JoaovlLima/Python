fila =["Carlos","Marcos", "Meiri", "Yasmin", "Jorge"]

print("Olá, bem vindo a fila")
variavelAcao = int(input("Para adicionar digite 1, para excluir digite 2 e para ver a posicao digite 3 "))

if variavelAcao == 1:
   novoNome = input("digite um nome para ser adicionado ")
   fila.append(novoNome)
   print("fila alterada "+str(fila))
elif variavelAcao == 2:
   nomeExcluir = input("Nomes na fila: "+str(fila)+" \n digite o nome que será excluido ")
   fila.remove(nomeExcluir)
   print("fila alterada "+str(fila))
elif variavelAcao == 3:
   verPosicao = input("qual cliente deseja ver a posição? "+str(fila)+" ")
   
   for i, nome in enumerate(fila):
      if verPosicao == nome:
         print("A posição do "+str(verPosicao)+" é "+str(i+1))
      
      
else: print("numero invalido")

