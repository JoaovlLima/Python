import perguntas
import random

def verfResposta(pergunta,resposta):
    if (resposta == pergunta['resposta_correta']):
        print("Parabens você acertou")
        return True
    else:  
        print("errou") 
        return False


jogoBoll = True

random.shuffle(perguntas.perguntas_faceis)
random.shuffle(perguntas.perguntas_medias)
random.shuffle(perguntas.perguntas_dificeis)

perguntas_aletatorias = perguntas.perguntas_faceis + perguntas.perguntas_medias + perguntas.perguntas_dificeis

while jogoBoll:
   for index, pergunta in enumerate(perguntas_aletatorias,start=1):
       print(f"Pergunta {index}: {pergunta['pergunta']} ")
       for i, alternativa in enumerate(pergunta['alternativas'], start=1):
           print(f"{alternativa}")
           
           resposta = input("Responda: ")
             
           result = verfResposta(pergunta,resposta)
           print(result)
       if not result:
        print("Fim do jogo!")
        jogoBoll = False
        break

     
    
         
          