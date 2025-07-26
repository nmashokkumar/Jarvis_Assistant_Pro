import asyncio
from voice.speech_to_text import listen
from core.response_engine import generate_llm_response
from voice.text_to_speech import speak

async def main_pipeline():
    print("[Pipeline] Calibrating mic & listening...")

    user_input = listen()

    if not user_input.strip():
        print("[Pipeline] No input captured.")
        return

    print(f"[Pipeline] You said: {user_input}")

    print("[Pipeline] Sending to LLM (Jarvis_FT)...")
    llm_reply = await generate_llm_response(user_input, model_id="jarvis_FT")

    print(f"[Pipeline] Jarvis_FT replied: {llm_reply}")

    await speak(llm_reply)

if __name__ == "__main__":
    asyncio.run(main_pipeline())
