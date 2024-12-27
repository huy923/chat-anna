# from tokenizers import Tokenizer, models, trainers

# tokenizer = Tokenizer(models.BPE())
# trainer = trainers.BpeTrainer(vocab_size=30000, special_tokens=["[CLS]", "[SEP]", "[PAD]", "[MASK]"])
# tokenizer.train(files=["archwiki_pages.txt"], trainer=trainer)

# tokenizer.save("tokenizer.json")
#===========================================================================================================
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.processors import TemplateProcessing

from transformers import PreTrainedTokenizerFast  # <---- Add this line.



trainer = BpeTrainer(special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"])

tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
tokenizer.pre_tokenizer = Whitespace()

files = ["archwiki_pages.txt"]  # e.g. training with https://norvig.com/big.txt
tokenizer.train(files, trainer)

tokenizer.post_processor = TemplateProcessing(
    single="[CLS] $A [SEP]",
    pair="[CLS] $A [SEP] $B:1 [SEP]:1",
    special_tokens=[
        ("[CLS]", tokenizer.token_to_id("[CLS]")),
        ("[SEP]", tokenizer.token_to_id("[SEP]")),
    ],
)

awesome_tokenizer = PreTrainedTokenizerFast(tokenizer_object=tokenizer)
awesome_tokenizer.save_pretrained("awesome_tokenizer")
# awesome_tokenizer.from_pretrained('./awesome_tokenizer/')


# import json

# tokenizer_config = {"max_len": 512, "name_or_path": "tokenizer_name"}

# with open("tokenizer_config.json", 'w') as fp:
#     json.dump(tokenizer_config, fp)
# config = {
#     "architectures": [
#         "RobertaForMaskedLM"
#     ],
#     "attention_probs_dropout_prob": 0.1,
#     "hidden_act": "gelu",
#     "hidden_dropout_prob": 0.1,
#     "hidden_size": 768,
#     "initializer_range": 0.02,
#     "intermediate_size": 3072,
#     "layer_norm_eps": 1e-05,
#     "max_position_embeddings": 40000, #512, changed to 40000
#     "model_type": "roberta",
#     "num_attention_heads": 12,
#     "num_hidden_layers": 6,
#     "type_vocab_size": 1,
#     "vocab_size": 30 #30522, changed to 30 rostlab aminoacid vocabulary
# }

# with open("config.json", 'w') as fp:
#     json.dump(config, fp)