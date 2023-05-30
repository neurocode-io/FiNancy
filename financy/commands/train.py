import subprocess

def train(jsonl_file: str, base_model: str):
    # openai api fine_tunes.create -t <TRAIN_FILE_ID_OR_PATH> -m <BASE_MODEL>
    process = subprocess.run(["openai", "api", "fine_tunes.create", "-t", f"{jsonl_file}", "-m", f"{base_model}" ], capture_output=True, text=True)
    if process.returncode != 0:
        raise Exception(f"openai command failed: {process.stderr}")
    print(process.stdout)
