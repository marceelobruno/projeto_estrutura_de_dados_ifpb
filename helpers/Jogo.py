
import random
import time
from helpers.ListaEncadeadaCircular import Lista

#criar as exceções e implementar nos metodos
class JogoException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class Jogo:

    def __init__(self):
        self.__participantes = []
        self.__inicializador = None
        self.__rodada = 1
        self.__tempo = 0
        self.__removido = None
        self.__vencedores = 1
        self.__jogadores = Lista()

    def contemParticipantes(self) -> bool:
        if self.__jogadores.estaVazia():
            return False
        else:
            return True

    def inserirParticipante(self, name:str):
        self.__participantes.append(name)

    def numVencedores(self, quantidade:int): 
        #Criar exceçâo, a quantidade de vencedores deve estar entre 1 e o numero de participantes -1.
        self.__vencedores = quantidade
        return self.__vencedores

    def sortearInicializador(self):
        self.__inicializador = random.randint(1, len(self.__participantes))
        return self.__inicializador

    def __str__(self):

        if not self.contemParticipantes():
            str = f'Não há ninguém para jogar'
            return str
        
        str = f'''
        Participantes: {self.__jogadores}
        Rodada: {self.__rodada}
        Pointer: {self.__jogadores.elemento(self.__inicializador)}
        Saltos: {self.__tempo}
        Removido: {self.__removido}
        '''
        return str
    
    def iniciarJogo(self):
        try:
            #assert self.__participantes == [], 'Por favor insira os participantes antes.'
            
            for i in range(len(self.__participantes)):
                self.__jogadores.inserir(i+1, self.__participantes[i])
            
            jogadores = self.__jogadores
            self.sortearInicializador()

            rodadas = len(jogadores)
            
            while self.__rodada < rodadas:

                self.__tempo = random.randint(4, 15)
                removido = self.__jogadores.percorrer(self.__inicializador, self.__tempo)
                self.__removido = jogadores.elemento(removido)

                print(self)
                
                time.sleep(1)
                self.__removido = jogadores.remover(removido)
                
                self.__inicializador = jogadores.busca(jogadores.ponteiro)
                self.__rodada +=1
            
            print(f'Vencedor após {self.__rodada} Rodadas é: {jogadores.elemento(1)}')

        except AssertionError as ae:
            raise JogoException(ae)
        
        

    