import pygame, psutil

# Cores
azul = (0, 0, 255)
vermelho = (255, 0, 0)
branco = (255, 255, 255)

# Estrutura das telas
largura = 800
altura = 600
margem_lateral = 20
margem_altura = 50
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Exemplo Surface')
pygame.display.init()

s1 = pygame.surface.Surface((largura, altura/3))
s2 = pygame.surface.Surface((largura, altura/3))
s3 = pygame.surface.Surface((largura, altura/3))

pygame.draw.rect(s1, azul, (margem_lateral, margem_altura, largura - 2*margem_lateral, 70))
tela.blit(s1, (0,0))
pygame.draw.rect(s2, vermelho,(margem_lateral, margem_altura, largura - 2*margem_lateral, 70))
tela.blit(s2, (0, altura/3))
pygame.draw.rect(s3, branco, (margem_lateral, margem_altura, largura - 2 * margem_lateral, 70))
tela.blit(s3, (0, 2 * altura / 3))


clock = pygame.time.Clock()

terminou = False
while not terminou:
    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  terminou = True

    # Atualiza o desenho na tela
    pygame.display.update()
    # 60 frames por segundo
    clock.tick(60)

  # Finaliza a janela
pygame.display.quit()


