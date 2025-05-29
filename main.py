import tkinter as tk
from tkinter import messagebox
import numpy as np
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
                simular_bumeran_animado_3d_vectores(-15, 4, 0.35*np.pi, 0.3*np.pi, 0.1, 15, 10, 0.06)
            elif tipo == "desviado":
                simular_bumeran_animado_3d_vectores(15, 6, 0.4*np.pi, 0.2*np.pi, 0.3, 15, 10, 0.06)
            elif tipo == "perfecto":
                simular_bumeran_animado_3d_vectores(25, 8, 1.5*np.pi, 1.5*np.pi, 0.15, 6, 7, 0.06)
            elif tipo == "agresivo":
                simular_bumeran_animado_3d_vectores(15, 5, 0.5*np.pi, 0.4*np.pi, 0.2, 15, 9, 0.06)

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
        ventana.geometry("300x350")  # Aumentado para el nuevo selector

        entries = {}
        parametros = {
            'R': 10.0,
            'w': 0.6,
            'k': 0.1,
            't': 10.0
        }

        # Frame para parámetros
        frame_params = tk.Frame(ventana)
        frame_params.pack(pady=10)

        for i, (key, value) in enumerate(parametros.items()):
            label_text = {
                'R': 'Radio (R):',
                'w': 'Velocidad angular (w):',
                'k': 'Constante de amortiguamiento (k):',
                't': 'Tiempo máximo (t):'
            }
            tk.Label(frame_params, text=label_text[key]).pack(pady=5)
            entry = tk.Entry(frame_params)
            entry.insert(0, str(value))
            entry.pack()
            entries[key] = entry

        # Frame para selección de dimensión
        frame_dim = tk.LabelFrame(ventana, text="Seleccione dimensión", padx=10, pady=5)
        frame_dim.pack(pady=10)
        
        dim_var = tk.StringVar(value="2D")
        tk.Radiobutton(frame_dim, text="2D", variable=dim_var, value="2D").pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(frame_dim, text="3D", variable=dim_var, value="3D").pack(side=tk.LEFT, padx=10)

        def ejecutar():
            try:
                R = float(entries['R'].get())
                w = float(entries['w'].get())
                k = float(entries['k'].get())
                t = float(entries['t'].get())
                ventana.destroy()
                
                if dim_var.get() == "2D":
                    simular_bumeran_animado(R, R, w, w, k, 5.0, t, 0.01)
                else:
                    simular_bumeran_animado_3d_vectores(R, R, w, w, k, 5.0, t, 0.01)
                
                # Mostrar fórmula Wolfram independientemente de la dimensión elegida
                self.mostrar_formula_wolfram(R, R*w, k, t)  
            except ValueError:
                messagebox.showerror("Error", "Valores inválidos")

        tk.Button(ventana, text="Iniciar Simulación", 
                 command=ejecutar,
                 width=25, height=2).pack(pady=20)

    def mostrar_formula_wolfram(self, R, v, k, t_final):
        formula = f"parametric plot {{ {R:.2f}*cos({v/R:.2f}*t)*exp(-{k:.2f}*t), {R:.2f}*sin({v/R:.2f}*t)*exp(-{k:.2f}*t) }} for t=0 to {t_final:.2f}"
        ventana_formula = tk.Toplevel(self.root)
        ventana_formula.title("Fórmula para Wolfram Alpha")
        ventana_formula.geometry("520x200")  # Eliminar línea duplicada
        
        # Solo un Label, no dos
        tk.Label(ventana_formula, text="Fórmula lista para copiar y pegar en Wolfram Alpha:").pack(pady=10)
        
        campo_texto = tk.Text(ventana_formula, wrap="word", height=4, width=65)
        campo_texto.pack(padx=10)
        campo_texto.insert("1.0", formula)
        campo_texto.config(state="disabled")  # Solo una vez
        
        def copiar_al_portapapeles():
            self.root.clipboard_clear()
            self.root.clipboard_append(formula)
            messagebox.showinfo("Copiado", "Fórmula copiada al portapapeles.")  # Solo un mensaje
        
        tk.Button(ventana_formula, text="Copiar fórmula", 
                 command=copiar_al_portapapeles).pack(pady=5)
        tk.Button(ventana_formula, text="Cerrar", 
                 command=ventana_formula.destroy).pack(pady=5)

    def personalizado_avanzado(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Simulación Personalizada Avanzada")
        ventana.geometry("350x650")  # Aumentado para el nuevo selector
        
        entries = {}
        parametros = {
            'R_x': 10.0,
            'R_y': 4.0,
            'w_x': 0.35,
            'w_y': 0.3,
            'k': 0.1,
            'z_max': 5.0,
            't_max': 10.0,
            'dt': 0.01
        }
        
        frame = tk.Frame(ventana, padx=20, pady=10)
        frame.pack(expand=True, fill="both")
        
        tk.Label(frame, text="Parámetros de simulación", 
                 font=("Arial", 12, "bold")).pack(pady=10)

        for key, value in parametros.items():
            tk.Label(frame, text=f"{key}:").pack(pady=3)
            entry = tk.Entry(frame, width=30)
            entry.insert(0, str(value))
            entry.pack(pady=2)
            entries[key] = entry

        # Frame para selección de dimensión
        frame_dim = tk.LabelFrame(frame, text="Seleccione dimensión", padx=10, pady=5)
        frame_dim.pack(pady=10)
        
        dim_var = tk.StringVar(value="2D")
        tk.Radiobutton(frame_dim, text="2D", variable=dim_var, value="2D").pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(frame_dim, text="3D", variable=dim_var, value="3D").pack(side=tk.LEFT, padx=10)

        def ejecutar():
            try:
                valores = {k: float(v.get()) for k, v in entries.items()}
                ventana.destroy()
                
                if dim_var.get() == "2D":
                    simular_bumeran_animado(**valores)
                else:
                    simular_bumeran_animado_3d_vectores(**valores)
                
                formula = f"parametric plot {{ {valores['R_x']:.2f}*cos({valores['w_x']:.2f}*t)*exp(-{valores['k']:.2f}*t), {valores['R_y']:.2f}*sin({valores['w_y']:.2f}*t)*exp(-{valores['k']:.2f}*t) }} for t=0 to {valores['t_max']:.2f}"
                self.mostrar_formula_wolfram_avanzado(formula)
            except ValueError:
                messagebox.showerror("Error", "Valores inválidos")

        tk.Button(frame, text="Iniciar Simulación", 
                 command=ejecutar,
                 width=30,
                 height=2,
                 font=("Arial", 10, "bold")).pack(pady=20)

    def mostrar_formula_wolfram_avanzado(self, formula):
        ventana_formula = tk.Toplevel(self.root)
        ventana_formula.title("Fórmula para Wolfram Alpha")
        ventana_formula.geometry("520x200")
        
        tk.Label(ventana_formula, 
                text="Fórmula lista para copiar y pegar en Wolfram Alpha:").pack(pady=10)
        
        campo_texto = tk.Text(ventana_formula, wrap="word", height=4, width=65)
        campo_texto.pack(padx=10)
        campo_texto.insert("1.0", formula)
        campo_texto.config(state="disabled")
        
        def copiar_al_portapapeles():
            self.root.clipboard_clear()
            self.root.clipboard_append(formula)
            messagebox.showinfo("Copiado", "Fórmula copiada al portapapeles.")
        
        tk.Button(ventana_formula, text="Copiar fórmula", 
                 command=copiar_al_portapapeles).pack(pady=5)
        tk.Button(ventana_formula, text="Cerrar", 
                 command=ventana_formula.destroy).pack(pady=5)
if __name__ == "__main__":
    app = VentanaPrincipal()
    app.root.mainloop()
