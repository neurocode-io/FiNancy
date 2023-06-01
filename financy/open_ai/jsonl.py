from collections import namedtuple

Entry = namedtuple("Entry", ["prompt", "completion"])

# Each prompt should end with a fixed separator to inform the model when the prompt ends and the completion begins. 
seperator = "\n\nDecision:"
stop_sequence = "\n"

def write_entry(entry: Entry, file_name: str = "financy_form.jsonl"):
    with open(file_name, "a") as f:
        # {"prompt": "<prompt text>", "completion": "<ideal generated text>"}

        # we encode to perserve the newline character
        encodedPrompt = f"{entry.prompt}{seperator}".encode('unicode_escape').decode('utf-8')
        encodedCompletion = f"{entry.completion}{stop_sequence}".encode('unicode_escape').decode('utf-8')
        f.write(f'{{"prompt": "{encodedPrompt}", "completion": "{encodedCompletion}"}}\n')
