import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import yt_dlp
import os
from moviepy.editor import VideoFileClip

# Variáveis globais para caminhos
downloaded_file_path = None    # Caminho do vídeo recém-baixado
selected_video_file_path = None  # Caminho do vídeo escolhido localmente para conversão

def selecionar_pasta():
    """Seleciona a pasta de destino para o download."""
    pasta = filedialog.askdirectory()
    if pasta:
        caminho_destino.set(pasta)

def atualizar_progresso(d):
    """Atualiza a barra de progresso durante o download."""
    if d['status'] == 'downloading':
        tamanho_total = d.get('total_bytes', 0)
        baixado = d.get('downloaded_bytes', 0)
        if tamanho_total > 0:
            progresso = int((baixado / tamanho_total) * 100)
            progress_bar['value'] = progresso
            status.set(f"Baixando: {progresso}%")
            root.update_idletasks()

def baixar_video():
    """Baixa o vídeo do YouTube na melhor qualidade disponível."""
    global downloaded_file_path

    url = entrada_url.get()
    destino = caminho_destino.get()
    
    if not url.strip():
        messagebox.showwarning("Aviso", "Por favor, insira a URL do vídeo.")
        return
    if not destino.strip():
        messagebox.showwarning("Aviso", "Por favor, selecione uma pasta de destino.")
        return

    try:
        # Reseta o progresso e status
        progress_bar['value'] = 0
        status.set("Iniciando download...")
        root.update_idletasks()

        # Opções para o yt_dlp
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(destino, '%(title)s.%(ext)s'),
            'progress_hooks': [atualizar_progresso],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get("title", "video_sem_titulo")
            ext = info_dict.get("ext", "mp4")
            downloaded_file_path = os.path.join(destino, f"{title}.{ext}")

        status.set("Download concluído!")
        messagebox.showinfo("Sucesso", "Download concluído!")
    except Exception as e:
        status.set("")
        messagebox.showerror("Erro", f"Ocorreu um erro ao baixar o vídeo:\n{e}")

def escolher_video_para_converter():
    """Abre uma janela para selecionar um arquivo de vídeo local para conversão."""
    global selected_video_file_path
    # Filtra pelos formatos de vídeo mais comuns (ajuste conforme necessidade)
    tipos_video = [
        ("Arquivos de Vídeo", "*.mp4 *.mkv *.avi *.mov *.flv *.webm *.m4v"),
        ("Todos os Arquivos", "*.*")
    ]
    selected_video_file_path = filedialog.askopenfilename(filetypes=tipos_video)
    if selected_video_file_path:
        status.set(f"Vídeo selecionado: {os.path.basename(selected_video_file_path)}")
    else:
        status.set("Nenhum vídeo selecionado.")

def converter_video_local_para_mp3():
    """Converte para MP3 o vídeo selecionado localmente."""
    global selected_video_file_path

    if not selected_video_file_path or not os.path.exists(selected_video_file_path):
        messagebox.showwarning("Aviso", "Nenhum vídeo foi selecionado ou o arquivo não existe.")
        return

    try:
        status.set("Convertendo para MP3...")
        root.update_idletasks()

        # Constrói o caminho de saída (mesmo nome, mas extensão .mp3)
        base, _ = os.path.splitext(selected_video_file_path)
        mp3_path = base + ".mp3"

        video = VideoFileClip(selected_video_file_path)
        if not video.audio:
            raise ValueError("O vídeo selecionado não contém faixa de áudio.")
        
        # Extrai o áudio para MP3
        video.audio.write_audiofile(mp3_path)
        video.close()

        status.set("Conversão concluída!")
        messagebox.showinfo("Sucesso", f"Arquivo MP3 gerado em:\n{mp3_path}")
    except ValueError as ve:
        status.set("")
        messagebox.showerror("Erro", f"{ve}")
    except Exception as e:
        status.set("")
        messagebox.showerror("Erro", f"Ocorreu um erro ao converter o vídeo em MP3:\n{e}")

# =============================================
# CONFIGURAÇÃO DA JANELA PRINCIPAL (tkinter)
# =============================================

root = tk.Tk()
root.title("YouTube Downloader + Conversor MP3")

# Variáveis de interface
entrada_url = tk.StringVar()
caminho_destino = tk.StringVar()
status = tk.StringVar()

# Frame principal
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

# 1) Seção de Download de Vídeo
label_url = tk.Label(frame, text="URL do Vídeo do YouTube:")
label_url.grid(row=0, column=0, sticky="w")

entry_url = tk.Entry(frame, textvariable=entrada_url, width=50)
entry_url.grid(row=1, column=0, columnspan=2, pady=5, sticky="we")

label_destino = tk.Label(frame, text="Pasta de Destino (para Download):")
label_destino.grid(row=2, column=0, sticky="w")

entry_destino = tk.Entry(frame, textvariable=caminho_destino, width=40)
entry_destino.grid(row=3, column=0, pady=5, sticky="we")

btn_selecionar_pasta = tk.Button(frame, text="Selecionar Pasta", command=selecionar_pasta)
btn_selecionar_pasta.grid(row=3, column=1, padx=5)

btn_baixar = tk.Button(frame, text="Baixar Vídeo", command=baixar_video, bg="#4CAF50", fg="white")
btn_baixar.grid(row=4, column=0, columnspan=2, pady=10, sticky="we")

# Barra de progresso do download
progress_bar = ttk.Progressbar(frame, orient="horizontal", length=400, mode="determinate")
progress_bar.grid(row=5, column=0, columnspan=2, pady=10)

# 2) Seção de Conversão de Vídeo Local para MP3
label_convert = tk.Label(frame, text="Conversão de Vídeo Local para MP3:")
label_convert.grid(row=6, column=0, sticky="w", pady=(10,0))

btn_escolher_video = tk.Button(frame, text="Escolher Vídeo", command=escolher_video_para_converter, bg="#FF9800", fg="white")
btn_escolher_video.grid(row=7, column=0, pady=5, sticky="we")

btn_converter_local = tk.Button(frame, text="Converter Selecionado para MP3", command=converter_video_local_para_mp3, bg="#2196F3", fg="white")
btn_converter_local.grid(row=7, column=1, pady=5, sticky="we")

# 3) Status
label_status = tk.Label(frame, textvariable=status, fg="blue")
label_status.grid(row=8, column=0, columnspan=2, pady=5)

root.mainloop()
