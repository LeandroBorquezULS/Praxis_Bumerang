import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

def simular_bumeran_animado_3d_vectores(R_x, R_y, omega_x, omega_y, k, z_max, t_max, dt):
    t = np.arange(0, t_max, dt)

    # Trayectoria en XY
    x = R_x * np.exp(-k * t) * np.cos(omega_x * t)
    y = R_y * np.exp(-k * t) * np.sin(omega_y * t)

    # Ajustar para que comience en (0,0)
    x = x - x[0]
    y = y - y[0]

    # Altura (Z) con forma de campana
    z = z_max * np.sin(np.pi * t / t_max)

    # Cálculo de los vectores tangente (T), normal (N), binormal (B)
    pos = np.vstack((x, y, z)).T
    dp = np.gradient(pos, axis=0)
    T_vec = dp / np.linalg.norm(dp, axis=1)[:, None]
    dT = np.gradient(T_vec, axis=0)
    N_vec = dT / np.linalg.norm(dT, axis=1)[:, None]
    B_vec = np.cross(T_vec, N_vec)
    B_vec = B_vec / np.linalg.norm(B_vec, axis=1)[:, None]

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Trayectoria completa en gris claro
    ax.plot(x, y, z, color='lightgray', label='Trayectoria completa')

    # Elementos animados
    trayectoria, = ax.plot([], [], [], 'b-', alpha=0.7, label='Trayectoria recorrida')
    punto, = ax.plot([], [], [], 'ro', markersize=8, label='Búmeran (posición actual)')

    # Quivers (vectores)
    quiv_tan = None
    quiv_norm = None
    quiv_bin = None

    # Texto para el tiempo transcurrido
    tiempo_text = ax.text2D(0.05, 0.95, '', transform=ax.transAxes, fontsize=10, color='red', bbox=dict(facecolor='white', alpha=0.9))

    ax.set_title('Vuelo 3D del Búmeran con vectores de Frenet-Serret')
    ax.set_xlabel('x (m)')
    ax.set_ylabel('y (m)')
    ax.set_zlabel('z (m)')
    ax.grid(True)
    ax.set_xlim(min(x)-1, max(x)+1)
    ax.set_ylim(min(y)-1, max(y)+1)
    ax.set_zlim(0, z_max + 1)
    ax.legend()

    def init():
        trayectoria.set_data([], [])
        trayectoria.set_3d_properties([])
        punto.set_data([], [])
        punto.set_3d_properties([])
        tiempo_text.set_text('')
        return trayectoria, punto, tiempo_text

    def update(frame):
        nonlocal quiv_tan, quiv_norm, quiv_bin

        trayectoria.set_data(x[:frame], y[:frame])
        trayectoria.set_3d_properties(z[:frame])
        punto.set_data([x[frame]], [y[frame]])
        punto.set_3d_properties([z[frame]])

        # Elimina los quivers anteriores si existen
        if quiv_tan is not None:
            quiv_tan.remove()
        if quiv_norm is not None:
            quiv_norm.remove()
        if quiv_bin is not None:
            quiv_bin.remove()

        # Dibuja los nuevos quivers para Frenet Frame (puedes ajustar el parámetro length)
        length = 1  # Ajusta el largo de los vectores a tu gusto
        idx = frame
        quiv_tan = ax.quiver(x[idx], y[idx], z[idx],
                             T_vec[idx,0], T_vec[idx,1], T_vec[idx,2],
                             color='g', length=length, normalize=True, linewidth=2, label='Tangente' if frame==0 else "")
        quiv_norm = ax.quiver(x[idx], y[idx], z[idx],
                              N_vec[idx,0], N_vec[idx,1], N_vec[idx,2],
                              color='r', length=length, normalize=True, linewidth=2, label='Normal' if frame==0 else "")
        quiv_bin = ax.quiver(x[idx], y[idx], z[idx],
                             B_vec[idx,0], B_vec[idx,1], B_vec[idx,2],
                             color='k', length=length, normalize=True, linewidth=2, label='Binormal' if frame==0 else "")

        # Actualiza el texto del tiempo transcurrido
        tiempo_text.set_text(f"Tiempo transcurrido: {t[frame]:.2f} s")
        return trayectoria, punto, quiv_tan, quiv_norm, quiv_bin, tiempo_text

    ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=False, interval=20)
    plt.show()

def menu():
    print("Simulación del vuelo de un búmeran en 3D con vectores de Frenet-Serret")
    print("1. Iniciar simulación por defecto (lanzamiento real)")
    print("2. Lanzamiento personalizado basico")
    print("   -Editar amortiguamiento (perdida de energia) y Radio iniciales para X e Y")
    print("3. Lanzamiento personalizado avanzado")
    print("   -Editar todos los parámetros de la simulación")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if not opcion.isdigit() or opcion not in ['1', '2', '3', '4']:
        print("Opción no válida. Intente de nuevo.")
        return menu()
    return opcion


if __name__ == "__main__":
    opcion = menu()
    if opcion == '1':
        # Parámetros del lanzamiento real
        R_x = 3              # Radio inicial (influye en el ancho del recorrido)
        R_y = 10             # Radio inicial en Y (influye en la lejanía del lanzamiento)
        omega_x = 0.24 * np.pi # Velocidad angular en X
        omega_y = 0.24 * np.pi # Velocidad angular en Y
        k = 0.3              # Amortiguamiento (cuánto se cierra la espiral)(Perdida de energía)
        z_max = 5            # Altura máxima
        t_max = 5.5          # Tiempo total
        dt = 0.06           # Paso de tiempo

        simular_bumeran_animado_3d_vectores(R_x, R_y, omega_x, omega_y, k, z_max, t_max, dt)

    elif opcion == '2':
        # Lanzamiento personalizado básico
        while True:
            try:
                R_x = float(input("Ingrese el radio inicial en X (ejemplo: 3): "))
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido para el radio en X.")
        while True:
            try:
                R_y = float(input("Ingrese el radio inicial en Y (ejemplo: 10): "))
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido para el radio en Y.")
        print("Ingrese las siguientes opciones de Amortiguamiento:")
        print("0.05 Poco viento, día calmo")
        print("0.1 Condiciones normales")
        print("0.3 es un día ventoso")
        print("0.5 Condiciones muy adversas")
        while True:
            k_input = input("(ejemplo: 0.3): ")
            try:
                k = float(k_input)
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido para el amortiguamiento.")
        omega_x = 0.24 * np.pi # Velocidad angular en X por defecto
        omega_y = 0.24 * np.pi # Velocidad angular en Y por defecto
        z_max = 5            # Altura máxima por defecto
        t_max = 5.5          # Tiempo total por defecto
        dt = 0.06           # Paso de tiempo por defecto

        simular_bumeran_animado_3d_vectores(R_x, R_y, omega_x, omega_y, k, z_max, t_max, dt)

    elif opcion == '3':
        # Lanzamiento personalizado avanzado
        while True:
            try:
                R_x = float(input("Ingrese el radio inicial en X: "))
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido para el radio en X.")
        while True:
            try:
                R_y = float(input("Ingrese el radio inicial en Y: "))
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido para el radio en Y.")
        while True:
            try:
                omega_x = float(input("Ingrese la velocidad angular en X (en rad/s): ")) * np.pi / 180
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido para la velocidad angular en X.")
        while True:
            try:
                omega_y = float(input("Ingrese la velocidad angular en Y (en rad/s): ")) * np.pi / 180
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido para la velocidad angular en Y.")
        while True:
            try:
                k = float(input("Ingrese el valor de amortiguamiento (ejemplo: 0.3): "))
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido para el amortiguamiento.")
        while True:
            try:
                z_max = float(input("Ingrese la altura máxima (ejemplo: 5): "))
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido para la altura máxima.")
        while True:
            try:
                t_max = float(input("Ingrese el tiempo total (ejemplo: 5.5): "))
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido para el tiempo total.")
        dt = 0.06
        # Paso de tiempo por defecto

        simular_bumeran_animado_3d_vectores(R_x, R_y, omega_x, omega_y, k, z_max, t_max, dt)

    else:
        print("Saliendo de la simulación.")
