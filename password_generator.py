import secrets
import string

def generar_password(longitud=12, mayus=True, minus=True, numeros=True, simbolos=True):
    caracteres = ""
    if mayus:
        caracteres += string.ascii_uppercase
    if minus:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += "!@#$%^&*()-_=+[]{};:,.<>?"

    if not caracteres:
        raise ValueError("Debes elegir al menos un tipo de caracter")

    # Generar la contraseña
    password = "".join(secrets.choice(caracteres) for _ in range(longitud))
    return password

if __name__ == "__main__":
    print("🔐 Generador de contraseñas seguras 🔐\n")
    longitud = int(input("¿Cuántos caracteres quieres? (Ej. 16): ") or 16)
    cantidad = int(input("¿Cuántas contraseñas generar? (Ej. 5): ") or 5)

    print("\nAquí tienes tus contraseñas seguras:\n")
    for i in range(cantidad):
        print(f"{i+1}: {generar_password(longitud)}")
