import json
import os
import difflib  # para coincidencias aproximadas

ARCHIVO_RESPUESTAS = "respuestas.json"

def cargar_respuestas():
    if os.path.exists(ARCHIVO_RESPUESTAS):
        with open(ARCHIVO_RESPUESTAS, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {
            "hola": "¡Hola! ¿Cómo estás?",
            "como estas": "Estoy bien, gracias por preguntar.",
            "tu nombre": "Me llamo MiniBot.",
            "adios": "Adiós, vuelve pronto."
        }

def guardar_respuestas(respuestas):
    with open(ARCHIVO_RESPUESTAS, "w", encoding="utf-8") as f:
        json.dump(respuestas, f, ensure_ascii=False, indent=4)

def buscar_mejor_coincidencia(mensaje, respuestas):
    # Busca la palabra más parecida con difflib
    opciones = list(respuestas.keys())
    coincidencias = difflib.get_close_matches(mensaje, opciones, n=1, cutoff=0.6)
    return coincidencias[0] if coincidencias else None

def mini_chatbot():
    print("🤖 Hola, soy MiniBot más inteligente. Escribe 'salir' para terminar.")
    print("📚 Puedes enseñarme nuevas respuestas usando: aprende [palabra] -> [respuesta]\n")

    respuestas = cargar_respuestas()

    while True:
        mensaje = input("Tú: ").strip().lower()

        if mensaje == "salir":
            print("🤖 Adiós, ¡que tengas buen día!")
            break

        # Enseñar nuevas respuestas
        if mensaje.startswith("aprende "):
            try:
                _, resto = mensaje.split("aprende ", 1)
                clave, respuesta = resto.split("->")
                clave = clave.strip()
                respuesta = respuesta.strip()
                respuestas[clave] = respuesta
                guardar_respuestas(respuestas)
                print(f"🤖 He aprendido que '{clave}' significa: '{respuesta}' (Guardado en memoria)")
            except:
                print("⚠️ Formato inválido. Usa: aprende palabra -> respuesta")
            continue

        # Buscar coincidencia exacta o aproximada
        if mensaje in respuestas:
            print("🤖", respuestas[mensaje])
        else:
            coincidencia = buscar_mejor_coincidencia(mensaje, respuestas)
            if coincidencia:
                print("🤖", respuestas[coincidencia])
            else:
                print("🤖 No entiendo, pero puedes enseñarme usando: aprende [palabra] -> [respuesta]")

if __name__ == "__main__":
    mini_chatbot()
