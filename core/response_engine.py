# core/response_engine.py

import asyncio
import time
from utils.logger import get_logger
logger = get_logger("RESP")

MODEL_MAP = {
    "jarvis_ft": "jarvis31_q4km:latest",
    "llama3": "llama3:latest",
    "deepseek": "deepseek-coder:1.3b"
}

async def generate_llm_response(prompt, model_id):
    """
    Runs Ollama locally and returns the model's response.
    """
    try:
        process = await asyncio.create_subprocess_exec(
            'ollama', 'run', model_id,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate(input=prompt.encode('utf-8'))

        if stderr:
            logger.warning(f"[LLM STDERR] {stderr.decode('utf-8').strip()}")

        response = stdout.decode('utf-8', errors='replace').strip()
        return response

    except Exception as e:
        logger.error(f"LLM invocation failed: {e}")
        return "[Jarvis Error] Unable to generate response."

def get_response(user_input, model_name="jarvis_ft"):
    """
    Blocking wrapper for generating LLM responses for pipeline testing.
    """
    try:
        model_id = MODEL_MAP.get(model_name.lower())
        if not model_id:
            logger.warning(f"Requested unknown model: {model_name}. Falling back to Jarvis FT.")
            model_id = MODEL_MAP["jarvis_ft"]

        prompt = user_input.strip()

        logger.info(f"Sending prompt to {model_id}: {prompt[:50]}...")
        start_time = time.perf_counter()

        response = asyncio.run(generate_llm_response(prompt, model_id))

        duration = round(time.perf_counter() - start_time, 2)
        logger.info(f"LLM response received in {duration}s")

        return response

    except Exception as e:
        logger.error(f"Error during LLM response generation: {e}")
        return "[Jarvis Error] Failed to get response."
