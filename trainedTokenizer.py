from transformers import AutoTokenizer

auto_loaded_tokenizer = AutoTokenizer.from_pretrained(
    "awesome_tokenizer", 
    local_files_only=True
)
