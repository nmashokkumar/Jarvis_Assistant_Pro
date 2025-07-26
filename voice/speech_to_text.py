import speech_recognition as sr
import noisereduce as nr
import librosa
import soundfile as sf
import os
from utils.logger import get_logger

logger = get_logger("STT")

recognizer = sr.Recognizer()
recognizer.pause_threshold = 1.8
recognizer.dynamic_energy_threshold = False

# One-time mic calibration on import
with sr.Microphone() as source:
    logger.info("Calibrating microphone for ambient noise...")
    recognizer.adjust_for_ambient_noise(source, duration=2.0)
    logger.info(
        f"Microphone calibration completed with energy_threshold={recognizer.energy_threshold}"
    )



def listen_with_noise_reduction(timeout=5, phrase_time_limit=60):
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(
                source, timeout=timeout, phrase_time_limit=phrase_time_limit
            )
        except sr.WaitTimeoutError:
            print("Couldn't hear that, Boss. Please try again.")
            return ""

    temp_wav = "temp.wav"
    clean_wav = "clean.wav"

    try:
        # Save raw audio
        with open(temp_wav, "wb") as f:
            f.write(audio.get_wav_data())

        # Check if file is non-empty
        if os.path.getsize(temp_wav) == 0:
            print("Audio capture failed, please try again.")
            logger.error("[STT] Captured WAV file is empty.")
            return ""

        try:
            y, sr_rate = librosa.load(temp_wav, sr=None)
            reduced = nr.reduce_noise(y=y, sr=sr_rate)
            sf.write(clean_wav, reduced, sr_rate)
        except Exception as e:
            logger.error(f"[STT] Noise reduction failed: {e}")
            print("Noise reduction failed, please try again.")
            return ""

        # Transcribe cleaned audio
        with sr.AudioFile(clean_wav) as source:
            audio = recognizer.record(source)

        query = recognizer.recognize_google(audio)
        return query

    except sr.UnknownValueError:
        print("I didn't understand that, Boss.")
        return ""

    except sr.RequestError as e:
        logger.error(f"[STT] Speech recognition service request failed: {e}")
        return ""

    except Exception as e:
        logger.error(f"[STT] Unexpected error in STT pipeline: {e}")
        return ""

    finally:
        for f in [temp_wav, clean_wav]:
            if os.path.exists(f):
                os.remove(f)
