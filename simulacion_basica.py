# simulacion_basica.py
import numpy as np
import matplotlib.pyplot as plt
import time
import tkinter as tk
from tkinter import messagebox

def simular_trayectoria(R, v, k, root):
    omega = v / R
    t_final = 2 * np.pi / omega

    fig, ax = plt.subplots()
    ax.set_xlim(-R, R)
    ax.set_ylim(-R, R)
    ax.set_aspect('equal')
    ax.grid(True)
    ax.set_xlabel("x(t) [m]")
    ax.set_ylabel("y(t) [m]")
    ax.set_title("Simulación de la trayectoria del bumerang")

    linea_trayectoria, = ax.plot([], [], 'b-', label='Trayectoria')
    punto_actual, = ax.plot([], [], 'ro', label='Bumerang')

    x_vals, y_vals = [], []
    t0 = time.perf_counter()

    while True:
        t = time.perf_counter() - t0
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

    ax.set_title(f"Trayectoria completa (1 giro) — Tiempo total: {t:.2f} s")
    plt.show()

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
