import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import time

# --- PARÁMETROS INICIALES ---
valores_predeterminados = {
    'R': 10.0,   # Radio de la trayectoria
    'v': 14.0,   # Velocidad lineal del bumerang (inicial)
    'k': 0.1     # Coeficiente de amortiguamiento (desaceleración)
}

# --- FUNCIÓN DE SIMULACIÓN ---
def simular_trayectoria(R, v, k):
    # Calculo de la velocidad angular (omega)
    omega = v / R
    # Tiempo total para completar una vuelta completa (2π radianes)
    t_final = 2 * np.pi / omega

    # Ventana de la gráfica
    fig, ax = plt.subplots()
    ax.set_xlim(-R, R)
    ax.set_ylim(-R, R)
    ax.set_aspect('equal')
    ax.grid(True)
    ax.set_xlabel("x(t) [m]")
    ax.set_ylabel("y(t) [m]")
    ax.set_title("Simulación de la trayectoria del bumerang")

    # Se crean dos elementos gráficos: línea azul para la trayectoria y punto rojo para el bumerang
    linea_trayectoria, = ax.plot([], [], 'b-', label='Trayectoria')
    punto_actual, = ax.plot([], [], 'ro', label='Bumerang')

    # Listas para almacenar los valores de x, y en el tiempo
    x_vals, y_vals = [], []

    # Tiempo inicial de la simulación
    t0 = time.perf_counter()

    # Bucle para actualiza la posición del bumerang
    while True:
        t = time.perf_counter() - t0

        # Si se completó una vuelta, se termina la simulación
        if t >= t_final:
            break

        x = R * np.cos(omega * t) * np.exp(-k * t)
        y = R * np.sin(omega * t) * np.exp(-k * t)

        x_vals.append(x)
        y_vals.append(y)

        linea_trayectoria.set_data(x_vals, y_vals)
        punto_actual.set_data([x], [y])

        ax.set_title(f"Trayectoria del bumerang | Tiempo: {t:.2f} s")
        plt.legend()
        plt.pause(0.01)

    # Al finalizar, se muestra la gráfica completa
    ax.set_title(f"Trayectoria completa (1 giro) — Tiempo total: {t:.2f} s")
    plt.show()

    # Mostrar fórmula para Wolfram Alpha en nueva ventana
    mostrar_formula_wolfram(R, v, k, t_final, root)

def mostrar_formula_wolfram(R, v, k, t_final, root):
    formula = f"parametric plot {{ {R:.2f}*cos({v/R:.2f}*t)*exp(-{k:.2f}*t), {R:.2f}*sin({v/R:.2f}*t)*exp(-{k:.2f}*t) }} for t=0 to {t_final:.2f}"

    ventana_formula = tk.Toplevel(root)
    ventana_formula.title("Fórmula para Wolfram Alpha")
    ventana_formula.geometry("520x200")

    tk.Label(ventana_formula, text="Fórmula lista para copiar y pegar en Wolfram Alpha:").pack(pady=10)

    campo_texto = tk.Text(ventana_formula, wrap="word", height=4, width=65)
    campo_texto.pack(padx=10)
    campo_texto.insert("1.0", formula)
    campo_texto.config(state="disabled")

    def copiar_al_portapapeles():
        root.clipboard_clear()
        root.clipboard_append(formula)
        messagebox.showinfo("Copiado", "Fórmula copiada al portapapeles.")

    tk.Button(ventana_formula, text="Copiar fórmula", command=copiar_al_portapapeles).pack(pady=5)
    tk.Button(ventana_formula, text="Cerrar", command=ventana_formula.destroy).pack(pady=5)

# --- VENTANA PRINCIPAL (Interfaz gráfica) ---
root = tk.Tk()
root.title("Simulación de Bumerang")
root.geometry("400x250")              # Tamaño de la ventana

# --- FUNCIÓN PARA INICIAR LA SIMULACIÓN ---
def iniciar_simulacion():
    try:
        R = float(entries['R'].get())
        v = float(entries['v'].get())
        k = float(entries['k'].get())

        # Se llama a la función de simulación con los valores ingresados
        simular_trayectoria(R, v, k)
    except ValueError:
        messagebox.showerror("Error", "Todos los parámetros deben ser números válidos.")

# Actualiza el color del texto dependiendo si es predeterminado o modificado
def verificar_modificacion(event=None):
    for clave, entry in entries.items():
        valor_actual = entry.get()
        try:
            valor = float(valor_actual)
            if valor == valores_predeterminados[clave]:
                entry.config(fg='gray')
            else:
                entry.config(fg='black')
        except ValueError:
            entry.config(fg='black')

# Crear etiquetas y campos de entrada
frame_top = tk.Frame(root)
frame_top.pack(pady=10)

entries = {}
for i, (clave, valor) in enumerate(valores_predeterminados.items()):
    tk.Label(frame_top, text=f"{clave}:", width=5).grid(row=i, column=0, sticky='e')
    entrada = tk.Entry(frame_top, width=20, fg='gray')
    entrada.insert(0, str(valor))
    entrada.grid(row=i, column=1)
    entrada.bind("<KeyRelease>", verificar_modificacion)
    entries[clave] = entrada

# --- BOTONES DE LA INTERFAZ ---
frame_bottom = tk.Frame(root)
frame_bottom.pack(pady=20)

btn_basica = tk.Button(frame_bottom, text="Iniciar simulación básica", command=iniciar_simulacion, width=25)    # Botón para iniciar la simulación
btn_avanzada = tk.Button(frame_bottom, text="Simulación avanzada", state="disabled", width=25)                  # Botón para simulación avanzada (desactivado)
btn_salir = tk.Button(frame_bottom, text="Salir", command=root.destroy, width=25)                               # Botón para cerrar la aplicación

# Posicionar los botones uno debajo del otro
btn_basica.grid(row=0, column=0, pady=5)
btn_avanzada.grid(row=1, column=0, pady=5)
btn_salir.grid(row=2, column=0, pady=5)

# Verifica inicial
verificar_modificacion()

# Ejecutar GUI
root.mainloop()