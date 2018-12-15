import pygame, psutil

#cia a tela
largura_tela = 800
altura_tela = 600
margem_lateral = 20
margem_altura = 50
altura_barra = 70
preto = (0,0,0)
vermelho = (255,0,0)
azul = (0,0,255)
branco = (255, 255, 255)
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Uso de memória")
cont = 60

pygame.display.init()
pygame.font.init()

#Cria o relógio
clock = pygame.time.Clock()
# Inicia a fonte para escrever na tela do pygame

font = pygame.font.Font(None, 32)

# Função para mostrar o uso de memória
def mostra_uso_memoria():
    mem = psutil.virtual_memory()
    larg = largura_tela - 2*margem_lateral
    tela.fill(preto)
    pygame.draw.rect(tela, azul,(margem_lateral, margem_altura, larg, altura_barra))
    larg = larg*mem.percent/100
    pygame.draw.rect(tela, vermelho, (margem_lateral, margem_altura, larg, altura_barra))
    total = round(mem.total/(1024**3), 2)
    texto_bara = 'Uso total de memória (Total: {}GB)'.format(str(total))
    text = font.render(texto_bara, 1, branco)
    tela.blit(text, (margem_lateral, 10))






# loop para que a tela fique ativa
terminou = False
while not terminou:
    # Eventos de mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    #chama a função
    if cont == 60:
        mostra_uso_memoria()
        cont = 0

    pygame.display.update()
    clock.tick(60)

pygame.display.quit()


