# voice/speech_noise_test.py

import speech_recognition as sr
import noisereduce as nr
import librosa
import soundfile as sf

def record_and_denoise_test(timeout=5, phrase_time_limit=10):
    recognizer = sr.Recognizer()
    raw_path = "raw_input.wav"
    clean_path = "clean_output.wav"

    print("🎤 Speak something... Jarvis will record background noise too...")

    with sr.Microphone() as source:
        try:
            recognizer.adjust_for_ambient_noise(source, duration=2.0)
            print("📢 Start speaking...")
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        except sr.WaitTimeoutError:
            print("❌ Didn't hear anything in time, Boss.")
            return

    # Save RAW audio
    with open(raw_path, "wb") as f:
        f.write(audio.get_wav_data())
    print(f"✅ Raw audio saved as '{raw_path}'")

    # Perform noise reduction and save CLEANED version
    try:
        y, sr_rate = librosa.load(raw_path, sr=None)
        reduced = nr.reduce_noise(y=y, sr=sr_rate)
        sf.write(clean_path, reduced, sr_rate)
        print(f"✅ Cleaned audio saved as '{clean_path}'")
    except Exception as e:
        print(f"❌ Noise reduction failed: {e}")
        return

    # Optional: Transcribe the cleaned audio
    try:
        with sr.AudioFile(clean_path) as source:
            cleaned_audio = recognizer.record(source)
        text = recognizer.recognize_google(cleaned_audio)
        print(f"🗣️ Transcription: {text}")
    except Exception as e:
        print(f"⚠️ Transcription error: {e}")
if __name__ == "__main__":
    record_and_denoise_test()