import pygame, random #Importando a nossa biblioteca pygame
from pygame.locals import *  #Importanto todas as funcionalidade do pygame

#############################Funções que usaremos ao decorrer do codigo########################################
def on_grid_random():   #Criando uma função para alianhar a maça com o personagem
    x = random.randint(0,59)
    y = random.randint(0,59)
    return (x * 10, y * 10)

def collision(c1, c2): #Criando a colisão
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

#Criando atalhos para definirmos as direções que nosso personagem esta indo na tela
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

#########################################################################################################

pygame.init() #Determina o inicio do nosso código
screen = pygame.display.set_mode((600, 600)) #Determina a nossa tela do jogo e suas dimensões em pixels
pygame.display.set_caption('Snake') #Nome da janela do nosso jogo

snake = [(200, 200), (210, 200), (220,200)] #Criando as posições e dimensões da nossa cobra/personagem na tela
snake_skin = pygame.Surface((10,10))    #Dimensões
snake_skin.fill((255,255,255)) #Definindo as cores do personagem

apple_pos = on_grid_random() #Definindo uma posição aleatoria para a maça
apple = pygame.Surface((10,10)) #Criando uma maçã para nosso personagem pontuar 
apple.fill((255,0,0))   #Definindo as cores dessa maçã

my_direction = LEFT

clock = pygame.time.Clock()  #Criamos uma função para limitar o fps do nosso jogo

font = pygame.font.Font('freesansbold.ttf', 18) #Criando o texto para o score
score = 0 #Definindo o score inicial

game_over = False
while not game_over: #Determinamos o laço infinito do nosso jogo
    clock.tick(10) #limitamos o fps para 10
    for event in pygame.event.get():    #eventos, interações do usuário com o jogo e ações que nosso algoritmo tem que fazer a partir disso
        if event.type == QUIT: #Fechar o nosso jogo
            pygame.quit()
            exit()

        if event.type == KEYDOWN:   #Definindo as ações que o personagem vai tomar quando pressionarmos a tecla
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT

    if collision(snake[0], apple_pos): #Definindo a personagem pontuando ao comer a maça
        apple_pos = on_grid_random()
        snake.append((0,0))
        score = score + 1
        
    # Checando se a personagem toca na borda
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break
    
    # Checando se a personagem toca ela mesma
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over: 
        break
    
    for i in range(len(snake) - 1, 0, -1): #Definimos a alteração de sentido para todo o corpo da nossa personagem
        snake[i] = (snake[i-1][0], snake[i-1][1])
        
    # Fazendo a personagem se mover
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    
    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    
    for x in range(0, 600, 10): # Desenhando as linhas horizontais do jogo
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10): # Desenhando as linhas verticais do jogo criando um grid
        pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))
    
    score_font = font.render('Score: %s' % (score), True, (255, 255, 255)) #Definindo o placar
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10) #Posição do placar
    screen.blit(score_font, score_rect)
    
    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update()

while True: #Definindo oque fazer quando o jogador perde
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
