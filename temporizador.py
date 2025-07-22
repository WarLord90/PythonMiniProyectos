import time
import platform
import os

if platform.system() == "Windows":
    import winsound

def sonar():
    sistema = platform.system()

    if sistema == "Windows":
        winsound.Beep(1000, 500)
    elif sistema in ["Linux", "Darwin"]:  # Darwin = macOS
        print("\a", end="", flush=True)  # beep clásico
        os.system('echo -e "\a"')
    else:
        print("🔇 No se pudo reproducir sonido en este sistema.")

def temporizador():
    print("⏳ Temporizador multiplataforma")

    # Pedimos el tiempo en segundos
    tiempo = int(input("¿Cuántos segundos quieres contar? "))

    for restante in range(tiempo, 0, -1):
        min_actual = restante // 60
        seg_actual = restante % 60
        print(f"\r⏳ Tiempo restante: {min_actual:02d}:{seg_actual:02d}", end="")
        time.sleep(1)

    print("\n⏰ ¡Tiempo terminado!")

    # Beeps finales
    for _ in range(3):
        sonar()
        time.sleep(0.3)

if __name__ == "__main__":
    temporizador()
