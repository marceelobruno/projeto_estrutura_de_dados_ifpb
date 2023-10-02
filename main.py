class ListaException(Exception):
    """Classe de exceção lançada quando uma violação de ordem genérica
       da lista é identificada.
    """

    def __init__(self, msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)


class Node:
    """
    Classe de objetos para um nó dinâmico na memória
    """

    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, newData):
        self.__data = newData

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, newNext):
        self.__next = newNext

    def hasNext(self):
        return self.__next is not None

    def __str__(self):
        return str(self.__data)


"""
Esta classe implementa uma estrutura Lista Simplesmente Encadeada
"""


class Lista:
    # constructor initializes an empty linkd list
    def __init__(self):
        self.__head = None
        self.__tamanho = 0

    def estaVazia(self):
        return self.__tamanho == 0

    def __len__(self):
        return self.__tamanho

    def elemento(self, posicao: int) -> any:
        try:
            assert not self.estaVazia(), 'Lista vazia'
            # assert posicao > 0 and posicao <= len(self), f'Posicao invalida. Lista contém {self.__tamanho} elementos'

            cursor = self.__head
            contador = 1
            while (contador < posicao):
                if cursor.next is None:
                    cursor = self.__head
                cursor = cursor.next
                contador += 1

            return cursor.data

        except AssertionError as ae:
            raise ListaException(ae)

    def modificar(self, posicao: int, carga: any):

        try:
            assert posicao > 0, 'A posicao não pode ser 0 (zero) ou um número negativo'
            # assert posicao <= len(self), f'Posicao invalida. Lista contém {self.__tamanho} elementos'
            assert not self.estaVazia(), 'Lista vazia'

            cursor = self.__head
            contador = 1
            while (contador < posicao):
                if cursor.next is None:
                    cursor = self.__head
                cursor = cursor.next
                contador += 1

            cursor.data = carga
        except TypeError:
            raise ListaException('A posição deve ser um número do tipo inteiro')
        except AssertionError as ae:
            raise ListaException(ae.__str__())

    # Aqui não precisa aplicar, pois se não houver o elemento que a chave está buscando,
    # o programa ficará no loop eternamente e não entrará no ListaException.
    def busca(self, chave: any) -> int:
        if (self.estaVazia()):
            raise ListaException('Lista vazia')

        cursor = self.__head
        contador = 1

        while cursor is not None:
            if cursor.data == chave:
                return contador
            cursor = cursor.next
            contador += 1

        raise ListaException(f'O valor {chave} não está armazenado na lista')

    def inserir(self, posicao: int, carga: any):
        try:
            assert posicao > 0 and posicao <= len(self) + 1, f'Posicao invalida. Lista contém {self.__tamanho} elementos'

            # CONDICAO 1: insercao se a lista estiver vazia
            if self.estaVazia():
                if posicao != 1:
                    raise ListaException('A lista esta vazia. A posicao correta para insercao é 1.')

                self.__head = Node(carga)
                self.__tamanho += 1
                return

            # CONDICAO 2: insercao na primeira posicao em uma lista nao vazia
            if posicao == 1:
                novo = Node(carga)
                novo.next = self.__head
                self.__head = novo
                self.__tamanho += 1
                return

            # CONDICAO 3: insercao apos a primeira posicao em lista nao vazia
            cursor = self.__head
            contador = 1
            while contador < posicao - 1:
                cursor = cursor.next
                contador += 1

            novo = Node(carga)
            novo.next = cursor.next
            cursor.next = novo
            self.__tamanho += 1

        except TypeError:
            raise ListaException('A posição deve ser um número inteiro')
        except AssertionError:
            raise ListaException('A posicao não pode ser um número negativo ou 0 (zero)')

    def remover(self, posicao: int) -> any:
        try:
            if (self.estaVazia()):
                raise ListaException('Não é possível remover de uma lista vazia')

            # assert posicao > 0 and posicao <= len(self), f'Posicao invalida. Lista contém {self.__tamanho} elementos'

            cursor = self.__head
            contador = 1

            while (contador <= posicao - 1):
                if cursor.next is None:
                    cursor = self.__head
                anterior = cursor
                cursor = cursor.next
                contador += 1

            data = cursor.data

            if (posicao == 1):
                self.__head = cursor.next
            else:
                anterior.next = cursor.next

            self.__tamanho -= 1
            return data

        except TypeError:
            raise ListaException('A posição deve ser um número inteiro')
        except AssertionError:
            raise ListaException('A posicao não pode ser um número negativo')

    def __str__(self):

        str = 'Lista: [ '
        if self.estaVazia():
            str += ']'
            return str

        cursor = self.__head

        while cursor is not None:
            str += f'{cursor.data}, '
            cursor = cursor.next

        str = str[:-2] + " ]"
        return str


if __name__ == '__main__':
    l1 = Lista()
    l1.inserir(1, 10)
    l1.inserir(2, 20)
    l1.inserir(1, 30)
    l1.inserir(1, 60)
    l1.inserir(1, 80)
    print(l1.busca(10))
    print(len(l1))
    l1.modificar(16, 100)
    l1.remover(10)
    print(l1)
