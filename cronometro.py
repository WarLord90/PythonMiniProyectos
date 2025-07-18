import time

def cronometro():
    print("⏱️ Cronómetro iniciado. Presiona CTRL+C para detener.\n")
    segundos = 0
    try:
        while True:
            horas = segundos // 3600
            minutos = (segundos % 3600) // 60
            seg = segundos % 60

            print(f"\r⏳ {horas:02}:{minutos:02}:{seg:02}", end="")
            time.sleep(1)
            segundos += 1
    except KeyboardInterrupt:
        print("\n⏹️ Cronómetro detenido.")

if __name__ == "__main__":
    cronometro()
