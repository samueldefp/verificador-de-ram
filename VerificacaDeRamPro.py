import customtkinter as ctk
import psutil

# --- CONFIGURAÇÃO DA JANELA ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# oi

class MonitorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações iniciais da janela
        self.title("Monitor de Sistema Pro")
        self.geometry("500x400")
        self.resizable(True, True)

        # --- LAYOUT (INTERFACE) ---
        
        # Título Principal
        self.lbl_titulo = ctk.CTkLabel(self, text="MONITOR DE HARDWARE", font=("Roboto", 20, "bold"))
        self.lbl_titulo.pack(pady=20)

        # 1. Seção CPU
        self.lbl_cpu = ctk.CTkLabel(self, text="CPU: 0%", font=("Roboto", 14))
        self.lbl_cpu.pack(pady=5)
        
        self.barra_cpu = ctk.CTkProgressBar(self, width=300, height=15)
        self.barra_cpu.pack(pady=5)
        self.barra_cpu.set(0)

        # Divisória visual
        self.linha = ctk.CTkFrame(self, height=2, width=300)
        self.linha.pack(pady=20)

        # 2. Seção RAM
        self.lbl_ram = ctk.CTkLabel(self, text="RAM: 0 GB / 0 GB", font=("Roboto", 14))
        self.lbl_ram.pack(pady=5)

        # Defini a cor inicial como verde ("green") explicitamente
        self.barra_ram = ctk.CTkProgressBar(self, width=300, height=15, progress_color="green")
        self.barra_ram.pack(pady=5)
        self.barra_ram.set(0)

        # --- INICIA O LOOP DE ATUALIZAÇÃO ---
        self.atualizar_dados()

    def atualizar_dados(self):
        # 1. Pega dados da CPU
        cpu_percent = psutil.cpu_percent(interval=None)
        
        # 2. Pega dados da RAM
        memoria = psutil.virtual_memory()
        ram_usada_gb = memoria.used / (1024**3)
        ram_total_gb = memoria.total / (1024**3)
        ram_percent = memoria.percent

        # 3. Atualiza os textos na tela
        self.lbl_cpu.configure(text=f"CPU: {cpu_percent:.1f}%")
        self.lbl_ram.configure(text=f"RAM: {ram_usada_gb:.1f} GB / {ram_total_gb:.1f} GB ({ram_percent}%)")

        # 4. Atualiza as barras (Valor entre 0.0 e 1.0)
        self.barra_cpu.set(cpu_percent / 100)
        self.barra_ram.set(ram_percent / 100)

        # --- LÓGICA DE COR DINÂMICA (CPU) ---
        if cpu_percent > 80:
            self.barra_cpu.configure(progress_color="red")
        else:
            self.barra_cpu.configure(progress_color="#1f6aa5") # Azul padrão do tema

        # --- LÓGICA DE COR DINÂMICA (RAM) - AQUI ESTÁ O SEU PEDIDO ---
        if ram_percent > 80:
            self.barra_ram.configure(progress_color="red")
        else:
            self.barra_ram.configure(progress_color="green") # Verde padrão

        # 5. Loop (Recursividade)
        self.after(3000, self.atualizar_dados)

if __name__ == "__main__":
    app = MonitorApp()
    app.mainloop()