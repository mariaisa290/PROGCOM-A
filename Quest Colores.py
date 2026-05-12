# Importar los módulos necesarios
import tkinter
import random

# Lista de colores posibles (nombres en español)
colores = ['Rojo', 'Azul', 'Verde', 'Rosa', 'Negro',
           'Amarillo', 'Naranja', 'Blanco', 'Morado', 'Café']

# Mapa de nombres en español al código de color para Tkinter
mapa_colores = {
    'Rojo': 'red',
    'Azul': 'blue',
    'Verde': 'green',
    'Rosa': 'pink',
    'Negro': 'black',
    'Amarillo': 'yellow',
    'Naranja': 'orange',
    'Blanco': 'white',
    'Morado': 'purple',
    'Café': 'brown'
}

puntaje = 0

# Tiempo de juego restante, inicialmente 30 segundos
tiempo_restante = 30

# Función que inicia el juego
def iniciar_juego(evento):
    global tiempo_restante

    if tiempo_restante == 30:
        # Iniciar el temporizador de cuenta regresiva
        cuenta_regresiva()

    # Ejecutar la función para elegir el siguiente color
    siguiente_color()

# Función para elegir y mostrar el siguiente color
def siguiente_color():
    global puntaje
    global tiempo_restante

    # Si hay tiempo restante en el juego
    if tiempo_restante > 0:

        # Activar el cuadro de entrada de texto
        entrada.focus_set()

        # Si el color escrito es igual al color del texto mostrado
        if entrada.get().lower() == colores[1].lower():
            puntaje += 1

        # Limpiar el cuadro de entrada de texto
        entrada.delete(0, tkinter.END)

        random.shuffle(colores)

        # Cambiar el color a escribir: cambia el texto Y el color del texto
        color_tkinter = mapa_colores[colores[1]]
        etiqueta_color.config(fg=color_tkinter, text=str(colores[0]))

        # Actualizar el puntaje
        etiqueta_puntaje.config(text="Puntaje: " + str(puntaje))

# Función de cuenta regresiva
def cuenta_regresiva():
    global tiempo_restante

    # Si hay tiempo en el juego
    if tiempo_restante > 0:

        # Decrementar el temporizador
        tiempo_restante -= 1

        # Actualizar la etiqueta de tiempo restante
        etiqueta_tiempo.config(text="Tiempo restante: " + str(tiempo_restante))

        # Volver a ejecutar la función después de 1 segundo
        etiqueta_tiempo.after(1000, cuenta_regresiva)

    else:
        # Mostrar mensaje de fin de juego
        etiqueta_color.config(text="¡Fin del juego!", fg="black")
        etiqueta_puntaje.config(text="Puntaje final: " + str(puntaje))

# --- Código principal ---

# Crear la ventana principal
raiz = tkinter.Tk()

# Establecer el título
raiz.title("JUEGO DE COLORES")

# Establecer el tamaño
raiz.geometry("400x220")

# Color de fondo
raiz.config(bg="#f0f0f0")

# Agregar etiqueta de instrucciones
instrucciones = tkinter.Label(
    raiz,
    text="¡Escribe el COLOR del texto, no lo que dice la palabra!",
    font=('Helvetica', 11),
    bg="#f0f0f0",
    wraplength=380
)
instrucciones.pack()

# Agregar etiqueta de puntaje
etiqueta_puntaje = tkinter.Label(
    raiz,
    text="Presiona Enter para comenzar",
    font=('Helvetica', 12),
    bg="#f0f0f0"
)
etiqueta_puntaje.pack()

# Agregar etiqueta de tiempo restante
etiqueta_tiempo = tkinter.Label(
    raiz,
    text="Tiempo restante: " + str(tiempo_restante),
    font=('Helvetica', 12),
    bg="#f0f0f0"
)
etiqueta_tiempo.pack()

# Agregar etiqueta para mostrar los colores
etiqueta_color = tkinter.Label(raiz, font=('Helvetica', 50), bg="#f0f0f0")
etiqueta_color.pack()

# Agregar cuadro de entrada de texto
entrada = tkinter.Entry(raiz, font=('Helvetica', 13))

# Ejecutar la función 'iniciar_juego' cuando se presione Enter
raiz.bind('<Return>', iniciar_juego)
entrada.pack()

# Establecer foco en el cuadro de entrada
entrada.focus_set()

# Iniciar la interfaz gráfica
raiz.mainloop()

# Video https://youtu.be/DfAwSMZtBqs?si=TApOadbAv8FgZ3sP