import os

LOG_FILE = os.path.join("logs", "grammar_finetune_raw.log")

def log_finetune_sample(raw_text: str, fixed_text: str, llm_response: str):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"RAW: {raw_text.strip()}\n")
        f.write(f"FIXED: {fixed_text.strip()}\n")
        f.write(f"LLM: {llm_response.strip()}\n")
        f.write("---\n")
