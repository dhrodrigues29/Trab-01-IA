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
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


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
    raise NotImplementedError
    """
    busca_grafo(s): 
        X ← {}
        F ← fila( {s} )
        loop:
            se F = ∅: FALHA
            v ← F.desenfileira()
            se v é o objetivo: retornar caminho s-v
            se v ∉ X:
                Insere v em X
                Insere vizinhos de v em F
    """
    


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
    raise NotImplementedError


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
