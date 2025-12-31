"""
Requisitos:
pip install yt-dlp
pip install moviepy
pip install tkinter (geralmente já vem com Python)
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import yt_dlp
import os
import threading
from moviepy.editor import VideoFileClip

# Constantes
SUPPORTED_VIDEO_FORMATS = [
    ("Arquivos de Vídeo", "*.mp4 *.mkv *.avi *.mov *.flv *.webm *.m4v"),
    ("Todos os Arquivos", "*.*")
]
DEFAULT_DOWNLOAD_FORMAT = 'bestvideo+bestaudio/best'
WINDOW_MIN_WIDTH = 500
WINDOW_MIN_HEIGHT = 400

# Variáveis globais para caminhos
downloaded_file_path = None    # Caminho do vídeo recém-baixado
selected_video_file_path = None  # Caminho do vídeo escolhido localmente para conversão

def is_valid_url(url):
    """
    Verifica se a URL parece ser válida (começa com http:// ou https://).

    Args:
        url (str): URL a ser verificada

    Returns:
        bool: True se a URL parece válida, False caso contrário
    """
    return url.strip().startswith(('http://', 'https://'))

def mostrar_processando():
    """Configura a interface para mostrar estado de processamento."""
    root.config(cursor="wait")
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Button):
            widget.config(state='disabled')

def restaurar_interface():
    """Restaura a interface ao estado normal após processamento."""
    root.config(cursor="")
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Button):
            widget.config(state='normal')

def limpar_campos():
    """Limpa os campos e reseta o estado da interface."""
    entrada_url.set("")
    progress_bar['value'] = 0
    status.set("")
    root.update_idletasks()

def selecionar_pasta():
    """
    Seleciona a pasta de destino para o download.
    Abre um diálogo para seleção de pasta e atualiza o campo de destino.
    """
    pasta = filedialog.askdirectory()
    if pasta:
        caminho_destino.set(pasta)

def atualizar_progresso(d):
    """
    Atualiza a barra de progresso durante o download.

    Args:
        d (dict): Dicionário com informações do progresso do download
    """
    if d['status'] == 'downloading':
        tamanho_total = d.get('total_bytes', 0)
        baixado = d.get('downloaded_bytes', 0)
        if tamanho_total > 0:
            progresso = int((baixado / tamanho_total) * 100)
            progress_bar['value'] = progresso
            status.set(f"Baixando: {progresso}%")
            root.update_idletasks()

def baixar_video():
    """
    Baixa um vídeo do YouTube na melhor qualidade disponível.
    Verifica a URL e a pasta de destino antes de iniciar o download.
    Atualiza a barra de progresso durante o download.
    """
    global downloaded_file_path

    url = entrada_url.get()
    destino = caminho_destino.get()

    if not url.strip():
        messagebox.showwarning("Aviso", "Por favor, insira a URL do vídeo.")
        return

    if not is_valid_url(url):
        messagebox.showwarning("Aviso", "Por favor, insira uma URL válida do YouTube.")
        return

    if not destino.strip():
        messagebox.showwarning("Aviso", "Por favor, selecione uma pasta de destino.")
        return

    mostrar_processando()
    try:
        # Reseta o progresso e status
        progress_bar['value'] = 0
        status.set("Iniciando download...")
        root.update_idletasks()

        # Opções para o yt_dlp
        ydl_opts = {
            'format': DEFAULT_DOWNLOAD_FORMAT,
            'outtmpl': os.path.join(destino, '%(title)s.%(ext)s'),
            'progress_hooks': [atualizar_progresso],
            'nocheckcertificate': True,
            'ignoreerrors': False,
            'logtostderr': False,
            'quiet': True,
            'no_warnings': True,
            'default_search': 'auto',
            'source_address': '0.0.0.0'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get("title", "video_sem_titulo")
            ext = info_dict.get("ext", "mp4")
            downloaded_file_path = os.path.join(destino, f"{title}.{ext}")

        status.set("Download concluído!")
        messagebox.showinfo("Sucesso", "Download concluído!")
        limpar_campos()
    except Exception as e:
        status.set("")
        messagebox.showerror("Erro", f"Ocorreu um erro ao baixar o vídeo:\n{e}")
    finally:
        restaurar_interface()

def escolher_video_para_converter():
    """
    Abre uma janela para selecionar um arquivo de vídeo local para conversão.
    Atualiza o status com o nome do arquivo selecionado.
    """
    global selected_video_file_path
    selected_video_file_path = filedialog.askopenfilename(filetypes=SUPPORTED_VIDEO_FORMATS)
    if selected_video_file_path:
        status.set(f"Vídeo selecionado: {os.path.basename(selected_video_file_path)}")
    else:
        status.set("Nenhum vídeo selecionado.")

def converter_video_local_para_mp3():
    """
    Converte para MP3 o vídeo selecionado localmente.
    Verifica a existência do arquivo e da faixa de áudio antes da conversão.
    """
    global selected_video_file_path

    if not selected_video_file_path or not os.path.exists(selected_video_file_path):
        messagebox.showwarning("Aviso", "Nenhum vídeo foi selecionado ou o arquivo não existe.")
        return

    mostrar_processando()
    try:
        status.set("Convertendo para MP3...")
        root.update_idletasks()

        mp3_path = os.path.splitext(selected_video_file_path)[0] + ".mp3"

        with VideoFileClip(selected_video_file_path) as video:
            if not video.audio:
                raise ValueError("O vídeo selecionado não contém faixa de áudio.")
            video.audio.write_audiofile(mp3_path)

        status.set("Conversão concluída!")
        messagebox.showinfo("Sucesso", f"Arquivo MP3 gerado em:\n{mp3_path}")
    except ValueError as ve:
        status.set("")
        messagebox.showerror("Erro", f"{ve}")
    except Exception as e:
        status.set("")
        messagebox.showerror("Erro", f"Ocorreu um erro ao converter o vídeo em MP3:\n{e}")
    finally:
        restaurar_interface()

# =============================================
# CONFIGURAÇÃO DA JANELA PRINCIPAL (tkinter)
# =============================================

root = tk.Tk()
root.title("Video Downloader + Conversor MP3")
root.minsize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)

# Variáveis de interface
entrada_url = tk.StringVar()
caminho_destino = tk.StringVar()
status = tk.StringVar()

# Frame principal
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

# Configuração de peso das colunas
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=0)

# 1) Seção de Download de Vídeo
label_url = tk.Label(frame, text="Digite aqui a URL do Vídeo desejado:")
label_url.grid(row=0, column=0, sticky="w")

entry_url = tk.Entry(frame, textvariable=entrada_url, width=50)
entry_url.grid(row=1, column=0, columnspan=2, pady=5, sticky="we")

label_destino = tk.Label(frame, text="Pasta de Destino (para Download):")
label_destino.grid(row=2, column=0, sticky="w")

entry_destino = tk.Entry(frame, textvariable=caminho_destino, width=40)
entry_destino.grid(row=3, column=0, pady=5, sticky="we")

btn_selecionar_pasta = tk.Button(frame, text="Selecionar Pasta", command=selecionar_pasta)
btn_selecionar_pasta.grid(row=3, column=1, padx=5)

btn_baixar = tk.Button(frame, text="Baixar Vídeo", command=lambda: threading.Thread(target=baixar_video, daemon=True).start(), bg="#4CAF50", fg="white")
btn_baixar.grid(row=4, column=0, columnspan=2, pady=10, sticky="we")

# Barra de progresso do download
progress_bar = ttk.Progressbar(frame, orient="horizontal", length=400, mode="determinate")
progress_bar.grid(row=5, column=0, columnspan=2, pady=10, sticky="we")

# 2) Seção de Conversão de Vídeo Local para MP3
label_convert = tk.Label(frame, text="Conversão de Vídeo Local para MP3:")
label_convert.grid(row=6, column=0, sticky="w", pady=(10,0))

btn_escolher_video = tk.Button(frame, text="Escolher Vídeo", command=escolher_video_para_converter, bg="#FF9800", fg="white")
btn_escolher_video.grid(row=7, column=0, pady=5, sticky="we")

btn_converter_local = tk.Button(frame, text="Converter para MP3", command=converter_video_local_para_mp3, bg="#2196F3", fg="white")
btn_converter_local.grid(row=7, column=1, pady=5, padx=5, sticky="we")

# 3) Status
label_status = tk.Label(frame, textvariable=status, fg="blue", wraplength=400)
label_status.grid(row=8, column=0, columnspan=2, pady=5)

# Inicia o loop principal
root.mainloop()
