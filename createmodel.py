# import sentencepiece as spm

# # Huấn luyện SentencePiece và tạo tokenizer.model
# spm.SentencePieceTrainer.train(
#     input='archwiki_pages.txt',           # Tệp văn bản nguồn
#     model_prefix='tokenizer',            # Tiền tố cho các tệp đầu ra
#     vocab_size=32003,                    # Tổng số từ vựng (bao gồm cả token đặc biệt)
#     pad_id=32000,                        # ID cho token [PAD]
#     unk_id=0,                            # ID cho token <unk>
#     bos_id=1,                            # ID cho token <s>
#     eos_id=2,                            # ID cho token </s>
#     user_defined_symbols=["<|im_start|>", "<|im_end|>"],  # Các token đặc biệt bổ sung
#     model_type='bpe',                    # Loại tokenizer (BPE - Byte Pair Encoding)
#     max_sentence_length=4096             # Chiều dài tối đa của câu
# )

# print("Tạo tokenizer.model và tokenizer.vocab thành công!")
from transformers import BertTokenizer

# tokenizer = AutoTokenizer.from_pretrained('distilroberta-base')
# config = AutoConfig.from_pretrained('distilroberta-base')

# tokenizer.save_pretrained('YOURPATH')
# config.save_pretrained('YOURPATH')

# tokenizer = AutoTokenizer.from_pretrained('YOURPATH')
tokenizer = BertTokenizer.from_pretrained('./awesome_tokenizer/')