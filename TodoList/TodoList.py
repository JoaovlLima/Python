print("O que você deseja realizar?")

tarefas = []
tarefaAberta = True
while tarefaAberta:
  acao = int(input("1-Adicionar Tarefa\n2-Vizualizar Tarefas\n3-Editar Tarefa\n4-Marcar como concluido\n5-Excluir Tarefa\n 6-Sair\n"))
  if acao == 1:
    novaTarefa = input("Adicione uma nova tarefa: ")
    tarefas.append(novaTarefa)
    print("Suas Tarefas: "+str(tarefas))
  elif acao == 2:
    print("Suas Tarefas: "+str(tarefas))
  elif acao == 3:
     print("Suas Tarefas: "+str(tarefas))
     editTarefa = input("Qual tarefa deseja editar?")
     if editTarefa in tarefas:
       tarefaEdit = input("Digite para alterar a tarefa")
       posicao = tarefas.index(editTarefa)

       tarefas[posicao] = tarefaEdit
       print("Suas Tarefas: "+str(tarefas))
     else: print("Tarefa inexistente")
  elif acao == 4:
      print("Suas Tarefas: "+str(tarefas))
      concluirTarefa = input("Qual tarefa deseja concluir?")
      if concluirTarefa[-12:] != "(concluido)":
       if concluirTarefa in tarefas:
       
        posicao = tarefas.index(concluirTarefa)
      
        tarefas[posicao] = concluirTarefa + "(concluido)"
        print("Suas Tarefas: "+str(tarefas))
       else: print("Tarefa inexistente")
      else:("Tarefa já concluida")
  elif acao == 5: 
    print("Suas Tarefas: "+str(tarefas))
    excluiTarefa = input("Qual tarefa deseja excluir?")
    if excluiTarefa in tarefas:
       
       posicao = tarefas.index(excluiTarefa)

       del tarefas[posicao]
       print("Suas Tarefas: "+str(tarefas))
    else: print("Tarefa inexistente")
  elif acao == 6:
    tarefaAberta = False
  else: ("Acão inexistente")  
