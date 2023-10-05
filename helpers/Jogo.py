import os
import random
import time

from helpers.ListaEncadeadaCircular import Lista


# criar as exceções e implementar nos metodos
class JogoException(Exception):
    def __init__(self, msg):
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

    def quantParticipantes(self):
        return len(self.__participantes)

    def contemParticipantes(self) -> bool:
        if self.__jogadores.estaVazia():
            return False
        else:
            return True

    def inserirParticipante(self, name: str):
        if name in self.__participantes:
            raise JogoException(
                "Participante já foi inserido, por favor insira outro nome.")

        self.__participantes.append(name)

    def numVencedores(self, quantidade: int):
        # Criar exceçâo, a quantidade de vencedores deve estar entre 1 e o numero de participantes -1.
        try:
            assert 1 <= quantidade <= self.quantParticipantes()- 1, 'Insira um numero entre a margem apresentada.'
            self.__vencedores = quantidade 
        except AssertionError as ae:
            raise JogoException(ae)

    def sortearInicializador(self):
        self.__inicializador = random.randint(1, len(self.__participantes))

    def __str__(self):
        if not self.contemParticipantes():
            str = 'Não há ninguém para jogar'
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
            # assert self.__participantes == [], 'Por favor insira os participantes antes.'

            for i in range(len(self.__participantes)):
                self.__jogadores.inserir(i+1, self.__participantes[i])

            jogadores = self.__jogadores
            self.sortearInicializador()

            rodadas = len(self.__participantes) - self.__vencedores

            while self.__rodada <= rodadas:

                self.__tempo = random.randint(4, 15)
                removido = self.__jogadores.percorrer(
                    self.__inicializador, self.__tempo)
                self.__removido = jogadores.elemento(removido)

                print(self)

                time.sleep(1)
                self.__removido = jogadores.remover(removido)

                self.__inicializador = jogadores.busca(jogadores.ponteiro)
                self.__rodada += 1

            if self.__vencedores == 1:
                print(f'Vencedor após {self.__rodada -1} Rodadas é: {jogadores.elemento(1)}')
            else:
                print(f'Os Vencedores após {self.__rodada-1} Rodadas são: {jogadores}')
        except AssertionError as ae:
            raise JogoException(ae)

    def carregaJogo(self, players: list = ['ronaldo', 'rivaldo', 'ronaldinho', 'kaká']):
        # Preencha a Lista abaixo com os nomes dos participantes que deseja
        # participantes = ['luiz','marcelo','lucas','fabio','leo']
        participantes = players

        # Variavel para criação/leitura de caminho relativo.
        caminho = r'./data'

        # Cria o diretório caso o caminho informado não exista.
        if not os.path.exists(caminho):
            os.makedirs(caminho)
            with open(fr"{caminho}/participantes.txt", "w", encoding='utf-8') as arquivo:
                for participante in participantes:
                    arquivo.write(participante + ",")
        else:
            with open(fr"{caminho}/participantes.txt", "w", encoding='utf-8') as arquivo:
                for participante in participantes:
                    arquivo.write(participante + ",")

        # Abre o arquivo em modo de leitura
        with open(fr"{caminho}/participantes.txt", "r", encoding='utf-8') as arquivo:

            # Lendo todas as linhas do arquivo
            linhas = arquivo.readlines()

            # Dividindo cada linha da lista em uma lista de nomes
            # nomes = [linha.split(",") for linha in linhas]

            players = []
            for linha in linhas:
                players.extend(linha.split(','))
                jogador = players.extend(linha.split(','))
                self.inserirParticipante(jogador)

            equipo = []
            for e in players:
                if e == '':
                    continue
                # else:
                equipo.append(e)

            for j in equipo:
                self.inserirParticipante(j)

            return players[0:-1]
