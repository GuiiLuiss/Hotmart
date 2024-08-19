import logging
import whisper
from translate import Translator
from tqdm import tqdm

# Função para transcrever o áudio usando o modelo Whisper
def transcribe_audio(audio_path, language='pt'):
    logging.info(f"Iniciando transcrição do áudio: {audio_path}")
    
    # Carrega o modelo Whisper e realiza a transcrição
    model = whisper.load_model("large")
    result = model.transcribe(audio_path, language=language)
    
    logging.info("Transcrição concluída.")
    return result['text']

# Função para traduzir o texto de um idioma para outro
def translate_text(text, from_lang='pt', to_lang='en'):
    logging.info("Iniciando tradução do texto.")
    
    # Instancia o tradutor e divide o texto para evitar limites de caracteres
    translator = Translator(from_lang=from_lang, to_lang=to_lang)
    text_parts = split_text(text)
    
    # Traduz cada parte do texto
    translated_parts = [translator.translate(part) for part in tqdm(text_parts, desc="Traduzindo texto")]
    
    logging.info("Tradução concluída.")
    return " ".join(translated_parts)

# Função auxiliar para dividir o texto em partes menores
def split_text(text, max_length=500):
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]

