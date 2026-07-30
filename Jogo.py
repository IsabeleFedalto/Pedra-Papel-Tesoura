import random
from colorama import Fore, Back, Style
print("="*35)
print(Fore.LIGHTCYAN_EX + "PEDRA PAPEL E TESOURA".center(35) + Style.RESET_ALL)
print("="*35)
for numero in range():
    escolha_jogador = int(input("""Escolha entre:
    [1] 🪨Pedra
    [2] 📄Papel
    [3] ✂️Tesoura
    """))
    op = ["Pedra", "Papel", "Tesoura"]
    escolha_pc = random.choice(op)
    if escolha_pc == escolha_jogador:
        print("Empate entre os jogadores")