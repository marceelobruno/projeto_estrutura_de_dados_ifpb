from helpers.ListaEncadeadaCircular import Lista, ListaException
from helpers.Jogo import Jogo
from helpers.PilhaSequencial import Pilha, PilhaException

l1 = Lista()
p1 = Pilha()
try:    
    jogo1 = Jogo()
    jogo1.inserirParticipante('Lucas')
    jogo1.inserirParticipante('Kaique')
    jogo1.inserirParticipante('Luiz')
    jogo1.inserirParticipante('Marcelo')
    jogo1.inserirParticipante('Bruno')
    jogo1.inserirParticipante('Lorena')
    jogo1.inserirParticipante('Maria')

    jogo1.iniciarJogo()

except ListaException as le:
    print(le)

# except Exception as e:
#     print('Algo inesperado aconteceu...')
