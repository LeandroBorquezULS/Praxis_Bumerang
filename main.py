import tkinter as tk
from tkinter import messagebox
import numpy as np
from simulacion_basica import simular_trayectoria
from plano_2D import simular_bumeran_animado
from plano_3D import simular_bumeran_animado_3d_vectores

class VentanaPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simulación de Bumerang")
        self.root.geometry("400x300")
        self.crear_interfaz()

    def crear_interfaz(self):
        # Frame principal
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)

        # Título
        titulo = tk.Label(frame, text="Simulador de Bumerang", font=("Arial", 16, "bold"))
        titulo.pack(pady=20)

        # Botones
        tk.Button(frame, text="Simulación por defecto", 
                 command=self.menu_defecto, width=25).pack(pady=10)
        
        tk.Button(frame, text="Simulación personalizada simple", 
                 command=self.personalizado_simple, width=25).pack(pady=10)
        
        tk.Button(frame, text="Simulación personalizada avanzada", 
                 command=self.personalizado_avanzado, width=25).pack(pady=10)
        
        tk.Button(frame, text="Salir", 
                 command=self.root.destroy, width=25).pack(pady=10)

    def menu_defecto(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Tipo de simulación por defecto")
        ventana.geometry("300x400")

        tk.Label(ventana, text="=== Menú de lanzamientos por defecto ===", 
                 font=("Arial", 12, "bold")).pack(pady=10)

        def simulacion_2d(tipo):
            ventana.destroy()
            if tipo == "normal":
                simular_bumeran_animado(-15, 4, 0.35*np.pi, 0.3*np.pi, 0.1, 15, 10, 0.01)
            elif tipo == "desviado":
                simular_bumeran_animado(15, 6, 0.4*np.pi, 0.2*np.pi, 0.3, 15, 10, 0.01)
            elif tipo == "perfecto":
                simular_bumeran_animado(25, 8, 1.5*np.pi, 1.5*np.pi, 0.15, 6, 7, 0.01)
            elif tipo == "agresivo":
                simular_bumeran_animado(15, 5, 0.5*np.pi, 0.4*np.pi, 0.2, 15, 9, 0.01)

        def simulacion_3d(tipo):
            ventana.destroy()
            if tipo == "normal":
                simular_bumeran_animado_3d_vectores(-15, 4, 0.35*np.pi, 0.3*np.pi, 0.1, 15, 10, 0.01)
            elif tipo == "desviado":
                simular_bumeran_animado_3d_vectores(15, 6, 0.4*np.pi, 0.2*np.pi, 0.3, 15, 10, 0.01)
            elif tipo == "perfecto":
                simular_bumeran_animado_3d_vectores(25, 8, 1.5*np.pi, 1.5*np.pi, 0.15, 6, 7, 0.01)
            elif tipo == "agresivo":
                simular_bumeran_animado_3d_vectores(15, 5, 0.5*np.pi, 0.4*np.pi, 0.2, 15, 9, 0.01)

        # Frame para 2D
        frame_2d = tk.LabelFrame(ventana, text="Simulación 2D", padx=10, pady=5)
        frame_2d.pack(padx=10, pady=5, fill="x")

        tk.Button(frame_2d, text="1. Lanzamiento normal", 
                 command=lambda: simulacion_2d("normal"), width=25).pack(pady=2)
        tk.Button(frame_2d, text="2. Lanzamiento desviado", 
                 command=lambda: simulacion_2d("desviado"), width=25).pack(pady=2)
        tk.Button(frame_2d, text="3. Lanzamiento perfecto", 
                 command=lambda: simulacion_2d("perfecto"), width=25).pack(pady=2)
        tk.Button(frame_2d, text="4. Lanzamiento agresivo", 
                 command=lambda: simulacion_2d("agresivo"), width=25).pack(pady=2)

        # Frame para 3D
        frame_3d = tk.LabelFrame(ventana, text="Simulación 3D", padx=10, pady=5)
        frame_3d.pack(padx=10, pady=5, fill="x")

        tk.Button(frame_3d, text="1. Lanzamiento normal", 
                 command=lambda: simulacion_3d("normal"), width=25).pack(pady=2)
        tk.Button(frame_3d, text="2. Lanzamiento desviado", 
                 command=lambda: simulacion_3d("desviado"), width=25).pack(pady=2)
        tk.Button(frame_3d, text="3. Lanzamiento perfecto", 
                 command=lambda: simulacion_3d("perfecto"), width=25).pack(pady=2)
        tk.Button(frame_3d, text="4. Lanzamiento agresivo", 
                 command=lambda: simulacion_3d("agresivo"), width=25).pack(pady=2)

    def personalizado_simple(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Simulación Personalizada Simple")
        ventana.geometry("300x300")  # Aumenté un poco la altura para el nuevo campo

        entries = {}
        parametros = {
            'R': 10.0,
            'v': 14.0,
            'k': 0.1,
            't': 10.0  # Añadido nuevo parámetro de tiempo
        }

        for i, (key, value) in enumerate(parametros.items()):
            label_text = {
                'R': 'Radio (R):',
                'v': 'Velocidad (v):',
                'k': 'Constante de amortiguamiento (k):',
                't': 'Tiempo máximo (t):'
            }
            tk.Label(ventana, text=label_text[key]).pack(pady=5)
            entry = tk.Entry(ventana)
            entry.insert(0, str(value))
            entry.pack()
            entries[key] = entry

        def ejecutar():
            try:
                R = float(entries['R'].get())
                v = float(entries['v'].get())
                k = float(entries['k'].get())
                t = float(entries['t'].get())
                ventana.destroy()
                simular_trayectoria(R, v, k, self.root, t_max=t)  # Añadido parámetro t_max
            except ValueError:
                messagebox.showerror("Error", "Valores inválidos")

        tk.Button(ventana, text="Iniciar Simulación", 
                 command=ejecutar).pack(pady=20)

    def personalizado_avanzado(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Simulación Personalizada Avanzada")
        ventana.geometry("300x400")

        entries = {}
        parametros = {
            'R_x': 10.0,
            'R_y': 4.0,
            'omega_x': 0.35,
            'omega_y': 0.3,
            'k': 0.1,
            'z_max': 5.0,
            't_max': 10.0,
            'dt': 0.01
        }

        for i, (key, value) in enumerate(parametros.items()):
            tk.Label(ventana, text=f"{key}:").pack(pady=2)
            entry = tk.Entry(ventana)
            entry.insert(0, str(value))
            entry.pack()
            entries[key] = entry

        def ejecutar():
            try:
                valores = {k: float(v.get()) for k, v in entries.items()}
                ventana.destroy()
                simular_bumeran_animado(**valores)
            except ValueError:
                messagebox.showerror("Error", "Valores inválidos")

        tk.Button(ventana, text="Iniciar Simulación", 
                 command=ejecutar).pack(pady=20)

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.root.mainloop()