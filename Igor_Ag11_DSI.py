
from colorama import Fore, Style, init

# Inicializa o Colorama
init(autoreset=True)

# Lista com os níveis do reservatório
niveis = [
    "Nível 1 - Muito baixo (CRÍTICO)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (ALERTA)"
]

# Função que define a cor de cada nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Simulação do monitoramento
nivel_atual = 3

if 1 <= nivel_atual <= len(niveis):
    cor = definir_cor(nivel_atual)

    print(cor + "MONITORAMENTO DO RESERVATÓRIO")
    print(cor + niveis[nivel_atual - 1])
    print(Style.RESET_ALL)
else:
    print("Erro: nível do reservatório inválido.")
