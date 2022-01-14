from random import random
from random import choice

grelha =  [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]

fim = False
vitoria = False
pontos = 0

def set_2ou4():
    x = random()

    if x < 0.9:
        return 2
    else:
        return 4

def get_posicoes_vazias(grelha):
    posicoes_vazias = []
    for linha in [0, 1, 2, 3]:
        for coluna in [0, 1, 2, 3]:
            if grelha[linha][coluna] == 0 :
                posicao_vazia = [linha, coluna]
                posicoes_vazias.append(posicao_vazia)
    return (posicoes_vazias)


def inserir_2ou4(grelha):

    dois_ou_quatro = set_2ou4()
    posicoes_vazias = get_posicoes_vazias(grelha)
    posicao_vazia = choice(posicoes_vazias)
    linha = posicao_vazia[0]
    coluna = posicao_vazia[1]
    grelha[linha][coluna] = dois_ou_quatro

def novo_jogo():
    grelha =[[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

    fim = False
    vitoria = False
    pontos = 0
    inserir_2ou4(grelha)
    inserir_2ou4(grelha)
    jogo = (grelha, fim, vitoria, pontos)
    return jogo


def valor(jogo, linha, coluna):
    grelha = jogo[0]
    return grelha[linha][coluna]

def terminou(jogo):
    fim = jogo[1]
    return fim


def mover_esquerda(uma_lista, movimento): 
    resultado = []
    for valor in uma_lista:
        if valor != 0:
               resultado.append(valor)
    while len(resultado) < len(uma_lista):
            resultado.append(0)


    for y in range(len(uma_lista)):
        if uma_lista[y] != resultado[y]:
            movimento = True
        

    return (resultado, movimento)

def somar_esquerda(uma_lista, movimento, pontos):
    
    resultado = []
    vitoria = False
    index = 0
    
    while(index < len(uma_lista) - 1):
        if uma_lista[index] == uma_lista[index + 1]:
            soma = uma_lista[index] + uma_lista[index + 1]
            resultado.append(soma)
            index = index + 2
            if soma > 0:
                movimento = True
                pontos = pontos + soma
        else:
            resultado.append(uma_lista[index])
            index = index + 1
    if(index == len(uma_lista) - 1):
        resultado.append(uma_lista[index])
    while(len(resultado) < len(uma_lista)):
        resultado.append(0)

    return (resultado, movimento, pontos, vitoria) 


def ha_iguais_adjacentes(grelha):
    ha = False
    for i in [0, 1, 2, 3]:
        for j in [0, 1, 2]:
            if grelha[i][j] != 0 and grelha[i][j] == grelha[i][j + 1]:
                ha = True
    for j in [0, 1, 2, 3]:
        for i in [0, 1, 2]:
            if grelha[i][j] != 0 and grelha[i][j] == grelha[i + 1][j]:
                ha = True
    return ha

def actualizar_jogo(jogo, movimento):

    grelha = jogo[0]

    fim =  False

    if movimento ==  True :
        inserir_2ou4(grelha)
    posicoes_vazias = get_posicoes_vazias(grelha)
    if(len(posicoes_vazias) == 0) and  (ha_iguais_adjacentes(grelha) == False):
        fim =  True

    return fim

def get_vitoria(jogo):
    vitoria  =  False
    for linha in [0, 1, 2, 3]:
        for coluna in [0, 1, 2, 3]:
            valor_procurado = valor(jogo, linha, coluna)
            if valor_procurado >= 2048:
                vitoria = True
            

    return vitoria

def esquerda(jogo):

    grelha = jogo[0]
    pontos = jogo[3]
    movimento =  False
    for i in [0, 1, 2, 3]:

        (aux, movimento) = mover_esquerda(grelha[i], movimento)
        (nova_linha, movimento, pontos, vitoria) = somar_esquerda(aux, movimento, pontos)

        grelha[i] = nova_linha

    fim = actualizar_jogo(jogo, movimento)
    vitoria = get_vitoria(jogo)
    jogo_actualizado = (grelha, fim, vitoria, pontos)

    return jogo_actualizado

def reverter_linhas(grelha):
    resultado = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]
    
    for linha in [0, 1, 2, 3]:
        for coluna in [0, 1, 2, 3]:
            resultado[linha][3 - coluna] = grelha[linha][coluna]
    return resultado
       
def direita(jogo):
    (grelha, fim, vitoria, pontos) = jogo
    grelha_revertida = reverter_linhas(grelha)
    jogo_revertido = (grelha_revertida, fim, vitoria, pontos)
    jogo_revertido_actualizado = esquerda(jogo_revertido)
    (grelha, fim, vitoria, pontos) = jogo_revertido_actualizado
    grelha_revertida = reverter_linhas(grelha)
    jogo_actualizado = (grelha_revertida, fim, vitoria, pontos)
    return jogo_actualizado

def trocar_linhas_com_colunas(grelha):
    resultado = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]

    for coluna in [0, 1, 2, 3]:
        for linha in [0, 1, 2, 3]:
            resultado [linha][coluna] = grelha [coluna][linha]
    return resultado

def acima(jogo):
    (grelha, fim, vitoria, pontos) = jogo
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_transposto = (grelha_transposta, fim, vitoria, pontos)
    jogo_transposto_actualizado = esquerda(jogo_transposto)
    (grelha, fim, vitoria, pontos) = jogo_transposto_actualizado
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_actualizado = (grelha_transposta, fim, vitoria, pontos)
    return jogo_actualizado

def abaixo(jogo):
    (grelha, fim, vitoria, pontos) = jogo
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_transposto = (grelha_transposta, fim, vitoria, pontos)
    jogo_transposto_actualizado = direita(jogo_transposto)
    (grelha, fim, vitoria, pontos) = jogo_transposto_actualizado
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_actualizado = (grelha_transposta, fim, vitoria, pontos)
    return jogo_actualizado



def pontuacao(jogo):
    pontuacao = jogo[3]
    return pontuacao

    





