# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-03-14
# RLAB-23-02-09-0044-2
#

# Librerias
from sys import argv
from random import choice

# Variables
cachipun = ["piedra", "papel", "tijera"] # Lista

if str(argv[1]) in cachipun :
    player1 = str(argv[1])
    computer = choice(cachipun)
else :
    print("Argumento inválido: Debe ser piedra, papel o tijera.\n")
    exit()


# Resultados
if player1 == computer :
    print(f"Tú jugaste {player1}") 
    print(f"Computador jugó {computer}") 
    print("Empate!!")
elif player1 == "piedra" :
    if computer == "tijera" :
        print(f"Tú jugaste {player1}") 
        print(f"Computador jugó {computer}") 
        print("Ganaste!!")
    else :
        print(f"Tú jugaste {player1}") 
        print(f"Computador jugó {computer}") 
        print("Perdiste!!")
elif player1 == "papel" :
    if computer == "piedra" :
        print(f"Tú jugaste {player1}") 
        print(f"Computador jugó {computer}") 
        print("Ganaste!!")
    else :
        print(f"Tú jugaste {player1}") 
        print(f"Computador jugó {computer}") 
        print("Perdiste!!")
elif player1 == "tijera" :
    if computer == "papel" :
        print(f"Tú jugaste {player1}") 
        print(f"Computador jugó {computer}") 
        print("Ganaste!!")
    else :
        print(f"Tú jugaste {player1}") 
        print(f"Computador jugó {computer}") 
        print("Perdiste!!")