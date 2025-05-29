import tkinter as tk
from tkinter import messagebox
import numpy as np  
from simulacion_basica import simular_trayectoria
from plano_2D import simular_bumeran_animado
from plano_3D import simular_bumeran_animado_3d_vectores

# --- PARÁMETROS INICIALES ---
valores_predeterminados = {
    'R': 10.0,   # Radio de la trayectoria
    'v': 14.0,   # Velocidad lineal del bumerang (inicial)
    'k': 0.1     # Coeficiente de amortiguamiento (desaceleración)
}

def iniciar_simulacion():
    try:
        R = float(entries['R'].get())
        v = float(entries['v'].get())
        k = float(entries['k'].get())
        if R <= 0 or v <= 0 or k < 0:
            messagebox.showerror("Error", "Los parámetros deben ser positivos (R y v > 0, k ≥ 0).")
            return
        simular_trayectoria(R, v, k, root)
    except ValueError:
        messagebox.showerror("Error", "Todos los parámetros deben ser números válidos.")


def iniciar_simulacion_avanzada():
    ventana_avanzada = tk.Toplevel(root)
    ventana_avanzada.title("Parámetros - Simulación Avanzada")
    ventana_avanzada.geometry("350x400")

    parametros = {
        'R_x': 10.0,
        'R_y': 4.0,
        'omega_x': 0.35 * np.pi,
        'omega_y': 0.3 * np.pi,
        'k': 0.1,
        'z_max': 5.0,
        't_max': 10.0,
        'dt': 0.01
    }

    entries_avanzados = {}

    for i, (clave, valor) in enumerate(parametros.items()):
        tk.Label(ventana_avanzada, text=f"{clave}:").grid(row=i, column=0, sticky='e', padx=10, pady=5)
        entrada = tk.Entry(ventana_avanzada, width=15)
        entrada.insert(0, str(valor))
        entrada.grid(row=i, column=1, pady=5)
        entries_avanzados[clave] = entrada

    def ejecutar_simulacion_avanzada():
        try:
            valores = {clave: float(entry.get()) for clave, entry in entries_avanzados.items()}
            ventana_avanzada.destroy()
            simular_bumeran_animado(**valores)
        except ValueError:
            messagebox.showerror("Error", "Todos los parámetros deben ser números válidos.")

    tk.Button(ventana_avanzada, text="Iniciar Simulación", command=ejecutar_simulacion_avanzada).grid(row=len(parametros), column=0, columnspan=2, pady=20)

# --- FUNCIÓN PARA INICIAR LA SIMULACIÓN ---
def iniciar_simulacion():
    try:
        R = float(entries['R'].get())
        v = float(entries['v'].get())
        k = float(entries['k'].get())

        if R <= 0 or v <= 0 or k < 0:
                messagebox.showerror("Error", "Los parámetros deben ser positivos (R y v > 0, k ≥ 0).")
                return
        # Se llama a la función de simulación con los valores ingresados
        simular_trayectoria(R, v, k)
    except ValueError:
        messagebox.showerror("Error", "Todos los parámetros deben ser números válidos.")


# --- VENTANA PRINCIPAL (Interfaz gráfica) ---
root = tk.Tk()
root.title("Simulación de Bumerang")
root.geometry("400x250")              # Tamaño de la ventana


# Crear etiquetas y campos de entrada
frame_top = tk.Frame(root)
frame_top.pack(pady=10)

entries = {}
for i, (clave, valor) in enumerate(valores_predeterminados.items()):
    tk.Label(frame_top, text=f"{clave}:", width=5).grid(row=i, column=0, sticky='e')
    entrada = tk.Entry(frame_top, width=20, fg='gray')
    entrada.insert(0, str(valor))
    entrada.grid(row=i, column=1)
    entrada.bind("<KeyRelease>")
    entries[clave] = entrada

frame_bottom = tk.Frame(root)
frame_bottom.pack(pady=20)

tk.Button(frame_bottom, text="Iniciar simulación básica", command=iniciar_simulacion, width=25).grid(row=0, column=0, pady=5)
tk.Button(frame_bottom, text="Simulación avanzada", command=iniciar_simulacion_avanzada, width=25).grid(row=1, column=0, pady=5)
tk.Button(frame_bottom, text="Salir", command=root.destroy, width=25).grid(row=2, column=0, pady=5)

root.mainloop()