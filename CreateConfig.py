import json

config = {
    "_name_or_path": "MyCustomModel/V1.0",
    "architectures": ["LlamaForCausalLM"],
    "attention_bias": False,
    "bos_token_id": 1,
    "eos_token_id": 2,
    "hidden_act": "silu",
    "hidden_size": 2048,
    "initializer_range": 0.02,
    "intermediate_size": 5632,
    "max_position_embeddings": 2048,
    "model_type": "llama",
    "num_attention_heads": 32,
    "num_hidden_layers": 22,
    "num_key_value_heads": 4,
    "pretraining_tp": 1,
    "rms_norm_eps": 1e-05,
    "rope_scaling": None,
    "rope_theta": 10000.0,
    "tie_word_embeddings": False,
    "torch_dtype": "float32",
    "transformers_version": "4.34.0.dev0",
    "use_cache": False,
    "vocab_size": 32003
}

with open("config.json", "w") as f:
    json.dump(config, f, indent=4)

print("Config file created successfully!")
