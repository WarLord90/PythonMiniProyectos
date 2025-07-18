import time
from password_generator import generar_password

def cronometro():
    print(f"⏱️ Cronómetro iniciado. Presiona CTRL+C para detener.\n")
    segundos = 0
    try:
        while True:
            horas = segundos // 3600
            minutos = (segundos % 3600) // 60
            seg = segundos % 60

            print(f"\r⏳ {horas:02}:{minutos:02}:{seg:02}", end="")
            time.sleep(1)
            if segundos % 30 == 0:
                print(f"\n🔐 {generar_password(12)}")

            segundos += 1
    except KeyboardInterrupt:
        print(f"\n⏹️ Cronómetro detenido.")

if __name__ == "__main__":
    cronometro()