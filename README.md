# DownVideos

**DownVideos** é uma aplicação em Python com interface gráfica (GUI) projetada para baixar vídeos de plataformas como YouTube, Instagram e TikTok na melhor qualidade disponível e converter vídeos locais para o formato MP3. Desenvolvido com **tkinter** para a interface, **yt_dlp** para downloads e **moviepy** para conversão de áudio, este projeto foi criado com propósitos **didáticos** e não deve ser utilizado para fins comerciais.

> **Nota Importante** : Este script é destinado exclusivamente a fins educacionais. O uso para baixar vídeos é de total responsabilidade do usuário, respeitando os direitos autorais e os termos de serviço das plataformas.

## Funcionalidades

* **Download de Vídeos** : Baixe vídeos do YouTube, Instagram e TikTok inserindo a URL e escolhendo uma pasta de destino. A biblioteca **yt_dlp** suporta múltiplas plataformas e busca a melhor qualidade disponível.
* **Conversão de Vídeos Locais para MP3** : Converta arquivos de vídeo locais (como MP4, MKV, AVI, etc.) em áudio MP3 utilizando **moviepy**.
* **Interface Intuitiva** : Interface gráfica simples desenvolvida com **tkinter**, com barra de progresso para acompanhar o download.
* **Feedback em Tempo Real** : Exibe status atualizado durante o download e conversão, com mensagens de erro ou sucesso.

## Requisitos

Para executar o **DownVideos**, você precisará das seguintes dependências:

* Python 3.6 ou superior
* Bibliotecas Python:

  * **tkinter** (geralmente incluído com o Python)
  * **yt_dlp** - Para baixar vídeos das plataformas suportadas
  * **moviepy** - Para converter vídeos em MP3
  * **ffmpeg** (necessário pelo **moviepy** para manipulação de áudio/vídeo)

### Instalação das Dependências

**bash**

AjusteCopiar

`<span>pip install yt-dlp moviepy</span>`

Instale o **ffmpeg** no seu sistema:

* **Windows** : Baixe do site oficial e adicione ao PATH.
* **Linux** : **sudo apt-get install ffmpeg**
* **macOS** : **brew install ffmpeg**

## Como Usar

1. **Clone o Repositório** :
   **bash**

   AjusteCopiar

   `<span>git </span><span>clone</span><span> https://github.com/seu-usuario/DownVideos.git    </span><span></span><span>cd</span><span> DownVideos</span>`

1. **Execute o Script** :
   **bash**

   AjusteCopiar

   `<span>python downvideos.py</span>`

1. **Funcionalidades na Interface** :

* **Download de Vídeo** :
  * Insira a URL de um vídeo do YouTube, Instagram ou TikTok no campo "URL do Vídeo".

    * Clique em "Selecionar Pasta" para escolher o destino.

    * Clique em "Baixar Vídeo" e acompanhe o progresso na barra.

* **Conversão para MP3** :
  * Clique em "Escolher Vídeo" para selecionar um arquivo de vídeo local.

    * Clique em "Converter Selecionado para MP3" para gerar o arquivo MP3 no mesmo diretório do vídeo.

## Estrutura do Código

* **selecionar_pasta()** : Escolhe o diretório de destino para o download.
* **atualizar_progresso(d)** : Atualiza a barra de progresso com base nos dados do **yt_dlp**.
* **baixar_video()** : Realiza o download usando **yt_dlp** e salva no local especificado.
* **escolher_video_para_converter()** : Abre um diálogo para selecionar um vídeo local.
* **converter_video_local_para_mp3()** : Converte o vídeo selecionado em MP3 com **moviepy**.
* Interface **tkinter** organizada em seções para download e conversão.

## Exemplo de Uso

* **Download** : Insira **https://www.youtube.com/watch?v=example**, **https://www.instagram.com/p/example/** ou **https://www.tiktok.com/@user/video/example** e escolha uma pasta. O vídeo será salvo como **Título do Vídeo.mp4**.
* **Conversão** : Selecione um arquivo como **meu_video.mp4** e clique em "Converter". O resultado será **meu_video.mp3**.

## Limitações

* Requer conexão à internet para downloads.
* A conversão para MP3 exige que o vídeo tenha uma faixa de áudio válida.
* Suporte a formatos depende do **ffmpeg** e das plataformas configuradas no **yt_dlp**.

## Aviso Legal

Este projeto foi desenvolvido para fins  **didáticos e educacionais** . O download de vídeos de plataformas como YouTube, Instagram e TikTok deve respeitar os termos de uso dessas plataformas e as leis de direitos autorais aplicáveis. A responsabilidade pelo uso do script e pelos arquivos baixados é exclusivamente do usuário.

## Contribuições

Contribuições são bem-vindas! Abra issues ou pull requests para melhorias, como suporte a mais plataformas, ajustes na interface ou novas funcionalidades.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
