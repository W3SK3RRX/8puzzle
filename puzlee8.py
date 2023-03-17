estadoInicial = [[1, 5, 2], [4, 8, 3], [0, 7, 6]]
estadoInicial = [[1, 5, 2], [0, 8, 3], [4, 7, 6]]
estadoFinal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
fronteira = [(estadoInicial,[])]
visitado = set()

def acharVazio(estado):
    for i in range(3):
        for j in range(3):
            if estado[i][j] == 0:
                return i, j
            
def verificarEstado(estadoInicial, estadoFinal):
    for i in range(3):
            for j in range(3):
                if estadoInicial[i][j] != estadoFinal[i][j]:
                    return False
    return True

def mover(estado):
    vazio = acharVazio(estado)
    movimento = []
    if vazio[0] > 0:
        novoEstado = [linha[:] for linha in estado]
        novoEstado[vazio[0]][vazio[1]] = novoEstado[vazio[0]-1][vazio[1]]
        novoEstado[vazio[0]-1][vazio[1]] = 0
        movimento.append(('cima',novoEstado))

    if vazio[0] < 2:
        novoEstado = [linha[:] for linha in estado]
        novoEstado[vazio[0]][vazio[1]] = novoEstado[vazio[0]+1][vazio[1]]
        novoEstado[vazio[0]+1][vazio[1]] = 0
        movimento.append(('baixo',novoEstado))

    if vazio[1] > 0:
        novoEstado = [linha[:] for linha in estado]
        novoEstado[vazio[0]][vazio[1]] = novoEstado[vazio[0]][vazio[1]-1]
        novoEstado[vazio[0]][vazio[1]-1] = 0
        movimento.append(('esquerda',novoEstado))

    if vazio[1] < 2:
        novoEstado = [linha[:] for linha in estado]
        novoEstado[vazio[0]][vazio[1]] = novoEstado[vazio[0]][vazio[1]+1]
        novoEstado[vazio[0]][vazio[1]+1] = 0
        movimento.append(('direita',novoEstado))
    
    return movimento

def resolver():
    contador = 0
    while fronteira:
        atual, caminho = fronteira.pop(0)
        if verificarEstado(atual,estadoFinal):
            return caminho
        visitado.add(str(atual))
        movimentos = mover(atual)
        for movimento in movimentos:
            if str(movimento[1]) not in visitado:
                contador += 1
                fronteira.append((movimento[1], caminho + [movimento[0]]))


resposta = resolver()
if resposta:
    print(*estadoInicial,sep='\n')
    print("Solução encontrada em {} passos:".format(len(resposta)))
    for movimento in resposta:
        print(movimento)
else:
    print("Não foi possível encontrar uma solução.")

    
