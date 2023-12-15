def eh_territorio(arg):
    """eh_territorio(arg) recebe um argumento e verifica se é território, sem nunca gerar erros.
    Args:
        arg: este argumento pode ser de qualquer tipo

    Returns:
        retorna True se for território e retorna False se não for
    """
    if not isinstance(arg, tuple):
        return False
    if not arg:
        return False
    if len(arg) > 26:
        return False

    prim_len = None

    for i in arg:
        if not isinstance(i, tuple):
            return False
        if len(i) > 99:
            return False
        if prim_len is None:
            prim_len = len(i)
        elif len(i) != prim_len:
            return False
        for item in i:
            if not(type(item) == int and item in (0, 1)):
                return False
    return True

def obtem_ultima_intersecao(t):
    """obtem ultima intersecao(t) recebe um território e devolve a intersecao do extremo superior
        direito do território.

    Args:
        arg(tuple): Recebe um território

    Returns:
        _tuple_: última interseção desse território
    """
    n_v = len(t)
    n_h = len(t[0])
    for h in range(n_h - 1, -1, -1):
        for v in range(n_v - 1, -1, -1):
                return (chr(ord('A') + v), h +1)

def eh_intersecao(arg):
    """eh intersecao(arg) recebe um argumento de qualquer tipo e devolve True se o seu argumento
        corresponde a uma interseção e False caso contrário, sem nunca gerar erros.

    Args:
        arg(tuple): Recebe um território

    Returns:
        _bool_: Se for interseção devolve True caso contrário devolve False
    """
    if arg == None or not isinstance(arg, tuple) or len(arg) != 2:
        return False
    if not(isinstance(arg[0], str)) or isinstance(arg[0], bool) or not(len(arg[0]) == 1) or isinstance(arg[1], bool) or not(type(arg[1]) == int):
        return False
    if not (ord('A') <= ord(arg[0]) <= ord('Z')) or not (1 <= arg[1] <= 99):
        return False
    return True

def eh_intersecao_valida(t, i):
    """eh intersecao valida(t, i) recebe um território e uma interseção, e devolve True se a
        interseçãoo corresponde a uma interseção do território, e False caso contrário.

    Args:
        t (_tuple_): recebe um território
        i (_tuple_): recebe uma interseção

    Returns:
        _bool_: devolve True se a interseçãoo corresponde a uma interseção do território, e False caso contrário.
    """
    if eh_territorio(t) and eh_intersecao(i):
        n_v = len(t)
        n_h = len(t[0])
        v, h = ord(i[0]) - ord('A'), i[1] - 1

        if 0 <= v < n_v and 0 <= h < n_h:
            return True

    return False

def eh_intersecao_livre(t, i):
    """eh intersecao livre(t, i) recebe um território e uma interseção do território, e devolve
        True se a interseção corresponde a uma interseçãao livre (não ocupada por montanhas)
        dentro do território e False caso contrário.

    Args:
        t (_tuple_): recebe um território
        i (_tuple_): recebe uma interseção desse território
    Returns:
        _bool_: e devolve True se a interseção corresponde a uma interseçãao livre 
        (não ocupada por montanhas) dentro do território e False caso contrário.
    """
    if eh_territorio(t) and eh_intersecao_valida(t, i):
        v, h = ord(i[0]) - ord('A'), i[1] - 1
        if t[v][h] == 0:
            return True
    return False

def obtem_intersecoes_adjacentes(t, i):
    """obtem intersecoes adjacentes(t, i) recebe um território e uma interseção do território, e
        devolve o tuplo formado pelas interseções válidas adjacentes da interseção em ordem de
        leitura de um território.

    Args:
        t (_tuple_): recebe um território
        i (_tuple_): recebe uma interseção desse território

    Returns:
        _tuple_: devolve o tuplo formado pelas interseções válidas adjacentes da interseção dada no argumento
    """
    intersecoes_adjacentes = []
    if eh_territorio(t) and eh_intersecao_valida(t, i):
        n_h = len(t[0])
        n_v = len(t)
        v, h = ord(i[0]) - ord('A'), i[1] - 1
        adjacentes = [(v-1, h), (v+1, h), (v, h-1), (v, h+1)]

        for av, ah in adjacentes:
          if 0 <= av < n_v and 0 <= ah < n_h:
            adj_i = (chr(ord('A') + av), ah + 1)
            intersecoes_adjacentes.append(adj_i)

    return ordena_intersecoes(tuple(intersecoes_adjacentes))

def ordena_intersecoes(t):
    """ordena intersecoes(tup) recebe um tuplo de interseçoes (potencialmente vazio) e devolve
        um tuplo contendo as mesmas interseções ordenadas de acordo com a ordem de leitura
        do território.

    Args:
        t (_tuple_): recebe um tuplo de interseçoes

    Returns:
        _tuple_: devolve esse mesmo tuplo mas ordenado de acordo com a ordem de leitura
    """
    if isinstance(t, tuple):
      def chave_ordenacao(intersecao):
        return (intersecao[1], intersecao[0])

      intersecoes_ordenadas = sorted(t, key= chave_ordenacao)
      return tuple(intersecoes_ordenadas)

def territorio_para_str(t):
    """territorio para str(t) recebe um território e devolve a cadeia de caracteres que o representa.

    Args:
        t (_tuple_): recebe um território

    Raises:
        ValueError: Se o argumento dado for inválido, a função gera erro com a mensagem 'territorio_para_str: argumento invalido'.

    Returns:
        _str_: representação do território
    """
    if eh_territorio(t):
        tamanho = len(t[0])
        linha_de_letras = ' '
        resultado = '   ' + ' '.join([chr(65 + i) for i in range(len(t))]) + '\n' # Inicializa variáveis para construir a representação do território

        for i in range(tamanho):  # Itera pelas linhas do território e constrói a representação
            if i + 1 < 10:
                resultado += f' {i + 1} '
                for num_linha in t:
                    lugar = num_linha[i]
                    if lugar == 0:
                        resultado += '. '
                    elif lugar == 1:
                        resultado += 'X '
                resultado += f' {i + 1}\n'
            else:
                resultado += f'{i + 1} '
                for num_linha in t:
                    lugar = num_linha[i]
                    if lugar == 0:
                        resultado += '. '
                    elif lugar == 1:
                        resultado += 'X '
                resultado += f'{i + 1}\n'

        resultado += '   ' + ' '.join([chr(65 + i) for i in range(len(t))])

        lugar_linhas = resultado.split('\n') # Inverte a ordem das linhas para correspondência com a exibição tradicional do tabuleiro
        lugar_linhas.reverse()
        caminho = lugar_linhas

        t_string = '\n'.join(caminho) + linha_de_letras

        return t_string.rstrip()
    else:
        raise ValueError("territorio_para_str: argumento invalido")

def obtem_cadeia(t, i):
    """obtem cadeia(t,i) recebe um território e uma interseção do território (ocupada por uma
        montanha ou livre), e devolve o tuplo formado por todas as interseções que estão conetadas
        a essa interseção ordenadas (incluida si própria) de acordo com a ordem de leitura
        de um território. 

    Args:
        t (_tuple_): recebe um território
        i (_tuple_): recebe uma interseção do território

    Raises:
        ValueError: Se algum dos argumentos dado for inválido, a função gera um
        erro com a mensagem 'obtem_cadeia: argumentos invalidos'.

    Returns:
        _tuple_: tuplo formado por todas as interseções que estão conetadas
            a essa interseção ordenadas (incluida si própria)
    """
    if eh_territorio(t) and eh_intersecao_valida(t, i):

        cadeia = []
        inter_prox = [i]

        while inter_prox != []:
            intersecao = inter_prox.pop(0)
            cadeia.append(intersecao)
            intersecoes_adjacentes = obtem_intersecoes_adjacentes(t, intersecao)

            for elemento in intersecoes_adjacentes:
                if (eh_intersecao_livre(t, i) == eh_intersecao_livre(t, elemento)) and (elemento not in cadeia) and (elemento not in inter_prox):
                    inter_prox.append(elemento)

        return ordena_intersecoes(tuple(cadeia))
    
    else:
        raise ValueError('obtem_cadeia: argumentos invalidos')

def obtem_vale(t, i):
    """obtem vale(t,i) recebe um território e uma interseção do território ocupada por uma montanha,
    e devolve o tuplo (potencialmente vazio) formado por todas as interseções que formam
    parte do vale da montanha da interseção fornecida como argumento ordenadas de
    acordo á ordem de leitura de um território.

    Args:
        t (_tuple_): recebe um território
        i (_tuple_): recebe uma interseção do território ocupada por uma montanha

    Raises:
        ValueError: Se algum dos argumentos dado for inválido,
        a função gera um erro com a mensagem 'obtem_vale: argumentos invalidos'.

    Returns:
        _tuple_: devolve o tuplo (potencialmente vazio) formado por todas as interseções que formam
        parte do vale da montanha da interseção fornecida
    """
    if eh_territorio(t) and eh_intersecao_valida(t, i) and not eh_intersecao_livre(t, i):
        vale = ()
        for e in obtem_cadeia(t, i):  # Itera sobre as interseções da cadeia da montanha associada a i
            e_adj = obtem_intersecoes_adjacentes(t, e)
            for inter in e_adj: # Verifica se a interseção e inter têm o mesmo estado (livre/ocupada)
                if eh_intersecao_livre(t, i) != eh_intersecao_livre(t, inter) and inter not in vale:
                    vale += (inter, )

        return ordena_intersecoes(vale)

    else:
        raise ValueError('obtem_vale: argumentos invalidos')

def verifica_conexao(t, i1, i2):
    """verifica conexao(t,i1,i2) recebe um território e duas interseções do território e devolve
True se as duas interseções estão conetadas e False caso contrário.

    Args:
        t (_tuple_): recebe um território
        i1 (_tuple_): recebe uma interseção desse terrtótrio
        i2 (_tuple_): recebe outra interseção desse terrtótrio

    Raises:
        ValueError: Se algum dos argumentos dado for inválido, a função gera um erro com a mensagem
        'verifica_conexao: argumentos invalidos'.
    Returns:
        _bool_: devolve True se as duas interseções estão conetadas e False caso contrário.
    """
    if eh_territorio(t) and eh_intersecao_valida(t, i1) and eh_intersecao_valida(t, i2):
        return obtem_cadeia(t, i1) == obtem_cadeia(t, i2)
    else:
      raise ValueError('verifica_conexao: argumentos invalidos')

def obtem_intersecoes(t):
    """obtem_intersecoes(t) devolve um tuplo com as intersecoes ocupadas desse território
    Args:
        t (_tuple_): recebe um terrtório

    Returns:
        _tuple_: devolve um tuplo com as intersecoes ocupadas desse território
    """
    if eh_territorio(t):
        intersecoes = []

        for v in range(len(t)):
            for h in range(len(t[0])):
                if t[v][h] == 1:
                    intersecoes.append((chr(ord('A') + v), h + 1))

    return tuple(intersecoes)

def calcula_numero_montanhas(t):
    """calcula numero montanhas(t) recebe um território e devolve o número de interseções
        ocupadas por montanhas no território.

    Args:
        t (_tuple_): recebe um território

    Raises:
        ValueError: Se o argumento dado for inválido, a função
        gera um erro com a mensagem 'calcula_numero_montanhas: argumento invalido'.

    Returns:
        _int_: devolve o número de interseções devolve o número de interseções ocupadas por montanhas no território.
    """
    if eh_territorio(t):
        numero_montanhas = len(obtem_intersecoes(t))
    else:
        raise ValueError('calcula_numero_montanhas: argumento invalido')
    return numero_montanhas

def calcula_numero_cadeias_montanhas(t):
    """calcula tamanho vales(t) recebe um território e devolve o número total de interseções
diferentes que formam todos os vales do território.

    Args:
        t (_tuple_): recebe um terriótrio

    Raises:
        ValueError: Se o argumento dado for inválido, a função gera
        um erro com a mensagem 'calcula_numero_cadeias_montanhas: argumento invalido'.

    Returns:
        _int_: devolve o número total de interseções diferentes que formam todos os vales do território.
    """
    def obtem_cadeias_montanhas(t):
        intersecoes = obtem_intersecoes(t)
        num_cad_mon = []
        visitados = set()

        for intersecao in intersecoes:
            if intersecao not in visitados:
                cad_mon = [intersecao] # Inicializa uma lista para armazenar a cadeia de montanha
                visitados.add(intersecao)
                fila = [intersecao]

                while fila:
                    atual = fila.pop(0) # Encontra vizinhos não visitados que estão conectados à interseção atual
                    vizinhos = [v for v in intersecoes if verifica_conexao(t, atual, v) and v not in visitados]
                    for vizinho in vizinhos:
                        fila.append(vizinho)
                        visitados.add(vizinho)
                        cad_mon.append(vizinho) # Adiciona o vizinho à cadeia de montanha

                num_cad_mon.append(cad_mon) # Adiciona a cadeia de montanha à lista de cadeias

        return num_cad_mon

    if eh_territorio(t):
        num_cad_mon = obtem_cadeias_montanhas(t)
        return len(num_cad_mon)
    else:
        raise ValueError('calcula_numero_cadeias_montanhas: argumento invalido')
    
def calcula_tamanho_vales(t):
    """calcula tamanho vales(t) recebe um território e devolve o número total de interseções
        diferentes que formam todos os vales do território.

    Args:
        t (_tuple_): recebe um território

    Raises:
        ValueError: Se o argumento dado for inválido, a função gera um erro com a mensagem
        'calcula_tamanho_vales: argumento invalido'.

    Returns:
        _int_: devolve o tamanho de um vale
    """
    if eh_territorio(t):
        vales = []
        cad_mon = obtem_intersecoes(t)
        for cadeia in cad_mon:
            for intersecao in obtem_vale(t, cadeia):
                if intersecao not in vales:
                    vales.append(intersecao)
        return len(vales)

    else:
        raise ValueError('calcula_tamanho_vales: argumento invalido')