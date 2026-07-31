import random
from colorama import Fore, Back, Style

def escolha_do_pc(escolha):
    print("Computador escolheu " + escolha)

def reset():
    print(Style.RESET_ALL, end="")

def ponto_do_pc():
    print(Fore.RED + "Ponto para o computador")
    reset()
def ponto_do_jogador():
    print(Fore.GREEN + "Ponto para o jogador")
    reset()
def placar(jogador, computador):
    print(f"Pontuação:\n Jogador: {jogador} | PC: {computador}")
print(Fore.LIGHTCYAN_EX + "="*38 + "\n\t\tPEDRA PAPEL E TESOURA\n" +"="*38)
reset()

rodadas = 0
pontos_jogador = 0
pontos_pc = 0

while rodadas <3:
    escolha_jogador = input("""Digite a sua escolha:
    🪨Pedra
    📄Papel
    ✂️Tesoura
    """).strip().capitalize()
    op = ["Pedra", "Papel", "Tesoura"]
    escolha_pc = random.choice(op)
    if escolha_jogador not in op:
        print(Fore.RED + "Opção inválida! Tente novamente.")
        reset()
        continue

    #Empate
    if escolha_pc == escolha_jogador:
        escolha_do_pc(escolha_pc)
        print(Fore.YELLOW + "Empate entre os jogadores")
        reset()
        print(f"Pontuação:\n Jogador: {pontos_jogador} | PC: {pontos_pc}")

    # Pc ganha
    if (escolha_pc == "Papel" and escolha_jogador == "Pedra") or \
            (escolha_pc == "Tesoura" and escolha_jogador == "Papel") or \
            (escolha_pc == "Pedra" and escolha_jogador == "Tesoura"):
        escolha_do_pc(escolha_pc)
        ponto_do_pc()
        pontos_pc += 1
        print(f"Pontuação:\n Jogador: {pontos_jogador} | PC: {pontos_pc}")
        rodadas += 1

    #Jogador ganha
    if (escolha_jogador == "Papel" and escolha_pc == "Pedra") or \
            (escolha_jogador == "Tesoura" and escolha_pc == "Papel") or \
            (escolha_jogador == "Pedra" and escolha_pc == "Tesoura"):
        escolha_do_pc(escolha_pc)
        ponto_do_jogador()
        pontos_jogador += 1
        placar(pontos_jogador, pontos_pc)
        rodadas += 1
    if pontos_jogador == 2:
        break
    elif pontos_pc == 2:
        break
if pontos_jogador < pontos_pc:
    print( Fore.RED + "💀O pc ganhou💀")
    reset()
else:
    print( Fore.GREEN + "⭐O jogador Ganhou, PARABENS!⭐")
    reset()
