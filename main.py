from random import randint
from time import sleep

player = {}
inimigos = {
      "Aranha": 10,
      "Escorpião": 50,
      "Urso": 100,
      "Dragão verde": 200,
      "Dragão preto": 1000
}

def criar_personagem():
        nome = input("Digite o nome do seu personagem: \n")
        print(f"\nO guerreiro {nome} acaba de chegar no feudo Bravs e recebe uma missão direta do senhor Feudal de eliminar as criaturas que atrapalham o cotidiano de lá. Conforme seu personagem fica mais forte, ele pode evoluir a combater inimigos mais fortes.")
        print("Você pode escolher monstros para lutar, estudar para ganhar QI (que incrementa como bônus em seu ataque), ver a loja ou ver seu personagem.\n")
        player['nome'] = nome
        player['level'] = 1
        player['hitpoints'] = 10
        player['xp'] = 0
        player['qi'] = 0
        player['armour'] = 'Nenhuma'
        player['defense_boost'] = 0
        player['sword'] = 'Nenhuma'
        player['attack_boost'] = 0
        player['coins'] = 0

def avancar_level():
      player['level'] += 1

def estudar():
      while True:
            numero1 = randint(0, 20)
            numero2 = randint(0, 20)
            soma = numero1 + numero2

            soma_user = int(input(f"Qual a soma de {numero1} + {numero2}? \n"))
            if soma_user == soma:
                  player['qi'] += soma
                  print(f"Você ganhou {soma} pontos de QI. Total QI: {player['qi']}")
                  break
            else:
                  print("Resposta errada.")
                  break
            
      resposta = int(input("Você quer jogar novamente? [1] Sim, [2] Não: "))
      if resposta == 1:
            estudar()            
            
def loja():
      item_comprado = int(input(f"Qual item da loja você deseja comprar? [1] Armadura de ferro $250, [2] Armadura de ouro $1000, [3] Armadura de diamante $2500, [4] Espada de ferro $250, [5] Espada de ouro $1000, [6] Espada de diamante $2500, [7] Armadura e Espada de Meteoro $25000, [8] Sair da loja\n"))
      if item_comprado == 1:
            if player['coins'] >= 250:
                  player['coins'] -= 250
                  player['armour'] = 'Armadura de ferro'
                  player['defense_boost'] = 100
                  print(f"\nVocê comprou {player['armour']}!\n")
            else:
                  print("Dinheiro insuficiente!")
      elif item_comprado == 2:
            if player['coins'] >= 1000:
                  player['armour'] = 'Armadura de ouro'
                  player['defense_boost'] = 500
                  player['coins'] -= 1000
                  print(f"\nVocê comprou {player['armour']}!\n")
            else:
                  print("Dinheiro insuficiente!")
      elif item_comprado == 3:
            if player['coins'] >= 2500:
                  player['armour'] = 'Armadura de diamante'
                  player['defense_boost'] = 1000
                  player['coins'] -= 2500
                  print(f"\nVocê comprou {player['armour']}!\n")
            else:
                  print("Dinheiro insuficiente!")

      if item_comprado == 4:
            if player['coins'] >= 250:
                  player['coins'] -= 250
                  player['sword'] = 'Espada de ferro'
                  player['attack_boost'] = 100
            else:
                  print("Dinheiro insuficiente!")
      elif item_comprado == 5:
            if player['coins'] >= 1000:
                  player['sword'] = 'Espada de ouro'
                  player['attack_boost'] = 500
                  player['coins'] -= 1000
                  print(f"\nVocê comprou {player['sword']}!\n")
            else:
                  print("Dinheiro insuficiente!")
      elif item_comprado == 6:
            if player['coins'] >= 2500:
                  player['sword'] = 'Espada de diamante'
                  player['attack_boost'] = 1000
                  player['coins'] -= 2500
                  print(f"\nVocê comprou {player['sword']}!\n")
            else:
                  print("Dinheiro insuficiente!")
      elif item_comprado == 7:
            if player['coins'] >= 25000:
                  player['sword'] = 'Espada de meteoro'
                  player['attack_boost'] = 5000
                  player['armour'] = 'Armadura de meteoro'
                  player['defense_boost'] = 5000
                  player['coins'] -= 25000
                  print(f"\nVocê comprou {player['sword']}!\n")
                  print(f"\nVocê comprou {player['armour']}!\n")
            else:
                  print("Dinheiro insuficiente!")
      elif item_comprado == 8:
            print("\nSaindo da loja.\n")
      else:
              print("Digite uma resposta válida.")
              loja()

monstro_quest = 'Nenhum'

def quest():
      global monstro_quest
      global quantidade_monstros
      global recompensa
      quantidade_monstros = randint(1, 50)
      
      if player['level'] <= 10:
            numero_monstros = 1
            quantidade_monstros = randint(1, 20)
            recompensa = 500
      elif player['level'] <= 20:
            numero_monstros = randint(1, 2)
            quantidade_monstros = randint(1, 30)
            recompensa = 1000
      elif player['level'] <= 30:
            numero_monstros = randint(1, 3)
            quantidade_monstros = randint(1, 40)
            recompensa = 5000
      elif player['level'] >= 50:
            numero_monstros = randint(1, 5)
            quantidade_monstros = randint(1, 40)
            recompensa = 25000
      
      if numero_monstros == 1:
            monstro_quest = 'Aranha'
      elif numero_monstros == 2:
            monstro_quest = 'Escorpião'
      elif numero_monstros == 3:
            monstro_quest = 'Urso'
      elif numero_monstros == 4:
            monstro_quest = 'Dragão verde'
      elif numero_monstros == 5:
            monstro_quest = 'Dragão preto'

      print(f"\nSua quest é matar {quantidade_monstros} {monstro_quest}!\n")

quantidade_kills = 0

def combate(monstro):
      global monstro_quest
      global quantidade_kills
      global recompensa

      print(f"Você está lutando com {monstro}!")
      hp_player = player['hitpoints'] * player['level']
      hp_monstro = inimigos[monstro]
      while True:
            print("\nAtacando...")
            sleep(1)
            dano = randint(1, int(player['hitpoints'] + (player['attack_boost'] + player['qi']) / 10))
            player['xp'] += dano
            hp_monstro -= dano
            print(f"Você deu um dano de {dano}")
            print(f"Você ganhou {dano} XP! Total XP: {player['xp']}")
            if player['xp'] >= (player['level'] * 10):
                avancar_level()
                print(f"\nParabéns! Você atingiu o level {player['level']}!")
            if hp_monstro <= 0:
                  print(f"Parabéns! Você matou o monstro {monstro}!")
                  if monstro == monstro_quest:
                        quantidade_kills += 1
                        print(f"Você matou {quantidade_kills} {monstro}! Faltam {quantidade_monstros - quantidade_kills}")
                        if quantidade_kills == quantidade_monstros:
                              print(f"Você concluiu a quest e ganhou {recompensa} moedas de recompensa!")
                              player['coins'] += recompensa

                              monstro_quest = "Nenhuma quest"

                  if monstro == 'Aranha':
                        moedas_ganhas = randint(25, 250)
                        player['coins'] += moedas_ganhas
                  elif monstro == 'Escorpião':
                        moedas_ganhas = randint(250, 1000)
                        player['coins'] += moedas_ganhas
                  elif monstro == 'Urso':
                        moedas_ganhas = randint(1000, 2500)
                        player['coins'] += moedas_ganhas
                  elif monstro == 'Dragão verde':
                        moedas_ganhas = randint(2500, 10000)
                        player['coins'] += moedas_ganhas
                  elif monstro == 'Dragão preto':
                        moedas_ganhas = randint(10000, 25000)
                        player['coins'] += moedas_ganhas

                  print(f"Você ganhou {moedas_ganhas} moedas. Total de moedas: {player['coins']}")
                  break

            sleep(1)

            print("\nDefendendo...")
            sleep(1)
            dano = randint(0, int((inimigos[monstro] / 2 - player['defense_boost'] / 10)))
            hp_player -= dano
            print(f"Você sofreu um dano de {dano}! Total de vida: {hp_player}")

            if hp_player <= 0:
                  print("Você morreu! Tente novamente!")
                  break

            sleep(3)



def resposta_combate():
      while True:      
        resposta_combate = int(input("\nCom qual animal você deseja lutar? [1] Aranha, [2] Escorpião, [3] Urso, [4] Dragão verde, [5] Dragão preto\n"))
        if resposta_combate == 1:
              combate('Aranha')
              break
        elif resposta_combate == 2:
              combate('Escorpião')
              break
        elif resposta_combate == 3:
              combate('Urso')
              break
        elif resposta_combate == 4:
              combate('Dragão verde')
              break
        elif resposta_combate == 5:
              combate('Dragão preto')
              break
        else:
              print("Digite uma resposta válida.")
              resposta_combate()
      
def ver_personagem():
      print(f"\nNome: {player['nome']}")
      print(f"Level: {player['level']}")
      print(f"Hitpoints: {player['hitpoints']}")
      print(f"XP: {player['xp']}")
      print(f"QI: {player['qi']}")
      print(f"Hitpoints: {player['hitpoints']}")
      print(f"Moedas: {player['coins']}")
      print(f"Espada: {player['sword']}")
      print(f"Armadura: {player['armour']}")
      print(f"Boost de ataque: {player['attack_boost']}")
      print(f"Boost de defesa: {player['defense_boost']}")

def opcoes():
      opcao = int(input("\nO que você deseja fazer? [1] Combate, [2] Estudar, [3] Loja, [4] Ver personagem, [5] Quests\n"))
      
      if opcao == 1:
            resposta_combate()
      elif opcao == 2:
            estudar()
      elif opcao == 3:
            loja()
      elif opcao == 4:
            ver_personagem()
      elif opcao == 5:
            quest()
                      

def jogar(): 
    print(r"""
    x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
        _____   ____  _____ ______      ____  __ __   ____  ___    __ __    ___  ____   ______  __ __  ____     ___ 
    |     | /    |/ ___/|      |    |    \|  |  | /    ||   \  |  |  |  /  _]|    \ |      ||  |  ||    \   /  _]
    |   __||  o  (   \_ |      |    |  o  )  |  ||  o  ||    \ |  |  | /  [_ |  _  ||      ||  |  ||  D  ) /  [_ 
    |  |_  |     |\__  ||_|  |_|    |   _/|  ~  ||     ||  D  ||  |  ||    _]|  |  ||_|  |_||  |  ||    / |    _]
    |   _] |  _  |/  \ |  |  |      |  |  |___, ||  _  ||     ||  :  ||   [_ |  |  |  |  |  |  :  ||    \ |   [_ 
    |  |   |  |  |\    |  |  |      |  |  |     ||  |  ||     | \   / |     ||  |  |  |  |  |     ||  .  \|     |
    |__|   |__|__| \___|  |__|      |__|  |____/ |__|__||_____|  \_/  |_____||__|__|  |__|   \__,_||__|\_||_____|

    x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
    """)

    print("Bem-vindo a Fast PYAdventure. Esse é um jogo estilo RPG em terminal.\n")
    criar_personagem()
    while True:
      opcoes()

jogar()