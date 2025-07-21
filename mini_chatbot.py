import json
import os
import random

ARCHIVO_RESPUESTAS = "respuestas.json"

def cargar_respuestas():
    if os.path.exists(ARCHIVO_RESPUESTAS):
        with open(ARCHIVO_RESPUESTAS, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        # Respuestas base (ya con listas para que pueda aleatorizar)
        return {
            "hola": ["¡Hola! ¿Cómo estás?", "¡Hey! Qué gusto verte.", "Hola, ¿todo bien?"],
            "como estas": ["Estoy bien, gracias por preguntar.", "Todo tranquilo, ¿y tú?", "Mejorando cada día 😄"],
            "tu nombre": ["Me llamo MiniBot.", "Puedes llamarme MiniBot.", "Soy MiniBot, tu asistente personal."],
            "adios": ["Adiós, vuelve pronto.", "¡Cuídate mucho!", "Nos vemos pronto 👋"]
        }

def guardar_respuestas(respuestas):
    with open(ARCHIVO_RESPUESTAS, "w", encoding="utf-8") as f:
        json.dump(respuestas, f, ensure_ascii=False, indent=4)

def obtener_respuesta(respuesta):
    """Devuelve una respuesta, aleatoria si es lista."""
    if isinstance(respuesta, list):
        return random.choice(respuesta)
    return respuesta  # Si es texto simple, lo devuelve tal cual

def mini_chatbot():
    print("🤖 Hola, soy MiniBot con MEMORIA. Escribe 'salir' para terminar.")
    print("📚 Puedes enseñarme nuevas respuestas usando: aprende [palabra] -> [respuesta]\n")

    # Cargar respuestas guardadas
    respuestas = cargar_respuestas()

    while True:
        mensaje = input("Tú: ").strip().lower()

        # Salir del chat
        if mensaje == "salir":
            print("🤖 Adiós, ¡que tengas buen día!")
            break

        # Enseñar nuevas respuestas
        if mensaje.startswith("aprende "):
            try:
                # separar palabra y respuesta
                _, resto = mensaje.split("aprende ", 1)
                clave, respuesta = resto.split("->")
                clave = clave.strip()
                respuesta = respuesta.strip()

                # Si ya existe y es lista, agregar una nueva opción
                if clave in respuestas:
                    if isinstance(respuestas[clave], list):
                        respuestas[clave].append(respuesta)
                    else:
                        respuestas[clave] = [respuestas[clave], respuesta]
                else:
                    # Crear nueva clave como lista
                    respuestas[clave] = [respuesta]

                guardar_respuestas(respuestas)  # guardar en archivo
                print(f"🤖 He aprendido que '{clave}' también puede significar: '{respuesta}' (Guardado en memoria)")
            except:
                print("⚠️ Formato inválido. Usa: aprende palabra -> respuesta")
            continue

        # Buscar respuesta exacta
        if mensaje in respuestas:
            print("🤖", obtener_respuesta(respuestas[mensaje]))
        else:
            # Buscar coincidencia parcial
            encontrado = False
            for clave, respuesta in respuestas.items():
                if clave in mensaje:  # si la clave está dentro del mensaje
                    print("🤖", obtener_respuesta(respuesta))
                    encontrado = True
                    break

            if not encontrado:
                print("🤖 No estoy seguro de eso, pero puedes enseñarme usando: aprende [palabra] -> [respuesta]")

if __name__ == "__main__":
    mini_chatbot()
