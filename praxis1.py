import numpy as np
import matplotlib.pyplot as plt

def simular_bumeran(R, w, k, t_max, dt):
    try:
        # Vector de tiempo
        t = np.arange(0, t_max, dt)
        
        # Ecuaciones paramétricas del movimiento
        x = R * np.exp(-k * t) * np.cos(w * t)
        y = R * np.exp(-k * t) * np.sin(w * t)
        
        # Gráfica de la trayectoria
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label='Trayectoria del búmeran')
        plt.title('Simulación de la trayectoria del búmeran')
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')
        plt.grid(True)
        plt.axis('equal')
        plt.legend()
        plt.show()
        
    except Exception as e:
        print(f"Error durante la simulación: {e}")

if __name__ == '__main__':
    # Parámetros de simulación
    R = 10           # Radio inicial (m)
    w = 0.9 * np.pi  # Velocidad angular (rad/s) (afecta la cantidad de vueltas por segundo)
    k = 0.1          # Coeficiente de amortiguamiento

    # Condiciones atmosféricas
    # k = 0.05   Día calmo, poco viento
    # k = 0.1    Condiciones normales
    # k = 0.3    Día ventoso
    # k = 0.5    Condiciones muy adversas

    t_max = 7       # Tiempo total (s)
    dt = 0.01        # Paso de tiempo (s)
    
    simular_bumeran(R, w, k, t_max, dt)