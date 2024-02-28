import perguntas
import jogo
import random
jogoBoll = True

random.shuffle(perguntas.perguntas_faceis)
random.shuffle(perguntas.perguntas_medias)
random.shuffle(perguntas.perguntas_dificeis)

perguntas_aletatorias = perguntas.perguntas_faceis + perguntas.perguntas_medias + perguntas.perguntas_dificeis

while(jogoBoll):
   for index, pergunta in enumerate(perguntas_aletatorias,start=1):
       print(f"Pergunta {index}: {pergunta['pergunta']} ")
       for i, alternativa in enumerate(pergunta['alternativas'], start=1):
           print(f"{i}. {alternativa}")
           
           resposta = input("Responda: ")
             
           result = jogo.verfResposta(pergunta,resposta)
           
           if not result:
            print("Fim do jogo!")
            jogoBoll = False
            break