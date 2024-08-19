import logging
from moviepy.editor import VideoFileClip, AudioFileClip
from tqdm import tqdm

# Função para sincronizar um áudio com um vídeo, com opção de limitar a duração máxima
def sync_audio_with_video(video_path, audio_path, output_video_path, max_duration=180):
    try:
        logging.info(f"Iniciando sincronização do áudio {audio_path} com o vídeo {video_path}")
        
        # Carrega o vídeo e limita a duração ao valor máximo especificado
        video_clip = VideoFileClip(video_path)
        video_clip = video_clip.subclip(0, min(max_duration, video_clip.duration))
        
        # Carrega o áudio e limita a duração ao valor máximo especificado
        audio_clip = AudioFileClip(audio_path)
        audio_clip = audio_clip.subclip(0, min(max_duration, audio_clip.duration))
        
        logging.info("Iniciando renderização do vídeo final.")
        
        # Cria uma barra de progresso durante a renderização do vídeo final
        with tqdm(total=100, desc="Renderizando vídeo") as pbar:
            final_clip = video_clip.set_audio(audio_clip)
            final_clip.write_videofile(output_video_path, codec="libx264", audio_codec="aac")
            pbar.update(100)
        
        logging.info(f"Vídeo gerado e salvo em {output_video_path}")
    
    except Exception as e:
        # Captura e loga qualquer erro que ocorra durante o processo
        logging.error(f"Ocorreu um erro na sincronização do vídeo: {e}")
        raise
