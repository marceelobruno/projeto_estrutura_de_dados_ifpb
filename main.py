from helpers.Jogo import Jogo, JogoException

try:    
    print('Bem Vindo ao Circuito Bomba !!')
    while True:
        jogo = Jogo()

        while True:
            try:
                menuInicial = int(input('Digite 1 para iniciar um jogo manualmente -- Digite 2 para carregar um arquivo de texto. '))
                assert menuInicial == 1 or menuInicial == 2, 'Digite uma das opções.'
                break

            except ValueError:
                print('Digite um numero inteiro dentre as opções.')
            except AssertionError as ae:
                print(ae)

        if menuInicial == 1:
            while True:
                try:   
                    numParticipantes = int(input('Digite o numero de participantes: '))
                    assert numParticipantes > 1, "São necessários no mínimo dois jogadores."
                    break
                except ValueError:
                    print('Digite um numero inteiro.')
                except AssertionError as ae:
                    print(ae)
            while True:
                try:
                    
                    jogador = input('Insira o nome do jogador (sem espaços no começo):').title()
                    jogo.inserirParticipante(jogador)
                    if (jogo.quantParticipantes() == numParticipantes):
                        break
                except JogoException as e:
                    print(e)

        if menuInicial == 2:
            load = jogo.carregaJogo()
            numParticipantes = len(load)

        while True:
            try:
                numVencedores = int(input(f'Para iniciar o jogo defina a quantidade de vencedores(1 - {numParticipantes - 1}): '))
                jogo.numVencedores(numVencedores)
                break

            except JogoException as jg:
                print(jg)
            except ValueError:
                print('Insira um numero inteiro dentro da margem apresentada.')

        print('Que os jogos começem -_-')

        jogo.iniciarJogo()

        jogarNovamente = input('Deseja rodar novamente o programa (s)im/(n)ão?').lower()
        if jogarNovamente == 's':
            continue
        else:
            print('Obrigado por jogar !')
            break

except Exception as e:
    print('Algo inesperado aconteceu...')
