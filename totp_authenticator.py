import pyotp
import time
import datetime

# 🔑 Usamos una clave fija para que siempre sea la misma
SECRET_KEY = "JBSWY3DPEHPK3PXP"
totp = pyotp.TOTP(SECRET_KEY)

print("🔐 Simulación Authenticator con zona horaria")
print(f"Clave secreta: {SECRET_KEY}\n")

try:
    while True:
        # Código actual
        codigo = totp.now()

        # Epoch time (segundos desde 1970 UTC)
        epoch_time = int(time.time())

        # Hora local y UTC para comparar
        hora_local = datetime.datetime.now()
        hora_utc = datetime.datetime.utcnow()

        print(
            f"\rCódigo: {codigo} | "
            f"Epoch: {epoch_time} | "
            f"Local: {hora_local.strftime('%H:%M:%S')} | "
            f"UTC: {hora_utc.strftime('%H:%M:%S')}",
            end=""
        )

        time.sleep(1)

except KeyboardInterrupt:
    print("\n⏹️ Simulación detenida por el usuario.")
