# Hotmart - Voice-over Automático para Vídeos
Avaliação - Cientista de Dados (AI Labs)

Este projeto demonstra um pipeline completo para extração de áudio de um vídeo, transcrição, tradução, síntese de voz em inglês e sincronização de áudio com vídeo, utilizando tecnologias de código aberto. 

## Estrutura do Projeto

```plaintext
Hotmart/
├── data/
│   ├── input/
│   │   └── case_video_hotmart.mp4  # (Insira o vídeo aqui)
│   └── output/                     # (Os resultados serão salvos aqui)
├── src/
│   ├── audio_processing.py
│   ├── main.py
│   ├── transcription.py
│   └── video_processing.py
├── requirements.txt
└── README.md
```

Para instalar as dependências necessárias, execute:

```bash
pip install -r requirements.txt
```

## Como Executar

1. **Preparação dos dados**: Coloque o vídeo a ser processado dentro da pasta `data/input` e renomeie-o para `case_video_hotmart.mp4`.

2. **Execução do pipeline**: Após a configuração dos dados, basta rodar o arquivo `main.py` localizado na pasta `src`:

```bash
python src/main.py
```

3. **Resultados**: Os arquivos gerados pelo pipeline estarão na pasta `data/output`:

    - `case_video_audio_5min.wav`: Áudio extraído do vídeo.
    - `case_video_audio_normalized.wav`: Áudio normalizado.
    - `transcription_ptbr.txt`: Transcrição do áudio em português.
    - `transcription_en.txt`: Tradução da transcrição para o inglês.
    - `transcription_en_audio.mp3`: Áudio em inglês gerado a partir da tradução.
    - `output_video_with_english_audio.mp4`: Vídeo final com o áudio em inglês sincronizado.

## Detalhes Técnicos

O pipeline completo envolve as seguintes etapas:

1. **Extração e Normalização de Áudio**:
   - Utilizamos `moviepy` para extrair o áudio do vídeo original e `pydub` para normalizar o volume do áudio extraído.

2. **Transcrição e Tradução**:
   - A transcrição do áudio em português é realizada utilizando o modelo `Whisper` da OpenAI.
   - A tradução do texto transcrito é feita com a biblioteca `translate`.

3. **Síntese de Voz**:
   - A síntese de voz em inglês é feita utilizando a biblioteca `gTTS` (Google Text-to-Speech).

4. **Sincronização de Áudio com Vídeo**:
   - A sincronização do áudio gerado com o vídeo original é realizada utilizando `moviepy`.

## Logs

Durante a execução, os logs do processo serão gerados no arquivo `data/output/project_log.log`. Esse arquivo contém informações detalhadas sobre cada etapa do pipeline.

## Considerações Finais

Este projeto é um protótipo focado em mostrar as capacidades de manipulação de mídia e processamento de linguagem natural. A sincronização perfeita dos lábios com a fala (lip-sync) não foi abordada neste protótipo devido às restrições de tempo e complexidade.
