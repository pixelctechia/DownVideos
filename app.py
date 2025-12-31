import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import threading
from core import baixar_video_core, converter_para_mp3_core, is_valid_url

# Constantes de Interface
SUPPORTED_VIDEO_FORMATS = [
    ("Arquivos de Vídeo", "*.mp4 *.mkv *.avi *.mov *.flv *.webm *.m4v"),
    ("Todos os Arquivos", "*.*")
]
WINDOW_MIN_WIDTH = 500
WINDOW_MIN_HEIGHT = 400

# Variáveis globais para caminhos
selected_video_file_path = None 

def mostrar_processando():
    root.config(cursor="wait")
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Button):
            widget.config(state='disabled')

def restaurar_interface():
    root.config(cursor="")
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Button):
            widget.config(state='normal')

def limpar_campos():
    entrada_url.set("")
    progress_bar['value'] = 0
    status.set("")
    root.update_idletasks()

def selecionar_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        caminho_destino.set(pasta)

def atualizar_progresso(d):
    """Callback para o yt-dlp via core."""
    if d['status'] == 'downloading':
        tamanho_total = d.get('total_bytes', 0)
        baixado = d.get('downloaded_bytes', 0)
        if tamanho_total > 0:
            progresso = int((baixado / tamanho_total) * 100)
            progress_bar['value'] = progresso
            status.set(f"Baixando: {progresso}%")
            root.update_idletasks()

def baixar_video_wrapper():
    """Wrapper para chamar o core sem travar a UI."""
    url = entrada_url.get()
    destino = caminho_destino.get()

    if not url.strip() or not is_valid_url(url):
        messagebox.showwarning("Aviso", "Por favor, insira uma URL válida.")
        return

    if not destino.strip():
        messagebox.showwarning("Aviso", "Selecione uma pasta de destino.")
        return

    mostrar_processando()
    try:
        status.set("Iniciando download...")
        root.update_idletasks()
        
        # Chama a lógica centralizada
        arquivo = baixar_video_core(url, destino, atualizar_progresso)
        
        status.set("Download concluído!")
        messagebox.showinfo("Sucesso", f"Download concluído:\n{os.path.basename(arquivo)}")
        limpar_campos()
    except Exception as e:
        status.set("Erro no download.")
        messagebox.showerror("Erro", str(e))
    finally:
        restaurar_interface()

def escolher_video_para_converter():
    global selected_video_file_path
    selected_video_file_path = filedialog.askopenfilename(filetypes=SUPPORTED_VIDEO_FORMATS)
    if selected_video_file_path:
        status.set(f"Selecionado: {os.path.basename(selected_video_file_path)}")

def converter_wrapper():
    global selected_video_file_path
    if not selected_video_file_path or not os.path.exists(selected_video_file_path):
        messagebox.showwarning("Aviso", "Selecione um vídeo válido.")
        return

    mostrar_processando()
    try:
        status.set("Convertendo...")
        root.update_idletasks()
        
        # Chama a lógica centralizada
        mp3_path = converter_para_mp3_core(selected_video_file_path)
        
        status.set("Conversão concluída!")
        messagebox.showinfo("Sucesso", f"MP3 gerado:\n{mp3_path}")
    except Exception as e:
        status.set("Erro na conversão.")
        messagebox.showerror("Erro", str(e))
    finally:
        restaurar_interface()

# GUI Setup (Mesmo layout, chamando novos wrappers com Threads)
root = tk.Tk()
root.title("DownVideos - Desktop")
root.minsize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)

entrada_url = tk.StringVar()
caminho_destino = tk.StringVar()
status = tk.StringVar()

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)
frame.columnconfigure(0, weight=1)

tk.Label(frame, text="URL do Vídeo do YouTube:").grid(row=0, column=0, sticky="w")
tk.Entry(frame, textvariable=entrada_url).grid(row=1, column=0, columnspan=2, pady=5, sticky="we")

tk.Label(frame, text="Pasta de Destino:").grid(row=2, column=0, sticky="w")
tk.Entry(frame, textvariable=caminho_destino).grid(row=3, column=0, pady=5, sticky="we")
tk.Button(frame, text="Selecionar Pasta", command=selecionar_pasta).grid(row=3, column=1, padx=5)

tk.Button(frame, text="BAIXAR VÍDEO", bg="#4CAF50", fg="white", 
          command=lambda: threading.Thread(target=baixar_video_wrapper, daemon=True).start()
).grid(row=4, column=0, columnspan=2, pady=10, sticky="we")

progress_bar = ttk.Progressbar(frame, orient="horizontal", mode="determinate")
progress_bar.grid(row=5, column=0, columnspan=2, pady=10, sticky="we")

tk.Label(frame, text="Conversão Local:").grid(row=6, column=0, sticky="w", pady=(10,0))
tk.Button(frame, text="Escolher Vídeo", bg="#FF9800", fg="white", command=escolher_video_para_converter).grid(row=7, column=0, pady=5, sticky="we")
tk.Button(frame, text="CONVERTER PARA MP3", bg="#2196F3", fg="white", 
          command=lambda: threading.Thread(target=converter_wrapper, daemon=True).start()
).grid(row=7, column=1, pady=5, padx=5, sticky="we")

tk.Label(frame, textvariable=status, fg="blue").grid(row=8, column=0, columnspan=2, pady=5)

if __name__ == "__main__":
    root.mainloop()
