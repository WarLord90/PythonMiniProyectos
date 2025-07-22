import tkinter as tk
from tkinter import messagebox
import time
import threading
import platform
import os

# Para sonido multiplataforma
if platform.system() == "Windows":
    import winsound

def sonar():
    sistema = platform.system()
    if sistema == "Windows":
        winsound.Beep(1000, 500)
    elif sistema in ["Linux", "Darwin"]:
        print("\a", end="", flush=True)
        os.system('echo -e "\a"')

def iniciar_temporizador():
    try:
        segundos = int(entry_tiempo.get())
        if segundos <= 0:
            messagebox.showwarning("Error", "Por favor ingresa un número mayor a 0")
            return

        # Deshabilitar botón mientras cuenta
        btn_iniciar.config(state="disabled")

        def contar():
            nonlocal segundos
            while segundos > 0:
                min_actual = segundos // 60
                seg_actual = segundos % 60
                label_tiempo.config(text=f"{min_actual:02d}:{seg_actual:02d}")
                time.sleep(1)
                segundos -= 1

            # Cuando termina
            label_tiempo.config(text="00:00")
            messagebox.showinfo("¡Tiempo terminado!", "⏰ ¡El temporizador ha finalizado!")
            for _ in range(3):
                sonar()
                time.sleep(0.3)
            btn_iniciar.config(state="normal")

        # Usamos threading para no congelar la interfaz
        threading.Thread(target=contar, daemon=True).start()

    except ValueError:
        messagebox.showwarning("Error", "Por favor ingresa un número válido")

# Crear ventana
root = tk.Tk()
root.title("⏳ Temporizador GUI")

# Campo para ingresar segundos
tk.Label(root, text="Tiempo en segundos:").pack(pady=5)
entry_tiempo = tk.Entry(root, width=10)
entry_tiempo.pack(pady=5)

# Label para mostrar el contador
label_tiempo = tk.Label(root, text="00:00", font=("Helvetica", 40))
label_tiempo.pack(pady=10)

# Botón para iniciar
btn_iniciar = tk.Button(root, text="Iniciar", command=iniciar_temporizador)
btn_iniciar.pack(pady=10)

# Ejecutar la interfaz
root.mainloop()
