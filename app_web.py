import streamlit as st
import os
from core import baixar_video_core, converter_para_mp3_core, is_valid_url

st.set_page_config(page_title="DownVideos Web", page_icon="🎥", layout="centered")

# Estilo Premium
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎥 DownVideos Web")
st.subheader("Download de vídeos e conversão para MP3 de forma simples.")

tab1, tab2 = st.tabs(["📥 Download", "🎵 Converter Local"])

with tab1:
    url = st.text_input("URL do Vídeo do YouTube:")
    # No Streamlit, lidamos com diretórios de forma diferente, 
    # por padrão vamos usar a pasta de downloads do usuário ou a atual.
    destino = st.text_input("Pasta de Destino:", value=os.getcwd())
    
    if st.button("Baixar Agora"):
        if is_valid_url(url):
            try:
                with st.spinner('Baixando...'):
                    # Hook simples para o Streamlit
                    def hook(d):
                        if d['status'] == 'downloading':
                            pass
                    
                    arquivo = baixar_video_core(url, destino, hook)
                    st.success(f"Vídeo baixado com sucesso: {arquivo}")
            except Exception as e:
                st.error(f"Erro: {e}")
        else:
            st.warning("Insira uma URL válida.")

with tab2:
    arquivo_upload = st.file_uploader("Escolha um vídeo para extrair o áudio", type=["mp4", "mkv", "avi", "mov"])
    
    if arquivo_upload is not None:
        # Salva o arquivo temporariamente para processar
        temp_path = os.path.join(os.getcwd(), arquivo_upload.name)
        with open(temp_path, "wb") as f:
            f.write(arquivo_upload.getbuffer())
            
        if st.button("Converter para MP3"):
            try:
                with st.spinner('Convertendo...'):
                    mp3_p = converter_para_mp3_core(temp_path)
                    st.success(f"MP3 Gerado!")
                    with open(mp3_p, "rb") as file:
                        st.download_button(label="Baixar MP3", data=file, file_name=os.path.basename(mp3_p))
            except Exception as e:
                st.error(f"Erro: {e}")
            finally:
                # Opcional: remover o vídeo temporário
                pass
