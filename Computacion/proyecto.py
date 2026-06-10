# Librerias importantes
import tkinter as tk
from tkinter import messagebox
import numpy as np

# Configuración de Matplotlib para que funcione dentro de Tkinter
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from scipy.optimize import curve_fit

# Función exponencial para el ajuste 
def modelo_exponencial(x, a, b, c):
    return a * np.exp(b * x) + c

# Clase Principal de la interfaz gráfica para la interacción
class AppGraficador:
    def __init__(self, root):
        self.root = root
        self.root.title("Comparador de Funciones Matemáticas")
        #self.root.geometry("1100x700") Acá puedo comentar la otra si no quiero pantalla máxima al abrir
        self.root.state('zoomed') # Maximizar ventana al abrir

        # Estilo de fuentes
        self.font_title = ("Arial", 12, "bold")
        self.font_label = ("Arial", 10)

        # Crear los dos paneles principales: Izquierda (Controles) y Derecha (Gráficos)
        self.panel_izquierdo = tk.Frame(self.root, width=300, bg="#f0f0f0", padx=15, pady=15)
        self.panel_izquierdo.pack(side=tk.LEFT, fill=tk.Y)

        self.panel_derecho = tk.Frame(self.root, bg="white")
        self.panel_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.crear_controles()
        self.inicializar_graficos()
        self.cargar_ejemplo()

    def crear_controles(self):
        # Título del panel
        lbl_instrucciones = tk.Label(self.panel_izquierdo, text="Panel de Datos", font=("Arial", 14, "bold"), bg="#f0f0f0")
        lbl_instrucciones.pack(pady=(0, 15))

        # Entrada de X
        lbl_x = tk.Label(self.panel_izquierdo, text="Valores de X (separados por espacios o comas):", font=self.font_label, bg="#f0f0f0", anchor="w")
        lbl_x.pack(fill=tk.X, pady=(5, 2))
        self.txt_x = tk.Entry(self.panel_izquierdo, font=("Arial", 11), bd=2, relief=tk.GROOVE)
        self.txt_x.pack(fill=tk.X, pady=(0, 10))

        # Entrada de f(x)
        lbl_y = tk.Label(self.panel_izquierdo, text="Valores de Y (separados por espacios o comas):", font=self.font_label, bg="#f0f0f0", anchor="w")
        lbl_y.pack(fill=tk.X, pady=(5, 2))
        self.txt_y = tk.Entry(self.panel_izquierdo, font=("Arial", 11), bd=2, relief=tk.GROOVE)
        self.txt_y.pack(fill=tk.X, pady=(0, 15))

        # Botón para graficar
        btn_graficar = tk.Button(self.panel_izquierdo, text="📈 Graficar y Comparar", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", cursor="hand2", command=self.procesar_y_graficar)
        btn_graficar.pack(fill=tk.X, pady=5)

        # Botón para limpiar
        btn_limpiar = tk.Button(self.panel_izquierdo, text="🗑️ Limpiar valores", font=("Arial", 10), bg="#f44336", fg="white", cursor="hand2", command=self.limpiar_campos)
        btn_limpiar.pack(fill=tk.X, pady=5)

        # Nota educativa abajo en el panel
        lbl_ayuda = tk.Label(self.panel_izquierdo, text="\n💡 Ayuda pedagógica:\nObserva cuál de las funciones\npasa exactamente sobre tus\npuntos rojos para saber\ncuál describe mejor tus datos ¿Te parece que son todas las funciones posibles?.", font=("Arial", 9, "italic"), bg="#f0f0f0", fg="#555", justify=tk.LEFT)
        lbl_ayuda.pack(side=tk.BOTTOM, fill=tk.X)

    def inicializar_graficos(self):
        # Crear la figura matemática con un diseño de 2x2
        self.fig = Figure(figsize=(8, 7), dpi=100)
        self.axs = self.fig.subplots(2, 2)
        self.fig.suptitle("¿Qué función se adapta mejor a tus puntos?", fontsize=14, fontweight="bold")
        
        # Integrar la figura de Matplotlib en el lienzo de Tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.panel_derecho)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Añadir la barra de herramientas de Matplotlib por si quieren hacer zoom o guardar la imagen
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.panel_derecho)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def cargar_ejemplo(self):
        # Carga el ejemplo por defecto solicitado (Días 1-10 y reglas constante en 1)
        self.txt_x.insert(0, "1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
        self.txt_y.insert(0, "1, 1, 1, 1, 1, 1, 1, 1, 1, 1")
        self.procesar_y_graficar()

    def limpiar_campos(self):
        self.txt_x.delete(0, tk.END)
        self.txt_y.delete(0, tk.END)

    def procesar_y_graficar(self):
        # Obtener textos y limpiar formatos de comas
        str_x = self.txt_x.get().replace(',', ' ')
        str_y = self.txt_y.get().replace(',', ' ')

        # Validación de datos: no dejar que pasen errores.
        if not str_x.strip() or not str_y.strip():
            messagebox.showwarning("Campos Vacíos", "Por favor, introduce valores numéricos tanto en X como en Y.")
            return

        try:
            x_data = np.array([float(x) for x in str_x.split()])
            y_data = np.array([float(y) for y in str_y.split()])
        except ValueError:
            messagebox.showerror("Error de Formato", "Asegúrate de ingresar únicamente números separados por espacios o comas.")
            return

        if len(x_data) != len(y_data):
            messagebox.showerror("Error de Datos", f"La cantidad de elementos no coincide.\nTienes {len(x_data)} valores en X y {len(y_data)} en Y.")
            return
        
        if len(x_data) < 2:
            messagebox.showwarning("Pocos datos", "Introduce al menos 2 puntos para realizar los ajustes matemáticos.")
            return

        # Limpiar los gráficos anteriores para dibujar los nuevos de cero
        for row in self.axs:
            for ax in row:
                ax.clear()

        # Eje X continuo para suavizar curvas
        x_suave = np.linspace(min(x_data) - 0.5, max(x_data) + 0.5, 300)

        #  1. Función constante
        ax = self.axs[0, 0]
        c_val = np.mean(y_data)
        ax.scatter(x_data, y_data, color='red', s=40, zorder=5, label='Puntos')
        ax.plot(x_suave, np.full_like(x_suave, c_val), color='blue', linewidth=2, label=f'y = {c_val:.2f}')
        ax.set_title("Constante ($y=c$)", color='blue', fontdict={'weight': 'bold'})
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.legend(fontsize=9)

        #  2. Función lineal
        ax = self.axs[0, 1]
        try:
            m, b = np.polyfit(x_data, y_data, 1)
            y_lineal = m * x_suave + b
            lbl = f'y = {m:.2f}x + {b:.2f}'
        except:
            y_lineal = np.full_like(x_suave, np.mean(y_data))
            lbl = 'No calculable'
        ax.scatter(x_data, y_data, color='red', s=40, zorder=5, label='Puntos')
        ax.plot(x_suave, y_lineal, color='green', linewidth=2, label=lbl)
        ax.set_title("Lineal ($y=mx+b$)", color='green', fontdict={'weight': 'bold'})
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.legend(fontsize=9)

        #  3. Función cuadrática
        ax = self.axs[1, 0]
        try:
            a, b_coef, c_coef = np.polyfit(x_data, y_data, 2)
            y_cuad = a * x_suave**2 + b_coef * x_suave + c_coef
            lbl = f'y = {a:.2f}x² + {b_coef:.2f}x + {c_coef:.2f}'
        except:
            y_cuad = np.full_like(x_suave, np.mean(y_data))
            lbl = 'No calculable'
        ax.scatter(x_data, y_data, color='red', s=40, zorder=5, label='Puntos')
        ax.plot(x_suave, y_cuad, color='purple', linewidth=2, label=lbl)
        ax.set_title("Cuadrática ($y=ax²+bx+c$)", color='purple', fontdict={'weight': 'bold'})
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.legend(fontsize=8)

        # 4. Función Exponencial
        ax = self.axs[1, 1]
        try:
            # Estimación inicial (p0) para el ajuste exponencial
            # Un ajuste razonable suele ser [1, 0.1, 1]
            popt, _ = curve_fit(modelo_exponencial, x_data, y_data, p0=[1, 0.1, np.mean(y_data)], maxfev=10000)
            y_exp = modelo_exponencial(x_suave, *popt)
            lbl = f'y = {popt[0]:.2f}·e^({popt[1]:.2f}x) + {popt[2]:.2f}'
        except:
            y_exp = np.full_like(x_suave, np.mean(y_data))
            lbl = 'Ajuste no convergió'
        
        ax.scatter(x_data, y_data, color='red', s=40, zorder=5, label='Puntos')
        ax.plot(x_suave, y_exp, color='orange', linewidth=2, label=lbl)
        ax.set_title("Exponencial ($y=a·e^{bx}+c$)", color='orange', fontdict={'weight': 'bold'})
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.legend(fontsize=8)

        # Reajustar márgenes automáticamente y redibujar el lienzo
        self.fig.tight_layout()
        self.canvas.draw()

# Ejecución de la ventana
if __name__ == "__main__":
    root = tk.Tk()
    app = AppGraficador(root)
    root.mainloop()