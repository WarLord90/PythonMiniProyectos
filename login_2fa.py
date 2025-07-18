import pyotp
import time

# 🔑 Clave secreta compartida entre cliente y servidor
SECRET_KEY = "JBSWY3DPEHPK3PXP"
totp = pyotp.TOTP(SECRET_KEY)

# Usuario y contraseña simulados
USUARIO = "javier"
PASSWORD = "12345678"

def mostrar_codigo_con_tiempo():
    """
    Muestra el código actual y cuántos segundos le quedan antes de expirar
    """
    codigo = totp.now()
    segundos_bloque = int(time.time()) % 30  # En qué segundo del bloque estamos
    tiempo_restante = 30 - segundos_bloque

    print(f"\n[Authenticator] Código actual: {codigo} (expira en {tiempo_restante}s)\n")
    return codigo

def login():
    print("🔐 Sistema con 2FA (Autenticación en Dos Factores)\n")

    usuario = input("Usuario: ")
    password = input("Contraseña: ")

    # Validar usuario y contraseña
    if usuario != USUARIO or password != PASSWORD:
        print("❌ Usuario o contraseña incorrectos.")
        return

    # Contraseña correcta → pedimos 2FA
    print("\n✅ Contraseña correcta.")
    print("Abre tu Authenticator...")

    # Mostramos el código como si fuera tu app
    mostrar_codigo_con_tiempo()

    # Usuario ingresa el código manualmente
    codigo_ingresado = input("Ingresa el código de 6 dígitos: ")

    # Servidor valida
    if totp.verify(codigo_ingresado):
        print("✅ Código correcto. Acceso permitido.")
    else:
        print("❌ Código inválido o expirado.")

if __name__ == "__main__":
    try:
        login()
    except KeyboardInterrupt:
        print("\n⏹️ Proceso detenido por el usuario.")
