# import sentencepiece as spm

# spm.SentencePieceTrainer.train(input='archwiki_pages.txt', model_prefix='tokenizer', vocab_size=1000, user_defined_symbols=['foo', 'bar'])
# import sentencepiece as spm
# import glob, os
# from collections import Counter

# files = []
# os.chdir("./data")
# for file in glob.glob("*.txt"):
#     files.append(file)

# if not files:
#     raise FileNotFoundError("No .txt files found in the './data' directory.")

# unique_tokens = Counter()
# for file in files:
#     with open(file, 'r', encoding='utf-8') as f:
#         for line in f:
#             tokens = line.strip().split() 
#             unique_tokens.update(tokens)

# default_vocab_size = 3000
# vocab_size = min(len(unique_tokens), default_vocab_size)
# print(f"Detected {len(unique_tokens)} unique tokens. Setting vocab_size={vocab_size}")

# input_files = ",".join(files)

# spm.SentencePieceTrainer.train(
#     input=input_files,
#     model_prefix='tokenizer',
#     vocab_size=vocab_size,
#     model_type='bpe',
#     user_defined_symbols=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"],
# )

# print("Tokenizer training complete! Files saved: tokenizer.model and tokenizer.vocab")



# =========================================================================================
import sentencepiece as spm
import glob, os

# Tạo danh sách các tệp dữ liệu
files = []
os.chdir("./data")
for file in glob.glob("*.txt"):
    files.append(file)

# Huấn luyện tokenizer
spm.SentencePieceTrainer.train(
    input=files,
    model_prefix='tokenizer',  # Tên của file output
    vocab_size=5000,           # Thử giảm số lượng từ vựng
    model_type='bpe',          # Chọn kiểu byte-pair encoding
    user_defined_symbols=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"],  # Các token đặc biệt
)

print("Tokenizer training complete!")

