import pyotp
import time

# 🔑 Ambos (cliente y servidor) comparten esta clave secreta
SECRET_KEY = "JBSWY3DPEHPK3PXP"

# Cliente y servidor usan la misma clave para generar el TOTP
cliente_totp = pyotp.TOTP(SECRET_KEY)
servidor_totp = pyotp.TOTP(SECRET_KEY)

print("🔐 Simulación Cliente-Servidor con TOTP")
print(f"Clave secreta compartida: {SECRET_KEY}\n")

try:
    while True:
        # Cliente genera el código actual
        codigo_cliente = cliente_totp.now()

        # Servidor genera su propio código para la misma ventana de tiempo
        codigo_servidor = servidor_totp.now()

        # Verificación (el servidor comprobaría esto)
        if codigo_cliente == codigo_servidor:
            estado = "✅ Coinciden (Acceso permitido)"
        else:
            estado = "❌ No coinciden (Acceso denegado)"

        print(
            f"\rCliente: {codigo_cliente} | Servidor: {codigo_servidor} | {estado}",
            end=""
        )

        time.sleep(1)

except KeyboardInterrupt:
    print("\n⏹️ Simulación detenida por el usuario.")
