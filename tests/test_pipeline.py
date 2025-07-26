import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import asyncio
from voice.speech_to_text import listen_with_noise_reduction
from voice.text_to_speech import speak
from core.response_engine import get_response  # Assuming this returns LLM response
from utils.logger import get_logger
logger = get_logger(__name__)

async def main():
    logger.info("🚀 Starting Jarvis Pro pipeline test: STT ➔ LLM ➔ TTS.")

    # Step 1: Capture user speech
    user_query = listen_with_noise_reduction(timeout=5, phrase_time_limit=10)

    if not user_query:
        logger.warning("No input captured from STT. Exiting pipeline test.")
        print("[HIGH] No speech detected. Please try again.")
        return

    logger.info(f"User query captured: {user_query}")

    # Step 2: Generate LLM response
    try:
        response_text = get_response(user_query)
        logger.info(f"LLM response generated: {response_text}")
    except Exception as e:
        logger.error(f"LLM response generation failed: {e}", exc_info=True)
        print("[HIGH] LLM failed to generate a response.")
        return

    # Step 3: Speak out LLM response
    try:
        await speak(response_text, emotion="normal")  # You can pass emotion detection here later
        logger.info("TTS playback completed for LLM response.")
    except Exception as e:
        logger.error(f"TTS playback failed: {e}", exc_info=True)
        print("[HIGH] TTS playback failed.")

    logger.info("✅ Jarvis Pro pipeline test completed.")

if __name__ == "__main__":
    asyncio.run(main())


