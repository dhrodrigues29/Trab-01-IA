from collections import deque

OBJETIVO = "12345678_"

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado, pai, acao, custo):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        # substituir a linha abaixo pelo seu codigo
        self.estado: str = estado
        self.pai: Nodo = pai
        self.acao: str = acao
        self.custo: int = custo
        

# “2435_1687”
# 2 4 3
# 5 _ 1
# 6 8 7

# RESTRICOES
# posicao = 0 -> esquerda e cima
# posicao = 1 -> cima
# posicao = 2 -> direita e cima
# posicao = 3 -> esquerda
# posicao = 5 -> direita
# posicao = 6 -> esquerda e baixo
# posicao = 7 -> baixo
# posicao = 8 -> direita e baixo

# Função auxiliar que faz uma troca entre dois elementos de uma string
# Exemplo: troca("2435_168", 4, 0) -> "_4352168"      trocou o "_" com o "2"

def troca(string, i, j):
    lista_string = list(string)
    lista_string[i], lista_string[j] = lista_string[j], lista_string[i]
    return(''.join(lista_string))


def direita(estado):
    espaco = estado.find("_")
    if espaco == 2 or espaco == 5 or espaco == 8:
        return estado
    else:
        estado = troca(estado, espaco, espaco + 1)
    
    return estado


def esquerda(estado):
    espaco = estado.find("_")
    if espaco == 0 or espaco == 3 or espaco == 6:
        return estado
    else:
        estado = troca(estado, espaco, espaco - 1)
    
    return estado

def acima(estado):
    espaco = estado.find("_")
    if espaco == 0 or espaco == 1 or espaco == 2:
        return estado
    else:
        estado = troca(estado, espaco, espaco - 3)
    
    return estado

def abaixo(estado):
    espaco = estado.find("_")
    if espaco == 6 or espaco == 7 or espaco == 8:
        return estado
    else:
        estado = troca(estado, espaco, espaco + 3)
    
    return estado
    


def sucessor(estado):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    espaco = estado.find("_")

    # _ esta na posicao central do puzzle, movimento em qualquer uma das quatro direções é permitido
    if espaco == 4:
        return [("esquerda", esquerda(estado)), ("direita", direita(estado)), ("acima", acima(estado)), ("abaixo", abaixo(estado))]
  
    elif espaco == 0:
        return [("direita", direita(estado)), ("abaixo", abaixo(estado))]

    elif espaco == 1:
        return [("esquerda", esquerda(estado)), ("direita", direita(estado)),("abaixo", abaixo(estado))]

    elif espaco == 2:
        return [("esquerda", esquerda(estado)), ("abaixo", abaixo(estado))]

    elif espaco == 3:
        return [("direita", direita(estado)), ("acima", acima(estado)), ("abaixo", abaixo(estado))]

    elif espaco == 5:
        return [("esquerda", esquerda(estado)), ("acima", acima(estado)), ("abaixo", abaixo(estado))]

    elif espaco == 6:
        return [("direita", direita(estado)), ("acima", acima(estado))]

    elif espaco == 7:
        return [("esquerda", esquerda(estado)), ("direita", direita(estado)), ("acima", acima(estado))]

    elif espaco == 8:
        return [("esquerda", esquerda(estado)),("acima", acima(estado))]



def expande(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """

    # sucessores corresponde a uma lista de tuplas, cujas tuplas sao (acao, estado_atingido)
    sucessores = sucessor(nodo.estado)

    nodos_resultantes = []

    # para cada tupla (acao, estado_atingido) na lista de sucessores...
    for suc in sucessores:
        #               estado   pai   acao    custo
        novo_nodo = Nodo(suc[1], nodo, suc[0], nodo.custo + 1)
        nodos_resultantes.append(novo_nodo)
        del novo_nodo

    return nodos_resultantes

# Exemplo de output da função expande
"""
nodo1 = Nodo("1234_5678", None, None, 0)

print(expande(nodo1)[0].estado + " " + expande(nodo1)[0].pai.estado + " " + expande(nodo1)[0].acao + " " + str(expande(nodo1)[0].custo))
print(expande(nodo1)[1].estado + " " + expande(nodo1)[1].pai.estado + " " + expande(nodo1)[1].acao + " " + str(expande(nodo1)[1].custo))
print(expande(nodo1)[2].estado + " " + expande(nodo1)[2].pai.estado + " " + expande(nodo1)[2].acao + " " + str(expande(nodo1)[2].custo))
print(expande(nodo1)[3].estado + " " + expande(nodo1)[3].pai.estado + " " + expande(nodo1)[3].acao + " " + str(expande(nodo1)[3].custo))
"""

# funcao que retorna a lista de movimentos feitos do primeiro ate o nodo recebido
def gera_lista_movimentos(nodo_final):

    # inicia o nodo atual com o nodo recebido e a lista de acoes vazia
    nodo_atual = nodo_final
    lista_movimentos = []

    # printa o custo do nodo final
    print("custo do nodo final: ", nodo_final.custo)
    
    # enquanto o nodo atual tiver pai, adiciona sua acao a lista de movimentos 
    # e atualiza o nodo atual para o nodo pai
    while nodo_atual.pai != None:
        lista_movimentos.append(nodo_atual.acao)
        nodo_atual = nodo_atual.pai

    # inverte e retorna a lista de movimentos preenchida do OBJETIVO ao estado inicial
    lista_movimentos.reverse()
    return lista_movimentos


def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo

    # inicia variavel de Nodo inicial com o estado recebido
    estado_inicial = Nodo(estado, None, None, 0)

    # inicia nodos_visitados como set(), que nao permite elementos repetidos i.e. set[1,1,2,3] = (1,2,3)
    nodos_visitados = set()

    # inicia nodos_fronteira como deque, que significa double-ended queue
    # facilita pop e append e funciona com qualquer tipo
    nodos_fronteira: deque = deque([estado_inicial])

    # enquanto houver nodos, repete a busca
    while len(nodos_fronteira) != 0:

        # remove o nodo atual do deque, o primeiro da fila i.e. [1,2,3].popleft() = 1
        nodo_atual = nodos_fronteira.popleft()  

        # se o nodo for o OBJETIVO, retorna a lista de movimentos
        if nodo_atual.estado == OBJETIVO:  
            return gera_lista_movimentos(nodo_atual)

        # checa se o estado atual ja estava na set de nodos visitados
        if not nodo_atual.estado in nodos_visitados:

            # adiciona o nodo aos nodos visitados
            nodos_visitados.add(nodo_atual.estado)  

            # insere no final da fila de nodos na fronteira o resultado do 
            # expande para o nodo atual i.e. [1,2].extend([3]) = [1,2,3]
            nodos_fronteira.extend(expande(nodo_atual))

    # se o while da busca encerrar, nao existe sequencia de movimentos possivel
    return None  

def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    
    # inicia variavel de Nodo inicial com o estado recebido
    estado_inicial = Nodo(estado, None, None, 0)

    # inicia nodos_visitados como set(), que nao permite elementos repetidos i.e. set[1,1,2,3] = (1,2,3)
    nodos_visitados = set()

    # inicia nodos_fronteira como deque, que significa double-ended queue
    # facilita pop e append e funciona com qualquer tipo
    nodos_fronteira: deque = deque([estado_inicial])

    # enquanto houver nodos, repete a busca
    while len(nodos_fronteira) != 0:

        # remove o nodo mais recente da pilha (deque) i.e. [1,2,3].pop() = 3
        nodo_atual = nodos_fronteira.pop()  

        # se o nodo for o OBJETIVO, retorna a lista de movimentos
        if nodo_atual.estado == OBJETIVO:  
            return gera_lista_movimentos(nodo_atual)

        # checa se o estado atual ja estava na set de nodos visitados
        if not nodo_atual.estado in nodos_visitados:

            # adiciona o nodo aos nodos visitados
            nodos_visitados.add(nodo_atual.estado)  

            # append a nodos na fronteira os vizinhos do nodo atual
            nodos_fronteira.extend(expande(nodo_atual))

    # se o while da busca encerrar, nao existe sequencia de movimentos possivel
    return None  


def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
