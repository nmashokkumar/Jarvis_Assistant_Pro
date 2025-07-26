# app/main.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import asyncio
from voice.speech_to_text import listen_with_noise_reduction
from voice.text_to_speech import speak
from core.response_engine import get_response
from utils.logger import get_logger
from utils.finetune_logger import log_finetune_sample

# Import the grammar fixer
from core.grammar_fixer import fix_grammar

logger = get_logger("MAIN")

def main():
    logger.info("Jarvis is online and ready.")
    print("Jarvis is online and ready.")

    while True:
        print("\n[Jarvis] Listening...")
        user_input = listen_with_noise_reduction()

        if not user_input:
            logger.warning("No speech detected, continuing to listen.")
            continue

        print(f"[You]: {user_input}")
        logger.info(f"User said (raw): {user_input}")

        # Apply grammar fixer before sending to LLM
        corrected_input = fix_grammar(user_input)
        if corrected_input != user_input:
            logger.info(f"Grammar corrected: {corrected_input}")
        else:
            logger.info("No grammar corrections applied.")

        # System exit handling
        lower_input = corrected_input.lower()
        if "exit" in lower_input or "shutdown" in lower_input:
            logger.info("Shutdown command detected. Shutting down.")
            print("[Jarvis] Shutting down. Goodbye Boss.")
            asyncio.run(speak("Shutting down. Goodbye Boss"))
            break

        # Get LLM response
        response = get_response(corrected_input)
        print(f"[Jarvis]: {response}")
        logger.info(f"Jarvis response: {response}")
        log_finetune_sample(user_input, corrected_input, response)
        # Speak response
        asyncio.run(speak(response))

if __name__ == "__main__":
    main()
