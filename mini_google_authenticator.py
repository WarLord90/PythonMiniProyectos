import pyotp
import time

# 🔑 Clave secreta fija (como la que te da un servidor)
SECRET_KEY = "JBSWY3DPEHPK3PXP"
totp = pyotp.TOTP(SECRET_KEY)

print("🔐 Mini Google Authenticator en consola")
print(f"Clave secreta: {SECRET_KEY}\n")

try:
    while True:
        # Cada vez que empieza un nuevo bloque de 30s, generamos código nuevo
        codigo_actual = totp.now()
        print(f"\n[Authenticator] Nuevo código: {codigo_actual}")

        # Contador regresivo de 30 segundos
        for tiempo_restante in range(30, 0, -1):
            print(f"\r⏳ Expira en: {tiempo_restante:02d}s", end="")
            time.sleep(1)

except KeyboardInterrupt:
    print("\n⏹️ Authenticator detenido.")
