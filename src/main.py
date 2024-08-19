import os
import logging
import warnings
from audio_processing import extract_audio_from_video, normalize_audio
from transcription import transcribe_audio, translate_text
from video_processing import sync_audio_with_video
from gtts import gTTS

# Configuração de logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("data/output/project_log.log"),
                        logging.StreamHandler()
                    ])

# Suprimir warnings desnecessários
warnings.filterwarnings("ignore")

def main():
    logging.info("Iniciando o pipeline de processamento de áudio e vídeo.")

    # Definindo os caminhos para os arquivos de entrada e saída
    video_path = "../Hotmart/data/input/case_video_hotmart.mp4"
    extracted_audio_path = "data/output/case_video_audio_5min.wav"
    normalized_audio_path = "data/output/case_video_audio_normalized.wav"
    transcription_output_path = "data/output/transcription_ptbr.txt"
    translation_output_path = "data/output/transcription_en.txt"
    audio_output_path = "data/output/transcription_en_audio.mp3"
    final_video_output_path = "data/output/output_video_with_english_audio.mp4"

    # Garantir que os diretórios de saída existam
    os.makedirs("data/output", exist_ok=True)

    try:
        # Etapa 1: Extração e normalização do áudio
        extract_audio_from_video(video_path, 0, 300, extracted_audio_path)
        normalize_audio(extracted_audio_path, normalized_audio_path)

        # Etapa 2: Transcrição e tradução do áudio
        transcription = transcribe_audio(normalized_audio_path, language='pt')
        with open(transcription_output_path, 'w', encoding='utf-8') as f:
            f.write(transcription)
            logging.info(f"Transcrição salva em {transcription_output_path}")
        
        translated_text = translate_text(transcription, from_lang='pt', to_lang='en')
        with open(translation_output_path, 'w', encoding='utf-8') as f:
            f.write(translated_text)
            logging.info(f"Tradução salva em {translation_output_path}")
        
        # Etapa 3: Síntese de voz (Text-to-Speech)
        logging.info("Iniciando síntese de voz em inglês.")
        tts = gTTS(text=translated_text, lang='en')
        tts.save(audio_output_path)
        logging.info(f"Áudio em inglês gerado e salvo em {audio_output_path}")

        # Etapa 4: Sincronização do áudio com o vídeo
        sync_audio_with_video(video_path, audio_output_path, final_video_output_path)

    except Exception as e:
        # Logar qualquer erro que ocorra durante o processo
        logging.error(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()