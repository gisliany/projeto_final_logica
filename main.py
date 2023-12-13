# Questão 2, importações


#  Questão 3, inicializações
janela = 

carro = 
carro2 = 
carro_loc = 
carro2_loc = 

contador = 
velocidade = 

esta_executando = True

# loop de jogo
while esta_executando:

  # Questão 5, item 2
  

  # esse trecho verifica se houve eventos de entrada (mouse, teclado)
  for event in pygame.event.get():
    if event.type == QUIT:
      esta_executando = False

    # Questão 6
    # if event.type == KEYDOWN:
    #   if event.key == K_a or event.key == K_LEFT:


  # redesenha elementos na janela
  visual.desenhar_estrada(janela)
  # Questão 4
  visual.desenhar_carros(janela)
  visual.atualizar_tela()
  
  # Questão 7, item 2
  
  
  # Questão 8, itens 2 e 3


# Questão 9
