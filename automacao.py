import time

# Simulação de estado da carga (ligada ou desligada)
estado_carga = False


def ligar_carga():
    global estado_carga
    if not estado_carga:
        estado_carga = True
        print("Carga ligada.")
    else:
        print("Carga já está ligada.")


def desligar_carga():
    global estado_carga
    if estado_carga:
        estado_carga = False
        print("Carga desligada.")
    else:
        print("Carga já está desligada.")


def simular_acionamento_remoto():
    print("Iniciando simulação de acionamento remoto...")
    time.sleep(1)

    ligar_carga()
    time.sleep(2)  # Simula carga ligada por 2 segundos

    desligar_carga()
    time.sleep(2)  # Simula carga desligada por 2 segundos

    ligar_carga()
    time.sleep(2)

    desligar_carga()
    print("Simulação finalizada.")


if __name__ == "__main__":
    simular_acionamento_remoto()
