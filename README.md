![GitHub repo size](https://img.shields.io/github/repo-size/pixelctechia/DownVideos)
![Python](https://img.shields.io/badge/Python-3.6+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

**DownVideos** é uma aplicação em Python com interface gráfica (GUI) projetada para baixar vídeos de plataformas como YouTube, Instagram e TikTok na melhor qualidade disponível e converter vídeos locais para o formato MP3. Desenvolvido com `tkinter` para a interface, `yt_dlp` para downloads e `moviepy` para conversão de áudio, este projeto foi criado com propósitos **didáticos** e não deve ser utilizado para fins comerciais.

> **Nota Importante**: Este script é destinado exclusivamente a fins educacionais. O uso para baixar vídeos é de total responsabilidade do usuário, respeitando os direitos autorais e os termos de serviço das plataformas.

## Funcionalidades

- **Download de Vídeos**: Baixe vídeos do YouTube, Instagram e TikTok inserindo a URL e escolhendo uma pasta de destino.
- **Conversão para MP3**: Transforme arquivos de vídeo locais (MP4, MKV, AVI, etc.) em áudio MP3.
- **Interface Simples**: GUI intuitiva com barra de progresso para acompanhar o download.
- **Feedback em Tempo Real**: Status atualizado durante o processo, com mensagens de erro ou sucesso.

## Demonstração
*(Adicione um GIF ou screenshot aqui para mostrar a interface em ação!)*  
<!-- Exemplo: ![Demo](docs/demo.gif) -->

## Requisitos

- **Python**: 3.6 ou superior
- **Dependências**:
  - `tkinter` (incluso no Python)
  - `yt_dlp` - Para downloads
  - `moviepy` - Para conversão
  - `ffmpeg` - Necessário para manipulação de áudio/vídeo

### Instalação das Dependências
```bash
pip install yt-dlp moviepy
```
 Instale o `ffmpeg`:
- **Windows**: Baixe em [ffmpeg.org](https://ffmpeg.org) e adicione ao PATH.
- **Linux**: `sudo apt-get install ffmpeg`
- **macOS**: `brew install ffmpeg`

## Como Usar

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/pixelctechia/DownVideos.git
   cd DownVideos
   ```

2. **Execute o Script**:
   ```bash
   python downvideos.py
   ```

3. **Na Interface**:
   - **Download**: Insira a URL (YouTube, Instagram ou TikTok), selecione a pasta e clique em "Baixar Vídeo".
   - **Conversão**: Escolha um vídeo local e clique em "Converter Selecionado para MP3".

## Exemplo de Uso

- **Download**: URL `https://www.youtube.com/watch?v=example` → Salva como `Título do Vídeo.mp4`.
- **Conversão**: Selecione `meu_video.mp4` → Gera `meu_video.mp3`.

## Estrutura do Projeto

- `downvideos.py`: Script principal com a lógica de download e conversão.
- `README.md`: Este arquivo.
- `requirements.txt`: Lista de dependências.
- `LICENSE`: Licença MIT.

## Limitações

- Requer internet para downloads.
- Conversão depende de áudio presente no vídeo.
- Formatos suportados variam conforme `ffmpeg` e `yt_dlp`.

## Aviso Legal

Este projeto é **didático**. O download de vídeos deve respeitar os termos das plataformas e leis de direitos autorais. A responsabilidade é do usuário.

## Como Contribuir

1. Faça um fork deste repositório.
2. Crie uma branch: `git checkout -b minha-melhoria`.
3. Commit suas mudanças: `git commit -m "Adicionei X"`.
4. Envie um pull request: `git push origin minha-melhoria`.

**Ideias**:
- Suporte a mais plataformas.
- Opções de qualidade de download.
- Melhorias na interface.

## Comunidade

- ⭐ Dê uma estrela se gostar do projeto!
- Abra um [issue](https://github.com/pixelctechia/DownVideos/issues) para sugestões ou bugs.

## Licença

Licenciado sob a [MIT License](LICENSE).

---

**Feito com ❤️ por [pixelctechia](https://github.com/pixelctechia)**  
```

---

### Como Usar Este README
1. Abra o GitHub Desktop e navegue até `D:\02-PROJETOS_CODE\DownVideos`.
2. Abra o arquivo `README.md` em um editor de texto (como Bloco de Notas ou VS Code).
3. Copie e cole o conteúdo acima.
4. Salve o arquivo.
5. No GitHub Desktop:
   - Veja as mudanças na aba **Changes**.
   - Digite uma mensagem de commit (ex.: "Atualizando README") e clique em **Commit to main**.
   - Clique em **Push origin** para enviar ao GitHub.

---

### Por Que Esse README é Bom?
- **Badges**: Mostram o tamanho do repositório, linguagem e licença, dando um toque profissional.
- **Estrutura Clara**: Seções organizadas facilitam a leitura.
- **Convite à Colaboração**: Inclui instruções simples para contribuir e ideias específicas.
- **Visibilidade**: Palavras-chave como "YouTube", "TikTok", "MP3" ajudam nas buscas.
- **Demonstração**: Espaço para um GIF (adicione depois, se quiser!).
