import speech_recognition as sr
from utils.logger import get_logger

logger = get_logger("STT")

recognizer = sr.Recognizer()

def listen_and_transcribe(timeout=5, phrase_time_limit=60):
    with sr.Microphone() as source:
        try:
            logger.info("Listening for speech input...")
            audio = recognizer.listen(
                source, timeout=timeout, phrase_time_limit=phrase_time_limit
            )
        except sr.WaitTimeoutError:
            print("Couldn't hear that, Boss. Please try again.")
            return ""

    try:
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
