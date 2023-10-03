from helpers.ListaEncadeadaCircular import Lista
from helpers.PilhaSequencial import Pilha

l1 = Lista()
p1 = Pilha()

l1.inserir(1,10)
l1.inserir(2,20)
l1.inserir(3,30)
l1.inserir(4,40)
l1.inserir(5,50)
l1.inserir(6,60)
print(l1)
teste = l1.percorrer(1,5)
print(l1)
l1.remover(teste)
print(l1)
l1.percorrer(1,10)
print(l1)

