import numpy as np
import matplotlib.pyplot as plt

def simular_bumeran(R=10, omega=2*np.pi, k=0.1, t_max=10, dt=0.01):
    try:
        # Vector de tiempo
        t = np.arange(0, t_max, dt)
        
        # Ecuaciones paramétricas del movimiento
        x = R * np.exp(-k * t) * np.cos(omega * t)
        y = R * np.exp(-k * t) * np.sin(omega * t)
        
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
    omega = 2 * np.pi  # Velocidad angular (rad/s) (cantidad de vueltas por segundo)
    k = 0.1          # Coeficiente de amortiguamiento (afecta en la distancia entre el lanzamiento y la vuelta)
    t_max = 1       # Tiempo total (s)
    dt = 0.01        # Paso de tiempo (s)
    
    simular_bumeran(R, omega, k, t_max, dt)