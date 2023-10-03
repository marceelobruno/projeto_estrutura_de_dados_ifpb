from helpers.ListaEncadeadaCircular import Lista, ListaException
from helpers.PilhaSequencial import Pilha, PilhaException

l1 = Lista()
p1 = Pilha()
try:    
    l1.inserir(1,10)
    l1.inserir(2,20)
    l1.inserir(3,30)
    l1.inserir(4,40)
    l1.inserir(5,50)
    l1.inserir(6,60)
    print(l1)
    teste = l1.percorrer(6,2)
    # print(l1)
    removido = l1.remover(teste)
    print(f'Removido: {removido}')
    print(l1)
    # l1.percorrer(1,10)
    # print(l1)
except ListaException as le:
    print(le)

except Exception as e:
    print('Algo inesperado aconteceu...')
