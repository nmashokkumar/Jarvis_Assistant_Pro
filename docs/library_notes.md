# Library Notes for Jarvis Assistant Pro

## 1. edge-tts
- Purpose: Text-to-speech using Microsoft Edge voices with low latency.
- Usage: In TTS playback module to speak responses.

## 2. pydub
- Purpose: Convert MP3 to WAV, trim, combine audio.
- Usage: Helps in ensuring TTS output compatibility with simpleaudio.

## 3. simpleaudio
- Purpose: Lightweight audio playback for WAV files.
- Usage: Plays spoken responses in TTS module without heavy dependencies.

## 4. speechrecognition
- Purpose: Convert speech to text using microphone input.
- Usage: STT for Jarvis command handling.

## 5. noisereduce, librosa, soundfile, numpy
- Purpose: Noise reduction and clean audio pipeline for accurate transcription.
- Usage: Preprocessing microphone input for better STT accuracy.

## 6. transformers
- Purpose: Connects and downloads models from Hugging Face.
- Usage: Used for grammar fixing in Jarvis using the T5 base model.

## 7. torch
- Purpose: Backend tensor operations and neural network execution for transformer models.
- Usage: Required to run the T5 grammar fixer efficiently during inference.

## 8. sentencepiece
- Purpose: Tokenization for models like T5, BART that use SentencePiece-based tokenizers.
- Usage: Enables the tokenizer for T5 grammar fixer to process and decode text correctly.

## 9. accelerate
- Purpose: Speeds up transformer model inference and manages device placement efficiently.
- Usage: Optional, but helps optimize T5 grammar fixer execution if used.

## 10. safetensors
- Purpose: Provides fast and safe tensor storage/loading compared to .bin for models.
- Usage: Optional, enables faster and secure model loading in transformers for T5 grammar fixer.

## 11. ONXX runtime-directml and optimum[onnxruntime]
- Purpose: To run the model in onxx format in GPU
- Ussge: Used for grammar fixing
