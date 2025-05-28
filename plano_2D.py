import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def simular_bumeran_animado(R_x, R_y, omega_x, omega_y, k, z_max, t_max, dt):
    t = np.arange(0, t_max, dt)

    # Trayectoria en XY con diferentes omegas
    x = R_x * np.exp(-k * t) * np.cos(omega_x * t)
    y = R_y * np.exp(-k * t) * np.sin(omega_y * t)

    # Ajustar para que comience en (0,0)
    x = x - x[0]
    y = y - y[0]

    # Altura (Z) con forma de campana
    z = z_max * np.sin(np.pi * t / t_max)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14,6))

    # Plano XY
    ax1.plot(x, y, 'lightgray', label='Trayectoria completa')
    trayectoria_xy, = ax1.plot([], [], 'b-', alpha=0.6, label='Trayectoria recorrida')
    punto_xy, = ax1.plot([], [], 'ro', label='Búmeran (posición actual)', markersize=8)
    ax1.set_title('Trayectoria XY (vista desde arriba)')
    ax1.set_xlabel('x (m)')
    ax1.set_ylabel('y (m)')
    ax1.grid(True)
    ax1.axis('equal')
    ax1.set_xlim(min(x)-1, max(x)+1)
    ax1.set_ylim(min(y)-1, max(y)+1)
    ax1.legend()

    # Plano XZ (altura)
    ax2.plot(x, z, 'lightgray', label='Altura completa')
    trayectoria_xz, = ax2.plot([], [], 'g-', alpha=0.6, label='Altura recorrida')
    punto_xz, = ax2.plot([], [], 'ro', label='Búmeran (posición actual)', markersize=8)
    ax2.set_title('Altura Z vs X')
    ax2.set_xlabel('x (m)')
    ax2.set_ylabel('z (m)')
    ax2.grid(True)
    ax2.set_xlim(min(x)-1, max(x)+1)
    ax2.set_ylim(0, z_max + 1)
    ax2.legend()

    def init():
        punto_xy.set_data([], [])
        trayectoria_xy.set_data([], [])
        punto_xz.set_data([], [])
        trayectoria_xz.set_data([], [])
        return punto_xy, trayectoria_xy, punto_xz, trayectoria_xz

    def update(frame):
        punto_xy.set_data([x[frame]], [y[frame]])
        trayectoria_xy.set_data(x[:frame], y[:frame])
        punto_xz.set_data([x[frame]], [z[frame]])
        trayectoria_xz.set_data(x[:frame], z[:frame])
        return punto_xy, trayectoria_xy, punto_xz, trayectoria_xz

    ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=1)
    plt.show()

if __name__ == "__main__":
    R_x = 10               # Radio en X
    R_y = 4               # Radio en Y
    omega_x = 0.35 * np.pi # Velocidad angular en X
    omega_y = 0.3 * np.pi # Velocidad angular en Y
    k = 0.1                # Amortiguamiento

      # Condiciones atmosféricas
    # k = 0.05   Día calmo, poco viento
    # k = 0.1    Condiciones normales
    # k = 0.3    Día ventoso
    # k = 0.5    Condiciones muy adversas

    z_max = 5              # Altura máxima
    t_max = 10            # Tiempo total
    dt = 0.01              # Paso de tiempo

    simular_bumeran_animado(R_x, R_y, omega_x, omega_y, k, z_max, t_max, dt)
