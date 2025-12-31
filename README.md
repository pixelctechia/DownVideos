# DownVideos - Download de Vídeos e Conversor MP3 🎥🎵

Uma ferramenta simples, gratuita e poderosa desenvolvida em Python para baixar vídeos do YouTube (incluindo Shorts) na melhor qualidade disponível e converter arquivos de vídeo locais para o formato MP3.

---

## ✨ Funcionalidades

- **Download de Vídeos:** Baixa vídeos do YouTube utilizando o motor robusto do `yt-dlp`.
- **Qualidade Superior:** Seleção automática dos melhores fluxos de áudio e vídeo disponíveis.
- **Conversão Local:** Transforma qualquer arquivo de vídeo local (.mp4, .mkv, .avi, etc.) em MP3 com um clique.
- **Interface Intuitiva:** Interface gráfica (GUI) amigável construída com Tkinter.
- **Não Trava:** Utiliza *Threading* para garantir que a interface continue respondendo durante o processamento.
- **Grátis e Ilimitado:** Sem taxas, sem limites de uso.

---

## 📋 Requisitos do Sistema

Antes de começar, você precisará ter instalado:
1. **Python 3.8 ou superior**: [Download Python](https://www.python.org/downloads/)
2. **FFmpeg**: Essencial para a fusão de áudio/vídeo e conversão de formatos.
   - [Guia de instalação do FFmpeg](https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg)

---

## 🚀 Instalação e Dependências

Siga os passos abaixo para rodar o projeto localmente:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/pixelctechia/DownVideos.git
   cd DownVideos
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # No Windows
   source .venv/bin/activate  # No Linux/Mac
   ```

3. **Instale as bibliotecas necessárias:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠️ Como Usar

### Para Baixar Vídeos:
1. Execute o aplicativo: `python app.py`.
2. Cole a **URL do vídeo** no campo indicado.
3. Clique em **Selecionar Pasta** para escolher onde o vídeo será salvo.
4. Clique em **Baixar Vídeo**.

### Para Converter Vídeo Local para MP3:
1. Clique em **Escolher Vídeo** e selecione um arquivo no seu computador.
2. Clique em **Converter para MP3**. O arquivo será salvo na mesma pasta do vídeo original.

---

## 📂 Estrutura do Projeto

```text
DownVideos/
├── app.py              # Código fonte principal (Interface e Lógica)
├── requirements.txt    # Lista de dependências do projeto
├── README.md           # Documentação do projeto
└── LICENSE             # Licença de uso (MIT)
```

---

## ⚠️ Aviso Legal

Este projeto foi desenvolvido para fins estritamente **educacionais**. O uso desta ferramenta para baixar conteúdo protegido por direitos autorais sem permissão pode violar os Termos de Serviço do YouTube e as leis de propriedade intelectual. Use com responsabilidade.

---

## 🤝 Como Contribuir

1. Faça um **Fork** do projeto.
2. Crie uma **Branch** para sua melhoria (`git checkout -b feature/minha-melhoria`).
3. Faça o **Commit** das suas alterações (`git commit -m "Adicionei X funcionalidade"`).
4. Envie para o GitHub (**Push**) (`git push origin feature/minha-melhoria`).
5. Abra um **Pull Request**.

---

## ⚖️ Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido por [Pixel C Tech](https://github.com/pixelctechia) 🚀
