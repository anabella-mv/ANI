#Librerias importanes
import tkinter as tk
from tkinter import messagebox
import numpy as np

# Configuración de Matplotlib para Tkinter
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class AppProductoLineal:
    def __init__(self, root):
        self.root = root
        self.root.title("Producto de Funciones Lineales")
        self.root.state('zoomed') # Maximizar al abrir

        # Estilos de fuentes
        self.font_title = ("Arial", 12, "bold")
        self.font_label = ("Arial", 10)
        self.font_equation = ("Courier", 11, "bold")

        # Paneles principales
        self.panel_izquierdo = tk.Frame(self.root, width=350, bg="#f5f5f5", padx=15, pady=15)
        self.panel_izquierdo.pack(side=tk.LEFT, fill=tk.Y)

        self.panel_derecho = tk.Frame(self.root, bg="white")
        self.panel_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.crear_controles()
        self.inicializar_grafico()
        
        # Cargar valores iniciales por defecto (ej: (x - 2)(x + 3))
        self.cargar_valores_defecto()

    def crear_controles(self):
        # Título del panel
        lbl_titulo = tk.Label(self.panel_izquierdo, text="Configuración de Funciones", font=("Arial", 14, "bold"), bg="#f5f5f5")
        lbl_titulo.pack(pady=(0, 20))

        # FUNCIÓN LINEAL 1
        lbl_f1 = tk.Label(self.panel_izquierdo, text="Recta 1: f(x) = m1·x + b1", font=self.font_title, fg="#1f77b4", bg="#f5f5f5")
        lbl_f1.pack(anchor="w", pady=(5, 5))
        
        frame_inputs1 = tk.Frame(self.panel_izquierdo, bg="#f5f5f5")
        frame_inputs1.pack(fill=tk.X, pady=2)
        
        tk.Label(frame_inputs1, text="m1 (Pendiente):", font=self.font_label, bg="#f5f5f5").grid(row=0, column=0, sticky="w")
        self.txt_m1 = tk.Entry(frame_inputs1, width=8, font=("Arial", 10))
        self.txt_m1.grid(row=0, column=1, padx=5, pady=2)
        
        tk.Label(frame_inputs1, text="b1 (O. origen):", font=self.font_label, bg="#f5f5f5").grid(row=1, column=0, sticky="w")
        self.txt_b1 = tk.Entry(frame_inputs1, width=8, font=("Arial", 10))
        self.txt_b1.grid(row=1, column=1, padx=5, pady=2)

        # Etiqueta para mostrar la ecuación armada de la Recta 1
        self.lbl_eq1 = tk.Label(self.panel_izquierdo, text="f(x) = ", font=self.font_equation, fg="#1f77b4", bg="#e1f5fe", anchor="w", padx=10, pady=5)
        self.lbl_eq1.pack(fill=tk.X, pady=(2, 15))

        # FUNCIÓN LINEAL 2 
        lbl_f2 = tk.Label(self.panel_izquierdo, text="Recta 2: g(x) = m2·x + b2", font=self.font_title, fg="#ff7f0e", bg="#f5f5f5")
        lbl_f2.pack(anchor="w", pady=(5, 5))
        
        frame_inputs2 = tk.Frame(self.panel_izquierdo, bg="#f5f5f5")
        frame_inputs2.pack(fill=tk.X, pady=2)
        
        tk.Label(frame_inputs2, text="m2 (Pendiente):", font=self.font_label, bg="#f5f5f5").grid(row=0, column=0, sticky="w")
        self.txt_m2 = tk.Entry(frame_inputs2, width=8, font=("Arial", 10))
        self.txt_m2.grid(row=0, column=1, padx=5, pady=2)
        
        tk.Label(frame_inputs2, text="b2 (O. origen):", font=self.font_label, bg="#f5f5f5").grid(row=1, column=0, sticky="w")
        self.txt_b2 = tk.Entry(frame_inputs2, width=8, font=("Arial", 10))
        self.txt_b2.grid(row=1, column=1, padx=5, pady=2)

        # Etiqueta para mostrar la ecuación armada de la Recta 2
        self.lbl_eq2 = tk.Label(self.panel_izquierdo, text="g(x) = ", font=self.font_equation, fg="#ff7f0e", bg="#fff3e0", anchor="w", padx=10, pady=5)
        self.lbl_eq2.pack(fill=tk.X, pady=(2, 20))

        # Separador visual
        tk.Frame(self.panel_izquierdo, height=2, bd=1, relief=tk.SUNKEN, bg="#ccc").pack(fill=tk.X, pady=10)

        # --- FUNCIÓN CUADRÁTICA RESULTANTE ---
        lbl_prod = tk.Label(self.panel_izquierdo, text="Resultado: h(x) = f(x) · g(x)", font=self.font_title, fg="#2ca02c", bg="#f5f5f5")
        lbl_prod.pack(anchor="w", pady=(5, 5))
        
        self.lbl_eq_cuad = tk.Label(self.panel_izquierdo, text="h(x) = ax² + bx + c", font=("Courier", 12, "bold"), fg="#2ca02c", bg="#e8f5e9", anchor="w", padx=10, pady=10)
        self.lbl_eq_cuad.pack(fill=tk.X, pady=(0, 20))

        # Botón para calcular y graficar
        btn_graficar = tk.Button(self.panel_izquierdo, text="📊 Calcular y Graficar", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", cursor="hand2", command=self.procesar_y_graficar)
        btn_graficar.pack(fill=tk.X, pady=5)

        # Nota pedagógica
        lbl_ayuda = tk.Label(self.panel_izquierdo, text="\n💡 Observación pedagógica:\nMira cómo los puntos donde las rectas cortan al eje X (raíces) son exactamente los mismos puntos donde la parábola corta al eje X.", font=("Arial", 9, "italic"), bg="#f5f5f5", fg="#555", justify=tk.LEFT, wraplength=300)
        lbl_ayuda.pack(side=tk.BOTTOM, fill=tk.X)

    def inicializar_grafico(self):
        self.fig = Figure(figsize=(8, 7), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.fig.suptitle("Superposición de Funciones: Lineales vs Cuadrática", fontsize=14, fontweight="bold")
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.panel_derecho)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.panel_derecho)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def cargar_valores_defecto(self):
        # Valores iniciales: (1x - 2) y (1x + 3) -> Resultado: x^2 + x - 6
        self.txt_m1.insert(0, "1")
        self.txt_b1.insert(0, "-2")
        self.txt_m2.insert(0, "1")
        self.txt_b2.insert(0, "3")
        self.procesar_y_graficar()

    def formatear_lineal(self, m, b, nombre="f"):
        """Formatea estéticamente la ecuación de la recta."""
        if m == 0:
            return f"{nombre}(x) = {b:.2f}"
        
        part_m = f"{m:.2f}x" if m != 1 else "x"
        part_m = f"-x" if m == -1 else part_m
        
        if b > 0:
            return f"{nombre}(x) = {part_m} + {b:.2f}"
        elif b < 0:
            return f"{nombre}(x) = {part_m} - {abs(b):.2f}"
        else:
            return f"{nombre}(x) = {part_m}"

    def formatear_cuadratica(self, a, b, c):
        """Formatea estéticamente la ecuación de la parábola ax^2 + bx + c."""
        # Término cuadrático
        if a == 1: part_a = "x²"
        elif a == -1: part_a = "-x²"
        elif a == 0: part_a = ""
        else: part_a = f"{a:.2f}x²"

        # Término lineal
        if b > 0: part_b = f" + {b:.2f}x" if b != 1 else " + x"
        elif b < 0: part_b = f" - {abs(b):.2f}x" if b != -1 else " - x"
        else: part_b = ""

        # Término independiente
        if c > 0: part_c = f" + {c:.2f}"
        elif c < 0: part_c = f" - {abs(c):.2f}"
        else: part_c = ""

        eq = f"h(x) = {part_a}{part_b}{part_c}"
        return eq if eq != "h(x) = " else "h(x) = 0"

    def procesar_y_graficar(self):
        try:
            # Obtener y validar coeficientes numéricos
            m1 = float(self.txt_m1.get())
            b1 = float(self.txt_b1.get())
            m2 = float(self.txt_m2.get())
            b2 = float(self.txt_b2.get())
        except ValueError:
            messagebox.showerror("Error de entrada", "Por favor introduce únicamente números válidos en los coeficientes.")
            return

        # 1. Calcular los coeficientes de la cuadrática mediante propiedad distributiva:
        # (m1*x + b1) * (m2*x + b2) = (m1*m2)x² + (m1*b2 + b1*m2)x + (b1*b2)
        a = m1 * m2
        b = (m1 * b2) + (b1 * m2)
        c = b1 * b2

        # 2. Actualizar las etiquetas de texto de la interfaz con formato limpio
        self.lbl_eq1.config(text=self.formatear_lineal(m1, b1, "f"))
        self.lbl_eq2.config(text=self.formatear_lineal(m2, b2, "g"))
        self.lbl_eq_cuad.config(text=self.formatear_cuadratica(a, b, c))

        # 3. Preparar el gráfico
        self.ax.clear()

        # Definir un rango dinámico inteligente en X para que siempre se aprecien las raíces
        raices = []
        if m1 != 0: raices.append(-b1/m1)
        if m2 != 0: raices.append(-b2/m2)
        
        if raices:
            min_x, max_x = min(raices) - 4, max(raices) + 4
        else:
            min_x, max_x = -10, 10

        x = np.linspace(min_x, max_x, 500)

        # Calcular curvas
        y_f1 = m1 * x + b1
        y_f2 = m2 * x + b2
        y_cuad = a * x**2 + b * x + c

        # Dibujar líneas en Matplotlib
        self.ax.plot(x, y_f1, label="f(x) Lineal 1", color="#1f77b4", linestyle="--", linewidth=2.5)
        self.ax.plot(x, y_f2, label="g(x) Lineal 2", color="#ff7f0e", linestyle="--", linewidth=2.5)
        self.ax.plot(x, y_cuad, label="h(x) Cuadrática (Producto)", color="#2ca02c", linewidth=2.5)

        # Dibujar los ejes cartesianos de referencia (X e Y)
        self.ax.axhline(0, color="black", linewidth=1, alpha=0.7)
        self.ax.axvline(0, color="black", linewidth=1, alpha=0.7)

        # Resaltar las raíces (intersecciones con el eje X) para reforzar el concepto pedagógico
        for raiz in raices:
            self.ax.scatter(raiz, 0, color="red", s=50, zorder=5)

        # Configuración estética del gráfico
        self.ax.set_title("Intersección y Comportamiento de las Funciones", fontsize=11)
        self.ax.grid(True, linestyle=":", alpha=0.6)
        self.ax.legend(loc="best", fontsize=10)
        
        # Redibujar el lienzo
        self.fig.tight_layout()
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = AppProductoLineal(root)
    root.mainloop()