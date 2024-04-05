import streamlit as st
from pytube import YouTube

def baixar_video(url):
    youtube = YouTube(url)
    
    video_stream = youtube.streams.get_highest_resolution()
    
    video_stream.download()
    
    return "Download concluído!"

st.title('Baixador de Vídeos do YouTube')

video_url = st.text_input('Insira o link do vídeo do YouTube aqui:', '')

if st.button('Baixar Vídeo'):
    if video_url != '':
        with st.spinner('Baixando... Por favor, aguarde.'):
            mensagem = baixar_video(video_url)
            st.success(mensagem)
    else:
        st.error('Por favor, insira um link válido.')

