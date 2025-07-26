import json
import os
input_file = "logs/grammar_finetune_raw.log"
output_file = "datasets/grammar_finetune_dataset.jsonl"

if not os.path.exists("datasets"):
    os.makedirs("datasets")

with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
    sample = {}
    for line in f_in:
        line = line.strip()
        if line.startswith("RAW:"):
            sample["raw_text"] = line[len("RAW:"):].strip()
        elif line.startswith("FIXED:"):
            sample["fixed_text"] = line[len("FIXED:"):].strip()
        elif line.startswith("LLM:"):
            sample["llm_response"] = line[len("LLM:"):].strip()
        elif line.strip() == "---":
            f_out.write(json.dumps(sample, ensure_ascii=False) + "\n")
            sample = {}

print(f"✅ Conversion complete: Saved to {output_file}")
