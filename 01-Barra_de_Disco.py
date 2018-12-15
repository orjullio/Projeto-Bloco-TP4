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
pygame.display.set_caption("Uso de Disco")
cont = 60

pygame.display.init()
pygame.font.init()

clock = pygame.time.Clock()
font = pygame.font.Font(None, 32)

def mostra_uso_disco():
    disco = psutil.disk_usage('.')
    larg = largura_tela - 2*margem_lateral
    tela.fill(branco)
    pygame.draw.rect(tela, azul, (margem_lateral, margem_altura, larg, altura_barra))
    larg = larg*disco.percent/100
    pygame.draw.rect(tela, vermelho, (margem_lateral, margem_altura, larg, altura_barra))
    total = round(disco.total/(1024**3),2)
    texto_barra = 'Uso de disco: (Total: {}GB)'.format(str(total))
    text = font.render(texto_barra, 1, preto)
    tela.blit(text, (margem_lateral, 10))




terminou = False
while not terminou:
    # Eventos de mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    #chama a função
    if cont == 60:
        mostra_uso_disco()
        cont = 0

    pygame.display.update()
    clock.tick(60)

pygame.display.quit()