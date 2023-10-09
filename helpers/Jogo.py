import os
import random
import time

from helpers.ListaEncadeadaCircular import Lista
from helpers.PilhaSequencial import Pilha


# criar as exceções e implementar nos metodos
class JogoException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Jogo:

    def __init__(self):
        self.__participantes = []
        self.__inicializador = None
        self.__rodada = 1
        self.__saltos = 0
        self.__removido = None
        self.__vencedores = 1
        self.__jogadores = Lista()
        self.__pilhaRemovidos = Pilha()

    def quantParticipantes(self) ->int:
        """Este método retorna a quantidade de participantes inseridos no self.__participantes.

        Returns:
            int: Retorna a quantidade de participantes. 
        """
        return len(self.__participantes)

    def contemParticipantes(self) -> bool:
        """Este método verifica se há participantes na partida. 

        Returns:
            bool: Retorna True ou False se houver participantes.
        """
        if self.__jogadores.estaVazia():
            return False
        else:
            return True

    def inserirParticipante(self, name: str) -> None:
        """Este método insere o participante dentro do vetor self.__participantes.

        Args:
            name (str): nome do participante a ser inserido

        Raises:
            JogoException: Sobe uma exceção caso o usuário tente adicionar o mesmo
            nome mais de uma vez.
        """
        # Verifica se o primeiro caractere da string é um espaço.
        if name== "" or name[0] == chr(32):
            raise JogoException('Nomeie o participante.')
        if name in self.__participantes:
            raise JogoException(
                "Participante já foi inserido, por favor insira outro nome.")

        self.__participantes.append(name)

    def inserirParticipanteCarregado(self, name: str) -> None:
        """Este método insere o participante dentro do vetor self.__participantes.

        Args:
            name (str): nome do participante a ser inserido

        Raises:
            JogoException: Sobe uma exceção caso o usuário tente adicionar o mesmo
            nome mais de uma vez.
        """
        if name in self.__participantes:
            raise JogoException(
                "Lista com participantes duplicados, por favor refaça a lista com nomes únicos e tente novamente!.")

        self.__participantes.append(name)

    def numVencedores(self, quantidade: int) -> None:
        """Este método determina o número de vencedores da partida.

        Args:
            quantidade (int): Quantidade de vencedores.

        Raises:
            JogoException: Sobe uma exceção caso a quantidade informada for um número menor 
            que 1 ou maior igual à quantidade de participantes.
        """
        try:
            assert 1 <= quantidade <= self.quantParticipantes()- 1, 'Insira um numero entre a margem apresentada.'
            self.__vencedores = quantidade

        except AssertionError as ae:
            raise JogoException(ae)

    def sortearInicializador(self) -> None:
        """Sorteia a posição do jogador que irá iniciar a primeira rodada.
        """
        self.__inicializador = random.randint(1, len(self.__participantes))

    def __str__(self) -> str:
        if not self.contemParticipantes():
            str = 'Não há ninguém para jogar'
            return str

        str = f'''
Participantes: {self.__jogadores}
Rodada: {self.__rodada}
Pointer: {self.__jogadores.elemento(self.__inicializador)}
Saltos: {self.__saltos}
Removido: {self.__removido}
        '''
        return str

    def iniciarJogo(self):
        """
        Inicia o jogo, realiza a jogabilidade e determina o vencedor ou vencedores após várias rodadas.

        Este método executa as seguintes etapas:
        1. Insere participantes na lista de jogadores.
        2. Realiza um sorteio para definir o inicializador do jogo.
        3. Realiza rodadas até que haja apenas um vencedor ou vencedores.
        4. Ao final é mostrado o percurso para a vitória.
        
        Raises:
            JogoException: Se não houver participantes no jogo.
        """
        try:
            assert not self.contemParticipantes(), "Não há participantes."
            
            #insere os particpantes na lista circular
            for i in range(len(self.__participantes)):
                self.__jogadores.inserir(i+1, self.__participantes[i])

            jogadores = self.__jogadores
            pilhaRemovidos = self.__pilhaRemovidos
            self.sortearInicializador()

            rodadas = len(self.__participantes) - self.__vencedores
            
            #Inicia o turno do jogo
            while self.__rodada <= rodadas:
                #Sorteia a quatidade de saltos.
                self.__saltos = random.randint(4, 15)
                #chama o método percorrer da lista para determinar o jogador eliminado.
                removido = self.__jogadores.percorrer(self.__inicializador, self.__saltos)
                self.__removido = jogadores.elemento(removido)

                print(self)

                time.sleep(1)
                self.__removido = jogadores.remover(removido)
                pilhaRemovidos.empilha(self.__removido)
                
                self.__inicializador = jogadores.busca(jogadores.ponteiro)
                self.__rodada +=1
            
            if self.__vencedores == 1:
                print(f'Vencedor após {self.__rodada -1} Rodadas é: {jogadores.elemento(1)}')
            else:
                print(f'Os Vencedores após {self.__rodada-1} Rodadas são: {jogadores}')

            print(f"""
Percurso para a vitória:
{pilhaRemovidos}        
                    """)
        except AssertionError as ae:
            raise JogoException(ae)

    def carregaJogo(self, players: list = ['ronaldo', 'rivaldo', 'ronaldinho', 'kaká']):
        """Este método carrega previamente uma lista com possíveis
        jogadores para o jogo Circuito Bomba.

        Args:
            players (list, optional): Valores default para os participantes do jogo.

        Returns:
            list: Lista com participantes pré-definidos.
        """
        # Variavel para criação/leitura de caminho relativo.
        caminho = r'./data'

        # Cria o diretório caso o caminho informado não exista.
        if not os.path.exists(caminho):
            os.makedirs(caminho)
            with open(fr"{caminho}/participantes.txt", "w", encoding='utf-8') as arquivo:
                for participante in players:
                    arquivo.write(participante + ",")

        # Abre o arquivo em modo de leitura
        with open(fr"{caminho}/participantes.txt", "r", encoding='utf-8') as arquivo:
            # Lendo todas as linhas do arquivo
            linhas = arquivo.readlines()
            # Dividindo cada linha da lista em uma lista de nomes
            players = []
            for linha in linhas:
                players.extend(linha.split(','))

            equipo = []
            for e in players:
                if e == '':
                    continue
                equipo.append(e)
                self.inserirParticipanteCarregado(e)

            return players[0:-1]
