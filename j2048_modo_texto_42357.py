from j2048_motor_42357 import set_2ou4, get_posicoes_vazias, inserir_2ou4, novo_jogo, ha_iguais_adjacentes, valor, terminou, get_vitoria, pontuacao, mover_esquerda, somar_esquerda, direita, esquerda, acima, abaixo
from j2048_gestor_42357 import get_numero, get_amigos, le_identificacao, inicializa_semente, regista_grelha_inicial, regista_jogada, regista_pontos, regista_ranking, escreve_registo


def ocupar_5_espacos(n):
    txt = str(n)
    while len(txt) < 5:
        txt = " " + txt

    return txt


def imprimir(jogo):
    for linha in [0, 1, 2, 3]:
        uma_linha = ""
        for coluna in [0, 1, 2, 3]:
            uma_linha = uma_linha + ocupar_5_espacos(valor(jogo, linha, coluna))
        print(uma_linha)
    print(jogo[1])
    print(jogo[2])
    print(jogo[3])

le_identificacao()
inicializa_semente(None)

jogo = novo_jogo()
grelha = jogo[0]
regista_grelha_inicial(grelha[0][0], grelha[0][1], grelha[0][2], grelha[0][3],
                       grelha[1][0], grelha[1][1], grelha[1][2], grelha[1][3],
                       grelha[2][0], grelha[2][1], grelha[2][2], grelha[2][3],
                       grelha[3][0], grelha[3][1], grelha[3][2], grelha[3][3],)
imprimir(jogo)


while input("-") != "q":
    x = input("--")
    if x == "d":
        jogo = direita(jogo)
        regista_jogada("d")
        imprimir(jogo)
    elif x == "a":
        jogo = esquerda(jogo)
        regista_jogada("a")
        imprimir(jogo)
    elif x == "w":
        jogo = acima(jogo)
        regista_jogada("w")
        imprimir(jogo)
    elif x == "s":
        jogo = abaixo(jogo)
        regista_jogada("s")
        imprimir(jogo)
    elif x == "n":
        regista_pontos(pontuacao(jogo))
        mensagem_cloud = escreve_registo()
        print(mensagem_cloud)
        
        le_identificacao()
        inicializa_semente(None)
        jogo = novo_jogo()
        grelha = jogo[0]
        regista_grelha_inicial(grelha[0][0], grelha[0][1], grelha[0][2], grelha[0][3],
                               grelha[1][0], grelha[1][1], grelha[1][2], grelha[1][3],
                               grelha[2][0], grelha[2][1], grelha[2][2], grelha[2][3],
                               grelha[3][0], grelha[3][1], grelha[3][2], grelha[3][3],)
        imprimir(jogo)

regista_pontos(pontuacao(jogo))
mensagem_cloud = escreve_registo()
print(mensagem_cloud)



