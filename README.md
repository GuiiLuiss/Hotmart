# Hotmart | Voice-Over Automático para Vídeos

Este repositório contém a minha solução para o desafio proposto pela Hotmart. Neste projeto, desenvolvi um pipeline completo para extração de áudio de um vídeo, transcrição, tradução, síntese de voz em inglês e sincronização de áudio com vídeo, utilizando tecnologias open-source.

## 🎯 O Desafio

O objetivo deste projeto é processar um vídeo de um curso em Português (Brasil), transcrever o conteúdo, traduzir para o inglês e gerar um vídeo de exemplo com voice-over em inglês. Para demonstrar o conceito, processei um sample de 3 a 5 minutos do vídeo original.

## Pontos Considerados:

- **Uso de Ferramentas Open-Source**
- **Qualidade da Transcrição e Tradução**
- **Síntese de Voz**: A síntese de voz em inglês foi realizada utilizando uma voz padrão.
- **Sincronização do Áudio com o Vídeo**: A sincronização perfeita dos lábios com o áudio (lip-sync) não foi abordada devido ao escopo do projeto, mas o áudio foi sincronizado de forma funcional para o conceito de voice-over.

## 📁 Estrutura do Projeto

```plaintext
Hotmart/
├── data/
│   ├── input/
│   │   └── case_video_hotmart.mp4  # (Insira o vídeo a ser processado aqui)
│   └── output/                     # (Os resultados serão salvos aqui)
├── src/
│   ├── audio_processing.py
│   ├── main.py
│   ├── transcription.py
│   └── video_processing.py
├── requirements.txt
└── README.md
```

## 🚀 Como Executar o Projeto

### 1. Instalação das Dependências

Para reproduzir este projeto, instale as dependências necessárias com o seguinte comando:

```bash
pip install -r requirements.txt
```

### 2. Preparação dos Dados

Coloque o vídeo a ser processado na pasta `data/input` e renomeie-o para `case_video_hotmart.mp4`.

### 3. Execução do Pipeline

Com os dados prontos, execute o pipeline rodando o script `main.py` localizado na pasta `src`:

```bash
python src/main.py
```

## ✅ Resultados

Os resultados gerados pelo pipeline serão armazenados na pasta `data/output`. Os principais arquivos de saída são:

- **`case_video_audio_5min.wav`**: Áudio extraído do vídeo.
- **`case_video_audio_normalized.wav`**: Áudio normalizado.
- **`transcription_ptbr.txt`**: Transcrição do áudio em português.
- **`transcription_en.txt`**: Tradução da transcrição para o inglês.
- **`transcription_en_audio.mp3`**: Áudio em inglês gerado a partir da tradução.
- **`output_video_with_english_audio.mp4`**: Vídeo final com o áudio em inglês sincronizado.

## 🔍 Detalhes Técnicos

O pipeline desenvolvido consiste nas seguintes etapas:

1. **Extração e Normalização de Áudio**:
   - Utilizei `moviepy` para extrair o áudio do vídeo e `pydub` para normalizar o volume.

2. **Transcrição e Tradução**:
   - A transcrição do áudio em português foi realizada com o modelo `Whisper` da OpenAI.
   - A tradução para o inglês foi feita com a biblioteca `translate`.

3. **Síntese de Voz**:
   - A síntese de voz em inglês foi realizada com `gTTS` (Google Text-to-Speech).

4. **Sincronização de Áudio com Vídeo**:
   - O áudio gerado foi sincronizado com o vídeo original utilizando `moviepy`.

## 📜 Logs de Execução

Durante a execução, os logs detalhados do processo foram salvos no arquivo `data/output/project_log.log`. Este arquivo documenta cada etapa do pipeline, facilitando a análise e depuração.
