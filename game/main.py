import random
print("Bienvenido a Piedra, Papel o Tijera")

pc_wins = 0
user_wins = 0
rounds = 1

while True:
  print('*' * 15)
  print('ROUND', rounds, "🥊")
  print('*' * 15)

  print('Victorias del usuario =>', user_wins)
  print('Victorias del computador =>', pc_wins)

  print('*' * 10)

  options = ('piedra', 'papel', 'tijera')

  user_option = input('Elige tu ataque => ')
  user_option = user_option.lower()
  computer_option = random.choice(options)

  if not (user_option in options):
    print('Esa opción no es válida...')
    continue

  print('Tu elegiste => ', user_option)
  print('La computadora eligió => ', computer_option)

  if user_option == computer_option:
    print('Empate')
  elif user_option == 'piedra':
    if computer_option == 'papel':
      print('perdiste...')
      print('*' * 10)
      pc_wins += 1
    else:
      print('Ganaste!')
      print('*' * 10)
      user_wins += 1
  elif user_option == 'papel':
    if computer_option == 'tijera':
      print('perdiste...')
      print('*' * 10)
      pc_wins += 1
    else:
      print('Ganaste!')
      print('*' * 10)
      user_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'piedra':
      print('perdiste...')
      print('*' * 10)
      pc_wins += 1
    else:
      print('Ganaste!')
      print('*' * 10)
      user_wins += 1

  if pc_wins == 3:
    print('La computadora gano con', pc_wins)
    print("Has jugado contra tu oponente", rounds, "rondas")
    break
  if user_wins == 3:
    print('El usuario gana con', user_wins)
    print("Has jugado contra tu oponente", rounds, "rondas")
    break

  rounds += 1
