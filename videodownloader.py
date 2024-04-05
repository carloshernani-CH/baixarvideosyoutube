import streamlit as st
from pytube import YouTube, exceptions
from pathlib import Path
import re

def is_valid_youtube_url(url):
    # Simple check to see if the URL is a valid YouTube URL
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    youtube_pattern = re.compile(youtube_regex)
    match = youtube_pattern.match(url)
    return bool(match)

def baixar_video(url):
    try:
        youtube = YouTube(url)
        video_stream = youtube.streams.get_highest_resolution()
        downloads_path = str(Path.home() / "Downloads")
        video_stream.download(output_path=downloads_path)
        return "Download concluído!"
    except exceptions.VideoUnavailable:
        return "Erro: O vídeo está indisponível."
    except Exception as e:
        return f"Erro inesperado: {e}"

st.title('Baixador de Vídeos do YouTube')

video_url = st.text_input('Insira o link do vídeo do YouTube aqui:', '')

if st.button('Baixar Vídeo'):
    if video_url and is_valid_youtube_url(video_url):
        with st.spinner('Baixando... Por favor, aguarde.'):
            mensagem = baixar_video(video_url)
            if "Download concluído!" in mensagem:
                st.success(mensagem)
            else:
                st.error(mensagem)
    else:
        st.error('Por favor, insira um link válido de YouTube.')