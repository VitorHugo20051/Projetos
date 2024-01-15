# TAD intersecoes
# Construtores
def cria_intersecao(col, lin):
    """
    Cria uma interseção a partir de uma coluna e uma linha.
    Args:
        col (str): Coluna da interseção (de 'A' a 'S').
        lin (int): Linha da interseção (de 1 a 19).
    Returns:
        tuple: A interseção criada como uma tupla (coluna, linha).
    Raises:
        ValueError: Se os argumentos não forem válidos.
    """
    if type(col) == str and len(col) == 1 and type(lin) == int:
        if 'A' <= col <= 'S' and 1 <= lin:
            return (col, lin)
    raise ValueError('cria_intersecao: argumentos invalidos')
# Seletores  
def obtem_col(i):
    """
    obtem col(i) devolve a coluna col da interseção i.
    """
    if isinstance(i[0], (list, tuple)):
        return [inter[0] for inter in i[0]]
    else:
        return i[0]

def obtem_lin(i):
    """
    obtem lin(i) devolve a linha lin da interseção i.
    """
    if isinstance(i[1], (list, tuple)):
        return [int(inter[1]) for inter in i[1]]
    else:
        return i[1]
# Reconhecedor
def eh_intersecao(arg):
    """
    eh intersecao(arg) devolve True caso o seu argumento seja uma intersecao
    e False caso contrário.
    """
    if type(arg) == str or type(arg) == tuple and len(arg) == 2 and type(arg[1]) != tuple:
        if 'A' <= arg[0] <= 'S' and 1 <= int(arg[1]) <= 19:
            return True
        return False
    elif isinstance(arg, (list, tuple)):
        for inter in arg:
            if not isinstance(inter, (str, tuple)) or len(inter) != 2:
                return False
            if not ('A' <= inter[0] <= 'S' and 1 <= int(inter[1]) <= 19):
                return False
        return True
    return False
# Teste
def intersecoes_iguais(i1, i2):
    """
    intersecoes_iguais(i1, i2) devolve True caso i1 e i2 sejam intersecoes iguais
    e False caso contrário.
    """
    if i1 == i2:
        return True
    return False
# Transformadores
def intersecao_para_str(i):
    """
    intersecao_para_str(i) devolve a cadeia de caracteres que representa o seu
    argumento.
    """
    return f'{obtem_col(i)}{obtem_lin(i)}'

def str_para_intersecao(i):
    """
    str_para_intersecao(i) devolve a intersecao que representa o seu
    argumento.
    """
    return i[0], int(i[1:])
# Funções de alto nível 
def obtem_intersecoes_adjacentes(i, l):
    """
    obtem intersecoes adjacentes(i, l) devolve um tuplo com as interseções adjacentes
    á interseção i de acordo com a ordem de leitura em que l corresponde á interseção
    superior direita do tabuleiro de Go.
    """

    intersecoes_adjacentes = []
    if type(i) != int:
        col = ord(obtem_col(i))
        lin = obtem_lin(i)
        v, h = ord(obtem_col(i)) - ord('A'), lin - 1
        adjacentes = [(v, h-1), (v, h+1), (v-1, h), (v+1, h)]

        for av, ah in adjacentes:
            if 0 <= av <= col and 0 <= ah <= lin:
                adj_i = (chr(ord('A') + av), ah + 1)
                if type(adj_i) != None and adj_i not in intersecoes_adjacentes and eh_intersecao(adj_i):
                    if obtem_col(adj_i) <= obtem_col(l) and obtem_lin(adj_i) <= obtem_lin(l):
                        intersecoes_adjacentes.append(adj_i)
    if intersecoes_adjacentes != None:
        return ordena_intersecoes(intersecoes_adjacentes)

def ordena_intersecoes(t):
    """
    ordena_intersecoes(t) recebe um tuplo de intersecoes e devolve um tuplo 
    com essas intersecoes ordenadas de acordo com a ordem dd leitura
    """
    intersecoes_ordenadas = sorted(t, key= lambda i: (obtem_lin(i), obtem_col(i)))
    return tuple(intersecoes_ordenadas)

# TAD pedra
# Construtores
def cria_pedra_branca():
    return 'O'

def cria_pedra_preta():
    return 'X'

def cria_pedra_neutra():
    return '.'
# Reconhecedores
def eh_pedra(arg):
    """
    Verifica se arg é uma pedra.
    Args:
        arg: universal
    Returns:
        bool: True se for pedra, False se não.
    """
    if isinstance(arg, (list, tuple)):
        for inter in arg:
            if isinstance(inter, str) and inter in ('O', 'X', '.'):
                return True
        return False
    else:
        return arg in ('O', 'X', '.')

def eh_pedra_branca(p):
    return eh_pedra(p) and p == 'O'

def eh_pedra_preta(p):
    return eh_pedra(p) and p == 'X'

def eh_pedra_neutra(p):
    return eh_pedra(p) and p == '.'
    
# Teste
def pedras_iguais(p1, p2):
    """
    Cria uma interseção a partir de uma coluna e uma linha.
    Args:
        p1: pedra
        p2: pedra
    Returns:
        bool: True se as pedra forem iguais, se não False
    """
    if eh_pedra(p1) and eh_pedra(p2):
        if eh_pedra_branca(p1) and eh_pedra_branca(p2) or eh_pedra_preta(p1) and eh_pedra_preta(p2) or eh_pedra_neutra(p1) and eh_pedra_neutra(p2):
            return True
        return False
    return False
# Transformadores
def pedra_para_str(p):
    """
    pedra para str(p) devolve a cadeia de caracteres que representa o jogador dono
    da pedra, isto e, O, X ou . para pedras do jogador branco, preto ou neutra
    respetivamente.
    Args:
        p: pedra
    Returns:
        str: Retorna uma pedra.
    """
    if eh_pedra(p):
        if p == cria_pedra_branca():
            return 'O'
        elif p == cria_pedra_preta():
            return 'X'
        elif p == cria_pedra_neutra():
            return '.'
# Função de alto nível
def eh_pedra_jogador(p):
    if eh_pedra(p):
        if eh_pedra_branca(p) or eh_pedra_preta(p):
            return True
        return False
    
# TAD goban
# Construtores
def cria_goban_vazio(n):
    """
    Cria um goban vazio.
    Args:
        n: número de colunas e linhas
    Returns:
        goban: Retorna um goban vazio.
    Raises:
        ValueError: Se os argumentos não forem válidos.
    """
    if type(n) == int and n in (9, 13, 19):
        return [['.' for _ in range(n)] for _ in range(n)]
    raise ValueError('cria_goban_vazio: argumento invalido')

def inter_para_indicie(i):
    if isinstance(i, str) and len(i) <= 3:
        coluna = ord(obtem_col(str_para_intersecao(i))) - ord('A')
        linha = int(obtem_lin(str_para_intersecao(i))) - 1
        return linha, coluna
    elif isinstance(i, tuple) and len(i) == 2 and isinstance(i[0], str) and isinstance(i[1], int):
        coluna = ord(i[0]) - ord('A')
        linha = i[1] - 1
        return linha, coluna
    elif isinstance(i, tuple) and len(i) == 1 and type(i[0]) == tuple and isinstance(i[0][0], str) and isinstance(i[0][1], int):
        coluna = ord(i[0][0]) - ord('A')
        linha = i[0][1] - 1
        return linha, coluna
    
    
def cria_goban(n, ib, ip):
    """
    Cria um goban.
    Args:
        n: número de linhas e coluna
        ib: intersecoes das pedras brancas
        ip: intersecoes das pedras pretas
    Returns:
        goban: Retorna um goban.
    Raises:
        ValueError: Se os argumentos não forem válidos.
    """
    if not (isinstance(n, int) and n in (9, 13, 19)):
        raise ValueError('cria_goban: argumentos invalidos')
    if not isinstance(ib, tuple) or not isinstance(ip, tuple):
        raise ValueError('cria_goban: argumentos invalidos')
    if len(ib) != len(set(ib)) or len(ip) != len(set(ip)) or any(not eh_intersecao(inter) for inter in ib + ip):
        raise ValueError('cria_goban: argumentos invalidos')
    if set(ib) & set(ip):
        raise ValueError('cria_goban: argumentos invalidos')

    goban = cria_goban_vazio(n)

    for inter in ib:
        lin, col = inter_para_indicie(inter)
        if 1 <= lin <= n and 1 <= col <= n:
            goban[col - 1][lin - 1] = 'O'
        raise ValueError('cria_goban: argumentos invalidos')
    
    for inter in ip:
        lin, col = inter_para_indicie(inter)
        if 1 <= lin <= n and 1 <= col <= n:
            goban[col - 1][lin - 1] = 'X'
        raise ValueError('cria_goban: argumentos invalidos')
    return goban

def cria_copia_goban(g):
    """
    Cria uma cópia do goban.
    Args:
        g: goban
    Returns:
        goban: Retorna uma cópia do goban.
    """
    tamanho = len(g)
    copia = [[g[col][lin] for col in range(tamanho)] for lin in range(tamanho)]
    return copia
# Seletores
def obtem_ultima_intersecao(g):
    """
    Obtem a ultima intersecao do goban.
    Args:
        g: goban
    Returns:
        tuple: Retorna a ultima intersecao do goban.
    """
    num_linhas = len(g)
    num_colunas = len(g[0]) - 1

    for lin in range(num_linhas, 0, -1):
        for col in range(num_colunas, 0, -1):
            return (chr(col + ord('A')), lin)

def obtem_pedra(g, i):
    """
    Obtem a pedra da intersecao.
    Args:
        g: goban
        i: intersecao
    Returns:
        str: Retorna a pedra da interseçao.
    """
    if eh_intersecao(i):
        lin, col = inter_para_indicie(i)
        cor_pedra = g[col][lin]
        if cor_pedra == 'O':
            return 'O'
        elif cor_pedra == 'X':
            return 'X'
        elif cor_pedra == '.':
            return '.'
    
def obtem_cadeia(g, i):
    """
    obtem cadeia(g, i) devolve o tuplo formado pelas interseçoes (em ordem de
    leitura) das pedras da mesma cor que formam a cadeia que passa pela interseçao i. Se a posiçao nao estiver ocupada, 
    devolve a cadeia de interseçoes
livres.
    Args:
        g: goban
        i: intersecao
    Returns:
        tuple: Retorna a cadeia de i.

    """
    cadeia = []
    inter_prox = [i]
    visitado = set()

    while inter_prox != []:
        inter = inter_prox.pop(0)
        if inter not in visitado:
            cadeia.append(inter)
            visitado.add(inter)
            adjacentes = obtem_intersecoes_adjacentes(inter, obtem_ultima_intersecao(g))

            for adj in adjacentes:
                if obtem_pedra(g, inter) == obtem_pedra(g, adj) and adj not in visitado:
                    inter_prox.append(adj)

    return ordena_intersecoes(cadeia)

# Modificadores
def coloca_pedra(g, i, p):
    """
    Coloca uma pedra no goban.
    Args:
        g: goban
        i: intersecao
        p: pedra
    Returns:
        tuple: Retorna o goban mas com a pedra na intersecao referida.
    """
    lin, col = inter_para_indicie(i)
    if p == cria_pedra_branca():
        g[col][lin] = 'O'
        
    elif p == cria_pedra_preta():
        g[col][lin] = 'X'

    else:
        g[col][lin] = '.'

    return g

def remove_pedra(g, i):
    """
    Cria uma interseção a partir de uma coluna e uma linha.
    Args:
        g: goban
        i: intersecao
    Returns:
        tuple: Retorna o goban mas com a pedra removida.
    """
    lin, col = inter_para_indicie(i)
    g[col][lin] = '.'
    return g

def remove_cadeia(g, t):
    """
    Remove uma cadeia de um goban.
    Args:
        g: goban
        t: cadeia
    Returns:
        tuple: Retorna o goban mas com a cadeia removida.
    """
    for intersecao in t:
        remove_pedra(g, intersecao)
    return g

# Reconhecedores
def eh_goban(arg):
    """
    Verifica se arg é um goban.
    Args:
        arg: universal
    Returns:
        bool: True se for um goban, False se não.
    """
    if len(arg) in (9, 13, 19):
        tamanho = len(arg)
        for c in arg:
            if len(c) != tamanho:
                return False
        for inter in c:
            if inter not in ('.', 'O', 'X'):
                return False
        return True
    return False

def eh_intersecao_valida(g, i):
    """
    Verifica se a interscao e valida no goban.
    Args:
        g: goban
        i: intersecao
    Returns:
        bool: Verifica se a intersecao é valida no goban.
    """
    if eh_goban(g) and eh_intersecao(i):
        lin, col = inter_para_indicie(i)
        if 1 <= col + 1 <= len(g) and 1 <= lin + 1 <= len(g[0]):
            return True
    return False

# Teste
def gobans_iguais(g1, g2):
    """
    Verifica se os gobans são iguais.
    Args:
        g1: goban
        g2: goban
    Returns:
        bool: True se forem gobans iguais, False se não.
    """
    if eh_goban(g1) and eh_goban(g2):
        return g1 ==  g2
    return False

# Transformadores
def goban_para_str(g):
    """
    Transforma o goban em uma string.
    Args:
        g: goban
    Returns:
        str: Retorna o goban.

    """
    if eh_goban(g):
        tamanho = len(g[0])
        linha_de_letras = ' '
        resultado = '   ' + ' '.join([chr(65 + i) for i in range(len(g))]) + '\n' # Inicializa variáveis para construir a representação do território

        for i in range(tamanho):  # Itera pelas linhas do território e constrói a representação
            if i + 1 < 10:
                resultado += f' {i + 1} '
                for num_linha in g:
                    lugar = num_linha[i]
                    resultado += f'{lugar} '
                resultado += f' {i + 1}\n'
            else:
                resultado += f'{i + 1} '
                for num_linha in g:
                    lugar = num_linha[i]
                    resultado += f'{lugar} '
                resultado += f'{i + 1}\n'

        resultado += '   ' + ' '.join([chr(65 + i) for i in range(len(g))])

        lugar_linhas = resultado.split('\n') # Inverte a ordem das linhas para correspondência com a exibição tradicional do tabuleiro
        lugar_linhas.reverse()
        caminho = lugar_linhas

        t_string = '\n'.join(caminho) + linha_de_letras

        return t_string.rstrip()

# Funções de alto nível
def obtem_territorios(g):
    """
    Obtem o territorio de cada jogador.
    Args:
        g: goban
    Returns:
        tuple: Retorna um tuplo com os territorios de cada jogador.
    """
    if eh_goban(g):
        territorio = []
        colunas = len(g[0])
        linhas = len(g)

        for lin in range(linhas):
            for col in range(colunas):
                if g[col][lin] == '.':
                    if obtem_cadeia(g, (chr(col + 65), lin + 1)) not in territorio:
                        territorio.append(obtem_cadeia(g, (chr(col + 65), lin + 1)))
    return tuple(territorio)

def obtem_adjacentes_diferentes(g, t):
    """
    Obtem as intersecoes adjacentes mas de tipos diferentes.
    Args:
        g: goban
        t: tuplo de intersecoes
    Returns:
        tuple: Retorna um tuplo com intersecoes adjacentes mas de tipos diferentes.
    """
    if eh_goban(g):
        adj_diferentes = set()
        for inter in t:
            adjacentes = obtem_intersecoes_adjacentes(inter, obtem_ultima_intersecao(g))
            for adjacente in adjacentes:
                if obtem_pedra(g, adjacente) == '.' and obtem_pedra(g, inter) != '.':
                    adj_diferentes.add(adjacente)
                if obtem_pedra(g, adjacente) != '.' and obtem_pedra(g, inter) == '.':
                    adj_diferentes.add(adjacente)

        return ordena_intersecoes(ordena_intersecoes(adj_diferentes))

def tem_liberdades(g, i):
    """
    Verifica se i tem liberdades.
    Args:
        g: goban
        i: intersecao
    Returns:
        bool:True se tiver liberdades, False se não.
    """
    if len(i) >= 3:
        for inter in i:
            adjacentes = obtem_intersecoes_adjacentes(inter, obtem_ultima_intersecao(g))
            for adjacente in adjacentes:
                if obtem_pedra(g, adjacente) == '.':
                    return True
        return False
    else:
        adjacentes = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))
        for adj in adjacentes:
            if obtem_pedra(g, adj) == '.':
                return True
        return False

def jogada(g, i, p):
    """
    Realiza uma jogada.
    Args:
        g: goban
        i: intersecao
        p: pedra
    Returns:
        goban: retorna o goban depois de realizada a jogada .
    """
    if obtem_pedra(g, i) == '.':
        coloca_pedra(g, i, p)

        jogador_contrario = 'O' if p == 'X' else 'X'
        adjacentes = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))
        for adjacente in adjacentes:
            cadeia_adversario = obtem_cadeia(g, adjacente)
            if obtem_pedra(g, adjacente) == jogador_contrario:
                if not tem_liberdades(g, cadeia_adversario):
                    for intersecao in cadeia_adversario:
                        remove_pedra(g, intersecao)

        return g
        
def obtem_pedras_jogadores(g):
    """
    Obtem as pedra de cada jogador.
    Args:
        col (str): Coluna da interseção (de 'A' a 'S').
        lin (int): Linha da interseção (de 1 a 19).
    Returns:
        tuple: Retorna um tuplo com as pedras de cada jogador.
    """
    lin, col = len(g[0]), len(g)
    brancos = 0
    pretos = 0
    for x in range(lin):
        for y in range(col):
            if g[y][x] == 'O':
                brancos += 1
            elif g[y][x] == 'X':
                pretos += 1

    return brancos, pretos

def eh_goban_vazio(g):
    """
    Verifica se é um goban vazio.
    Args:
        g: goban
    Returns:
        bool:True se for um goban vazio, False se não.
    """
    if eh_goban(g):
        for linha in g:
            for intersecao in linha:
                if intersecao != '.':
                    return False 
        return True  

# Funções adicionais
def calcula_pontos(g):
    """
    Calcula o número de pontos de cada jogador.
    Args:
        g: goban
    Returns:
        int:Retorna os pontos dos dois jogadores.
    """
    if eh_goban_vazio(g):
        return (0, 0)

    pontos_brancos, pontos_pretos = obtem_pedras_jogadores(g)

    for territorio in obtem_territorios(g):
        intersecoes_adjacentes = obtem_adjacentes_diferentes(g, territorio)
        todas_pedras_brancas = all(pedras_iguais(obtem_pedra(g, inter), cria_pedra_branca()) for inter in intersecoes_adjacentes)
        todas_pedras_pretas = all(pedras_iguais(obtem_pedra(g, inter), cria_pedra_preta()) for inter in intersecoes_adjacentes)

        if todas_pedras_brancas:
            pontos_brancos += len(territorio)
        if todas_pedras_pretas:
            pontos_pretos += len(territorio)

    return (pontos_brancos, pontos_pretos)

def captura_pedra(g, i, p):
    """
    Verifica se a pedra foi capturada.
    Args:
        g: goban
        i: intersecao
        p: pedra
    Returns:
        bool:True se a pedra foi capturada, False se não.
    """
    if not eh_intersecao_valida(g, i) or obtem_pedra(g, i) != '.':
        return False
    
    jogador_adversario = 'O' if p == 'X' else 'X'
    adjacentes = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))
    capturou_pedra = False
    
    for adj in adjacentes:
        if obtem_pedra(g, adj) == jogador_adversario and not tem_liberdades(g, adj):
            remove_pedra(g, adj)
            capturou_pedra = True
            
    return capturou_pedra

def eh_jogada_legal(g, i, p, l):
    """
    Verifica se a jogada é legal.
    Args:
        g: goban
        i: intersecao
        p: pedra
        l: estado do goban que não pode ser obtido após a jogada.
    Returns:
        bool:False se não for legal, True se for.
    """
    if not (eh_goban(g) and eh_goban(l) and eh_intersecao_valida(g, i) and eh_pedra_jogador(p)):
        return False

    copia_g = cria_copia_goban(g)

    if not eh_pedra_jogador(obtem_pedra(copia_g, i)):
        dif = obtem_adjacentes_diferentes(copia_g, obtem_cadeia(copia_g, i))

        if len(dif) != 0 and all(obtem_pedra(copia_g, elemento) == p for elemento in dif):
            jogada(copia_g, i, p)
            if copia_g != l and tem_liberdades(copia_g, i):
                return True
            return False
        elif len(dif) != 0 and all(obtem_pedra(copia_g, elemento) != p for elemento in dif):
            jogada(copia_g, i, p)
            if copia_g != l and tem_liberdades(copia_g, i):
                return True
            return False
        return False

    return False

def turno_jogador(g, p, l):
    """
    Oferece a opção de passar ou de colocar uma pedra numa intersecao propria.
    Args:
        g: goban
        p: pedra
        l: estado do goban que não pode ser obtido após a jogada.
    Returns:
        bool:False se o jogador passar True se não.
    """
    while True:
        acao = input(f"Escreva uma intersecao ou 'P' para passar [{p}]:").strip().upper()
        if acao == 'P':
            return False
        if eh_intersecao_valida(g, str_para_intersecao(acao)) and eh_jogada_legal(g, str_para_intersecao(acao), p, l):
            jogada(g, str_para_intersecao(acao), p)
            return True

def go(n, tb, tn):
    # Verificar a validade dos argumentos
    if not isinstance(n, int) or n not in (9, 13, 19):
        raise ValueError('go: argumentos invalidos')
    
    if not isinstance(tb, tuple) or not isinstance(tn, tuple):
        raise ValueError('go: argumentos invalidos')

    g = cria_goban(n, tb, tn)

    jogador_atual = 'X'

    ultima_acao_jogador_branco = None
    ultima_acao_jogador_preto = None

    while True:
        if jogador_atual == 'X':
            acao = turno_jogador(g, cria_pedra_branca(), ultima_acao_jogador_branco)
            ultima_acao_jogador_branco = acao
        else:
            acao = turno_jogador(g, cria_pedra_preta(), ultima_acao_jogador_preto)
            ultima_acao_jogador_preto = acao
        
        if ultima_acao_jogador_branco == 'P' and ultima_acao_jogador_preto == 'P':
            pontos = calcula_pontos(g)
            if pontos[0] > pontos[1]:
                return True
            else:
                return False
        
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

