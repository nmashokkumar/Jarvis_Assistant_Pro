import asyncio
import tempfile
import edge_tts
from pydub import AudioSegment
import simpleaudio as sa
from utils.logger import get_logger
logger = get_logger("TTS")

# Voice and emotion config
VOICE = "en-US-AndrewMultilingualNeural"
EMOTION_SETTINGS_LIMITED = {
    "happy": {"rate": "+5%", "pitch": "+3Hz", "volume": "+3%"},
    "angry": {"rate": "+5%", "pitch": "+0Hz", "volume": "+5%"},
    "sad": {"rate": "-3%", "pitch": "-3Hz", "volume": "+0%"},
    "normal": {"rate": "+0%", "pitch": "+0Hz", "volume": "+0%"},
    "caring": {"rate": "-2%", "pitch": "-2Hz", "volume": "+0%"}
}

def clean_text(text):
    import re
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

async def speak(text, emotion="normal"):
    """
    Speaks the given text with the specified emotion using edge-tts and plays it.
    Logs events instead of cluttered prints.
    """
    try:
        e = EMOTION_SETTINGS_LIMITED.get(emotion, EMOTION_SETTINGS_LIMITED["normal"])
        clean = clean_text(text)

        logger.info(f"TTS requested | Emotion: {emotion} | Rate: {e['rate']} | Pitch: {e['pitch']} | Volume: {e['volume']}")
        
        tts = edge_tts.Communicate(
            clean,
            voice=VOICE,
            rate=e["rate"],
            pitch=e["pitch"],
            volume=e["volume"]
        )

        temp_mp3 = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        await tts.save(temp_mp3.name)
        logger.info(f"TTS audio saved temporarily: {temp_mp3.name}")

        audio = AudioSegment.from_file(temp_mp3.name, format="mp3")
        temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        audio.export(temp_wav.name, format="wav")
        logger.info(f"TTS audio converted to WAV: {temp_wav.name}")

        wave_obj = sa.WaveObject.from_wave_file(temp_wav.name)
        play_obj = wave_obj.play()

        while play_obj.is_playing():
            await asyncio.sleep(0.1)

        logger.info(f"TTS playback completed successfully for emotion: {emotion}")

    except Exception as e:
        logger.error(f"[TTS ERROR] {e}", exc_info=True)
        print("[HIGH] TTS fallback triggered due to critical error.")  # ✅ High priority, show in terminal
