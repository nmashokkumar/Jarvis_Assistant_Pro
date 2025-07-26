# core/FixGrammar.py

import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from utils.logger import get_logger

logger = get_logger("FixGrammar")

MODEL_NAME = "vennify/t5-base-grammar-correction"

# Point model + tokenizer cache to your models/grammar_model folder
LOCAL_MODEL_DIR = os.path.join(
    os.path.dirname(__file__),  # core/
    "..",                       # up one level to Jarvis_Assistant_Pro/
    "models",                   # into models/
    "grammar_model"             # grammar_model/
)
LOCAL_MODEL_DIR = os.path.abspath(LOCAL_MODEL_DIR)

os.makedirs(LOCAL_MODEL_DIR, exist_ok=True)

try:
    # Check if tokenizer + config exist, else download
    tokenizer = AutoTokenizer.from_pretrained(
        LOCAL_MODEL_DIR if os.path.exists(os.path.join(LOCAL_MODEL_DIR, "tokenizer_config.json")) else MODEL_NAME,
        cache_dir=LOCAL_MODEL_DIR
    )
    model = AutoModelForSeq2SeqLM.from_pretrained(
        LOCAL_MODEL_DIR if os.path.exists(os.path.join(LOCAL_MODEL_DIR, "config.json")) else MODEL_NAME,
        cache_dir=LOCAL_MODEL_DIR
    )
    logger.info(f"T5 Grammar model loaded and using cache at: {LOCAL_MODEL_DIR}")

except Exception as e:
    logger.error(f"Failed to load T5 Grammar model: {e}")
    raise

def fix_grammar(text: str) -> str:
    if not text.strip():
        return text

    input_text = "grammar: " + text
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True)

    output_tokens = model.generate(**inputs, max_new_tokens=128)
    corrected = tokenizer.decode(output_tokens[0], skip_special_tokens=True)

    if corrected != text:
        print(f"[Grammar] Fixed: {corrected}")
        logger.info(f"Grammar corrected: '{text}' -> '{corrected}'")

    return corrected
