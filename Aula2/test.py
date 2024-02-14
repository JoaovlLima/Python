# 5 - Desafios Extras:
# Crie um programa que simule um jogo de tabuleiro, como xadrez ou damas. Permita que dois jogadores movam suas peças e valide se os movimentos são legais.

# Desenvolva um sistema de gerenciamento de tarefas. O programa deve permitir ao usuário adicionar, editar, marcar como concluída e excluir tarefas. Utilize estruturas de dados apropriadas.
num1 = int(input("Digite o primeiro numero"))
num2 = int(input("Digite o segundo numero"))
opNoFeita = True
while opNoFeita:   
    operacao = int(input("Qual operação deseja fazer?\n 1 - soma\n2-subtração\n3-multiplicação\n4-divisão "))
    if operacao == 1:
     resultado = num1 + num2
     print("O resultado é "+str(resultado))
     opNoFeita = False
    elif operacao == 2: 
     resultado = num1 - num2
     print("O resultado é "+str(resultado))
     opNoFeita = False
    elif operacao == 3: 
     resultado = num1 * num2
     print("O resultado é "+str(resultado))
     opNoFeita = False
    elif operacao == 4: 
     resultado = num1 / num2
     print("O resultado é "+str(resultado))
     opNoFeita = False
    else: print("operação inexistente")



         
  
