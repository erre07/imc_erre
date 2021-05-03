import time
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'


def logo():
    print(RED + "██████╗")
    print(RED + "██╔══██╗")
    print(RED + "██████╔╝")
    print(RED + "██╔══██╗")
    print(RED + "██║  ██║")
    print(RED + "╚═╝  ╚═╝")
    time.sleep(2.5)


def imc_por_erre():
    op = input(BLUE + f"Ingresa [1] para iniciar la calculadora y [2] para salir del programa.\n{RESET}--> ")
    while op == "1":
        if op == "2":
            break
        altura = float(input(f"\n{MAGENTA}Ingresa tu {CYAN}altura{RESET} {MAGENTA}en metros:{RESET} "))
        peso = float(input(f"{MAGENTA}Ingresa tu {CYAN}peso{RESET} {MAGENTA}en kg:{RESET} {RESET}"))
        altura_definida = altura * altura
        resultado = peso / altura_definida
        resultado = float(format(resultado, '.2f'))
        if resultado <= 18:
            print(f"\nSu IMC es {YELLOW}{resultado}{RESET} lo que indica que su peso está "
                  f"en la categoría de {YELLOW}BAJO PESO{RESET} para adultos de su misma estatura.")
            input(f"\nPresiona {RED}ENTER{RESET} para salir de la calculadora")
            break

        elif resultado <= 18.5 and resultado <= 24.9:
            print(f"\nSu IMC es {YELLOW}{resultado}{RESET} lo que indica que su peso está"
                  f" en la categoría {YELLOW}NORMAL{RESET} para adultos de su misma estatura")
            input(f"\nPresiona {RED}ENTER{RESET} para salir de la calculadora")
            break
        elif 25 < resultado <= 29.9:
            print(f"\nSu IMC es {YELLOW}{resultado}{RESET}, lo que indica que su peso está"
                  f" en la categoría de {YELLOW}SOBREPESO{RESET} para adultos de su misma estatura.")
            input(f"\nPresiona {RED}ENTER{RESET} para salir de la calculadora")
            break

        elif 30 <= resultado:
            print(f"\nSu IMC es {YELLOW}{resultado}{RESET}, lo que indica que su peso está"
                  f"en la categoría de {YELLOW}OBESO{RESET} para adultos de su misma estatura.")
            input(f"\nPresiona {RED}ENTER{RESET} para salir de la calculadora")
            break
        else:
            print(f"{RED}Hubo un error y el programa no devolvio ningun resultado.{RESET}"
                  f"{RED}Prueba con unos valores mas redondeado.{RESET}")
    print("Muchas gracias por usar este programa basico! "
          f"{RED}Visitenme en Instagram: @erre.py{RESET}")


logo()
print("\nSean bienvenidos a el calculador de indice de masa corporal realizado por ERRE")
print("\nLos valores deben ser ingresados en este formato (peso = 55.70) (altura = 1.7)")
print(RESET)
time.sleep(2.5)
imc_por_erre()
