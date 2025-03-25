#finais: Perdido, sala do tesouro e Dragão jantou
def divisao():
  print("="*80)

def gameover_me_perdi():
  print("""Game Over: Me perdi
  
  Apenas queria que minha mãe estivesse aqui ;-;""")

def gameover_armadilha_fatal():
  print("""Game Over: Armadilha Fatal

Ao tentar avançar com cautela, você pisa em uma pedra que aciona uma armadilha. 
Fios cortantes se estendem do teto, acertando você com precisão mortal. O som de 
lâminas raspando ecoa enquanto você cai, incapaz de escapar a tempo. Em um 
instante, o que restou de você é apenas uma sombra na masmorra.""")
  
def win():
  print("""Você finalmente encontra o tesouro, enterrado sob pilhas de ossos e 
  poeira antiga. O baú, coberto de runas brilhantes, emite um brilho suave que 
  ilumina sua face. Ao abrir a tampa, uma luz radiante irrompe, revelando pilhas
   de ouro, pedras preciosas e artefatos antigos. No centro, o "Coração de 
   Aether", a joia mítica, brilha com um poder pulsante. Você sente a carga de 
   sua conquista, mas também a pesada responsabilidade de possuir tal poder. O 
   destino do reino agora está em suas mãos.""")
  
def gameover_obsessão_fatal():
  print("""Game Over: Obsessão Fatal

Você não consegue desviar o olhar das sombras que se movem nas passagens. A 
curiosidade te consome, e quanto mais você observa, mais percebe que os próprios 
olhos da escuridão começam a refletir de volta. De repente, uma presença se 
aproxima sem aviso, e a escuridão te engole por completo. O último som que você 
ouve é o suspiro abafado da própria luz desaparecendo.""")

def gameover_o_louco():
  print("""Game Over: O louco
  
Você acha que seria uma otima ideia  bater com a cabeça na parede para ver se 
funcionaria, mas isso não é as backroons""")

def gameover_dragon():
  print("""Game Over: A Fúria do Dragão

Ao virar a esquina, você finalmente encontra o dragão. Seus olhos brilham como 
carvão em chamas, e um rugido ensurdecedor ecoa pela masmorra. Antes que possa 
reagir, o monstro desfere um golpe devastador com sua cauda, lançando você 
contra a parede. O calor do fogo preenche o ar e, em um instante, você é 
consumido pelas chamas, tornando-se mais uma vítima da besta.""")
  
def escolher():
  global escolha 
  escolha = int(input("""[0] - Ficar olhando
[1] - Ir para a primeira passagem, a esquerda
[2] - Ir para a segunda passagem, a frente
[3] - Ir para a terceira passagem, a direita
[4] - Olhar o mapa
"""))
  
def mapa():
  print("Norte, onde o sol nasce e onde fica o [rasuras] corpo")

print(""" Em um pequeno vilarejo à beira de um vasto reino, uma antiga masmorra 
foi redescoberta após séculos de esquecimento. A lenda diz que no fundo dela 
repousa o "Coração de Aether", uma joia mágica capaz de curar qualquer doença. 
A filha do rei caiu gravemente doente, e nenhum remédio ou feitiço parece 
funcionar. Desesperado, o monarca oferece uma generosa recompensa para quem 
trouxer a joia, mas o caminho até ela é traiçoeiro, cheio de monstros e 
armadilhas mortais. Você, um aventureiro experiente, é sua última esperança.""")
divisao()
print(""" A escuridão engole a luz da tocha, tornando impossível ver o que está à
frente. O ar é denso, e algo parece se mover nas sombras. O silêncio é 
opressor, com o peso do frio tornando a respiração mais difícil. Inscrições 
antigas nas paredes se distorcem, mas a visão é limitada. Sons distantes de 
correntes e água ecoam, intensificando a sensação de que algo o observa na 
penumbra.""")
divisao()
print("Há 3 passagens escuras a frente qual você escolherá?")

escolher()
if escolha == 0:
  gameover_obsessão_fatal()
elif escolha == 1:
  gameover_dragon()
elif escolha == 2:
  print("Enconta mais 3 caminhos")
  escolher()
  if escolha == 0:
    gameover_obsessão_fatal()
  elif escolha == 1:
    gameover_armadilha_fatal()
  elif escolha == 2:
    gameover_dragon()
  elif escolha == 3:
    print("Enconta mais 3 caminhos")
    escolher()
    if escolha == 0:
      gameover_obsessão_fatal()
    elif escolha == 1:
      win()
    elif escolha == 2:
      gameover_dragon()
    elif escolha == 3:
      gameover_armadilha_fatal()
    elif escolha == 4:
      mapa()
    else:
      gameover_o_louco()
  elif escolha == 4:
    mapa()
  else:
    gameover_o_louco()
elif escolha == 3:
  for i in range(0,6):
    print("Enconta mais 3 caminhos")
    escolher()
  gameover_me_perdi()
elif escolha == 4:
  mapa()
else:
  gameover_o_louco()
