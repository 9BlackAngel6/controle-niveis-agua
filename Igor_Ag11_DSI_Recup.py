
from colorama import Fore, Style, init

# Inicializa a biblioteca Colorama
init(autoreset=False)

# Lista com os níveis e suas respectivas situações
niveis_agua = [
    {"nivel": 1, "situacao": "Muito baixo - CRITICO"},
    {"nivel": 2, "situacao": "Baixo"},
    {"nivel": 3, "situacao": "Medio"},
    {"nivel": 4, "situacao": "Alto"},
    {"nivel": 5, "situacao": "Muito alto - ALERTA"}
]


# Funcao responsavel por definir a cor de cada nivel
def definir_cor(nivel):

    cores = {
        1: Fore.RED,
        2: Fore.YELLOW,
        3: Fore.GREEN,
        4: Fore.CYAN,
        5: Fore.BLUE
    }

    if nivel not in cores:
        raise ValueError("Nivel de agua invalido!")

    return cores[nivel]


# Funcao responsavel por exibir a situacao do reservatorio
def monitorar_reservatorio():

    print("\n===== MONITORAMENTO DO RESERVATORIO =====\n")

    for item in niveis_agua:
        try:
            nivel = item["nivel"]
            situacao = item["situacao"]

            cor = definir_cor(nivel)

            print(
                cor + f"Nivel {nivel}: {situacao}"
                + Style.RESET_ALL
            )

        except ValueError as erro:
            print(Fore.RED + str(erro) + Style.RESET_ALL)

    print("\n===== MONITORAMENTO FINALIZADO =====")


# Executa a simulacao
monitorar_reservatorio()
