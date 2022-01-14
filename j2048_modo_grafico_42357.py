import pygame
#importar funcoes dos ficheiros motor e gestor
from j2048_motor_42357 import set_2ou4, get_posicoes_vazias, inserir_2ou4, novo_jogo, ha_iguais_adjacentes, valor, terminou, get_vitoria, pontuacao, mover_esquerda, somar_esquerda, direita, esquerda, acima, abaixo
from j2048_gestor_42357 import get_numero, get_amigos, le_identificacao, inicializa_semente, regista_grelha_inicial, regista_jogada, regista_pontos, regista_ranking, escreve_registo
#from j2048_modo_texto_42357 import ocupar_5_espacos, imprimir
#inicializar pygame
pygame.init()

#janela#
largura = 500
altura = 500
global tamanho
tamanho = (largura, altura)
janela = pygame.display.set_mode(tamanho)
#imagens de fundo#
background = pygame.image.load("lego.bmp")
background2 = pygame.image.load("lego10.bmp")
background3 = pygame.image.load("lego5.bmp")
#atualizacao da janela#
frame_rate = 10
clock = pygame.time.Clock()
#dicionario de cores#
COR1 = (255, 102, 102)
COR2 = (255, 102, 178)
COR3 = (178, 102, 255)
COR4 = (102, 102, 255)
COR5 = (192, 192, 192)
COR6 = (102, 178, 255)
COR7 = (102, 255, 255)
COR8 = (102, 255, 178)
COR9 = (102, 255, 102)
COR10 = (178, 255, 102)
COR11 = (255, 255, 102)
COR12 = (255, 178, 102)
COR13 = (224, 224, 224)
COR14 = (153, 204, 255)
COR15 = (255, 204, 153)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
lista_cor = {0:BLACK, 2:COR1, 4:COR12, 8:COR11, 16:COR10, 32:COR9, 64:COR8, 128:COR7, 256:COR6, 512:COR5, 1024:COR4, 2048:COR3} 
#funcao associativa cores -> valores
def get_cor(i):
    return lista_cor[i]

#variaveis auxiliares#
pos_nr_x = int(largura/2)
pos_nr_y = int(altura/2)
#font_size = 25
#font = pygame.font.Font(None, font_size)
antialias = True
numero = 0
nova_frame = None#imagem que é constantemente atualizada e colada por cima da frame anterior
#inicialização das variáveis de jogo
jogo = novo_jogo()
global fim#fim por grelha preenchida
fim = False
global fim2#fim usando 'q'
fim2 = False
global done#utilizada para sair do ciclo while que controla o jogo
done = False
global jogar#alterar entre janela inicial e janela de jogo
jogar = False
jogo = ([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], False, False, 0, False)



def processar_eventos_pygame():
    global fim
    global numero
    global pos_nr_x
    global pos_nr_y
    global jogo
    global fim2
    global done
    global jogar
    letra = ""
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                fim2 = True
                fim = True
            elif event.key == pygame.K_x:
                done = True
                #pygame.quit()
            elif event.key == pygame.K_p:
                #inicia o jogo a partir da janela inicial
                #inicializa todas as variaveis de jogo
                fim2 = False
                fim = False
                jogar = True
                le_identificacao()
                inicializa_semente(None)
                jogo = novo_jogo()
                global grelha
                grelha = jogo[0]
                fim = jogo[1]
                regista_grelha_inicial(grelha[0][0], grelha[0][1], grelha[0][2], grelha[0][3],
                                       grelha[1][0], grelha[1][1], grelha[1][2], grelha[1][3],
                                       grelha[2][0], grelha[2][1], grelha[2][2], grelha[2][3],
                                       grelha[3][0], grelha[3][1], grelha[3][2], grelha[3][3])
            elif event.key == pygame.K_w:
                #volta á janela inicial
                jogar = False
                janela_inicial()
            elif event.key == pygame.K_LEFT:
                letra = "a"
                jogo = esquerda(jogo)
                regista_jogada(letra)
                pos_nr_x = pos_nr_x - 10
            elif event.key == pygame.K_RIGHT:
                letra = "d"
                jogo = direita(jogo)
                regista_jogada(letra)
                pos_nr_x = pos_nr_x + 10
            elif event.key == pygame.K_UP:
                letra = "w"
                jogo = acima(jogo)
                regista_jogada(letra)
                pos_nr_y = pos_nr_y - 10
            elif event.key == pygame.K_DOWN:
                letra = "s"
                jogo = abaixo(jogo)
                regista_jogada(letra)
                pos_nr_y = pos_nr_y + 10
            elif event.key == pygame.K_n:
                #termina o jogo atual
                #regista a pontuacao
                #imprime a mensagem_cloud
                #inicia um novo jogo 
                fim2 = False
                fim = terminou(jogo)
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
                                       grelha[3][0], grelha[3][1], grelha[3][2], grelha[3][3])


#janela inicial
def janela_inicial():
    #nova_frame.fill(BLACK)
    pygame.font.init()#iniciar função font
    default_font = pygame.font.get_default_font()#carregar font standard
    font_renderer = pygame.font.Font(default_font, 25)#escrever com tipo de font x e tamanho de letra y
    texto = font_renderer.render("use arrow keys to play", antialias, WHITE)#("texto", focar texto, cor do texto)
    nova_frame.blit(texto, (20, 200))#posicao da janela onde o texto é renderizado
    texto2 = font_renderer.render("'q' to quit game", antialias, WHITE)
    nova_frame.blit(texto2, (20, 350))
    texto3 = font_renderer.render("'n' for new game", antialias, WHITE)
    nova_frame.blit(texto3, (20, 300))
    texto4 = font_renderer.render("'x' to exit", antialias, WHITE)
    nova_frame.blit(texto4, (20, 400))
    texto5 = font_renderer.render("to start game press 'p'", antialias, WHITE)
    nova_frame.blit(texto5, (20, 150))
    texto6 = font_renderer.render("press 'w' to return to setting's window", antialias, WHITE)
    nova_frame.blit(texto6, (20, 250))

    #titulo 2048
    font_renderer = pygame.font.Font(default_font, 50)
    texto1 = font_renderer.render("2048", antialias, WHITE)
    nova_frame.blit(texto1, (20, 50))

def mostrar_pontuacao(jogo):
    pontos = pontuacao(jogo)#atualizar pontos segundo funcao pontuacao
    pygame.font.init()
    default_font = pygame.font.get_default_font()
    font_renderer = pygame.font.Font(default_font, 25)        
    texto = font_renderer.render("Pontos: " + str(pontos), antialias, WHITE)#renderizar "Pontos:" + String(pontos atualizados segundo def pontuacao) 
    nova_frame.blit(texto, (30, 450))
    
def mostrar_vitoria(jogo):
    vitoria = get_vitoria(jogo)#atualizar vitoria=True or vitoria=False
    if vitoria == True:
        #quando vitoria = True
        #renderizar "Congrats! You Won!
        #jogo continua
        #so é atualizado o estado vitoria
        pygame.font.init()
        default_font = pygame.font.get_default_font()
        font_renderer = pygame.font.Font(default_font, 25)        
        texto = font_renderer.render("Congrats! You Won!", antialias, WHITE)
        nova_frame.blit(texto, (220, 450))
        
def finalizar_jogo(jogo):
    grelha = jogo[0]
    pontos = pontuacao(jogo)
    vitoria = get_vitoria(jogo)
    #nova_frame.fill(BLACK)
    pygame.font.init()
    default_font = pygame.font.get_default_font()
    font_renderer = pygame.font.Font(default_font, 50)
    #quando fim = True
    #seja quando se pressiona 'q' como quando não ha movimento possivel na grelha
    #dependendo da vitoria = True ou vitoria = False
    if vitoria == True:
        #aparece uma janela de vitoria = True
        nova_frame.blit(background2, (0, 0))
        janela.blit(nova_frame, (0, 0))
        texto2 = font_renderer.render("Congrats!", antialias, COR11)
        nova_frame.blit(texto2, (20, 50))
        texto1 = font_renderer.render("You Won!", antialias, COR11)
        nova_frame.blit(texto1, (50, 100))
    else:
        #ou uma de vitoria = False
        nova_frame.blit(background3, (0, 0))
        janela.blit(nova_frame, (0, 0))
        texto2 = font_renderer.render("Sorry, you lost", antialias, COR10)
        nova_frame.blit(texto2, (10, 340))
        texto3 = font_renderer.render("Press 'n'", antialias, COR4)
        nova_frame.blit(texto3, (10, 390))
        texto4 = font_renderer.render("to try again", antialias, COR6)
        nova_frame.blit(texto4, (90, 430))
        
def construir_grelha(grelha):
    #para cada posicao grelha []linha] [coluna]
    for coluna in [0, 1, 2, 3]:
        for linha in [0, 1, 2, 3]:
            #dependendo do valor dessa posicao 
            val = valor(jogo, linha, coluna)
            cor = get_cor(val)
            if val >= 2:
                #é desenhado um quadrado com uma cor específica e o valor da posicao
                pygame.draw.rect(nova_frame, cor, (coluna*100 + 50, linha*100 + 35, 95, 95))#desenha um quadrado (posicao_x, posicao_y, tamanho_x, tamanho_y)
                pygame.font.init()
                default_font = pygame.font.get_default_font()
                font_renderer = pygame.font.Font(default_font, 25)        
                posicao = font_renderer.render(str(val), antialias, BLACK)
                nova_frame.blit(posicao, (coluna*100 + 60, linha*100 + 60))
    
def construir_nova_frame():
    global nova_frame
    global jogar
    #cria janela com dimensões definidas
    nova_frame = pygame.Surface(tamanho)
    #cola imagem de fundo na frame
    nova_frame.blit(background, (0, 0))
    #nova_frame.fill(BLACK)
    janela.blit(nova_frame, (0, 0))
    #atualiza janela de acordo com nova_frame
    if jogar == True:
        #clicando em 'p' -> jogar=True
        #altera a nova_frame
        construir_grelha(grelha)
        mostrar_pontuacao(jogo)
        mostrar_vitoria(jogo)
        fim = terminou(jogo)
        if fim == True or fim2 == True:
            #quando fim = True émostrada a janela de fim de jogo
            finalizar_jogo(jogo)
            regista_pontos(pontuacao(jogo))
            mensagem_cloud = escreve_registo()
            print(mensagem_cloud)
    else:
        #se jogar = False mantem nova_frame na janela inicial
        janela_inicial()
    
    
while done == False:
    #enquanto done = True
    #seja enquanto não se pressiona 'x'
    #o ciclo continua a correr
    #a construir nova_frame
    #a esperar comandos
    processar_eventos_pygame()
    construir_nova_frame()
    janela.blit(nova_frame, (0, 0))
    pygame.display.flip()
    clock.tick(frame_rate)
    numero = numero + 1

#pressionando 'x'
#regista os pontos
#imprime a mensagem_cloud
#sai do pygame
regista_pontos(pontuacao(jogo))
mensagem_cloud = escreve_registo()
print(mensagem_cloud)
pygame.quit()
