import os
import logging
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

# Função para extrair o áudio de um vídeo em um intervalo de tempo específico
def extract_audio_from_video(video_path, start_time, end_time, output_audio_path):
    # Log de início da extração de áudio do vídeo
    logging.info(f"Iniciando extração de áudio do vídeo: {video_path}")
    
    # Carrega o vídeo e recorta o trecho especificado pelo tempo de início e fim
    video_clip = VideoFileClip(video_path).subclip(start_time, end_time)
    # Extrai o áudio do trecho do vídeo e salva no caminho especificado
    video_clip.audio.write_audiofile(output_audio_path)

    # Verifica se o arquivo de áudio foi criado com sucesso
    if os.path.exists(output_audio_path):
        logging.info(f"Áudio extraído com sucesso e salvo em {output_audio_path}")
    else:
        # Log de erro e exceção se o arquivo de áudio não foi criado
        logging.error("Falha ao extrair o áudio.")
        raise FileNotFoundError("Falha ao extrair o áudio.")

# Função para normalizar o áudio extraído, ajustando o volume de forma uniforme
def normalize_audio(input_audio_path, output_audio_path):
    # Log de início da normalização do áudio
    logging.info(f"Iniciando normalização do áudio: {input_audio_path}")
    
    # Carrega o arquivo de áudio
    audio = AudioSegment.from_wav(input_audio_path)
    # Normaliza o áudio para garantir um volume uniforme
    normalized_audio = audio.normalize()
    # Exporta o áudio normalizado para um novo arquivo
    normalized_audio.export(output_audio_path, format="wav")
    
    # Log de sucesso ao salvar o áudio normalizado
    logging.info(f"Áudio normalizado salvo em {output_audio_path}")