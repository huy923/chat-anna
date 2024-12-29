# import sentencepiece as spm

# spm.SentencePieceTrainer.train(input='archwiki_pages.txt', model_prefix='tokenizer', vocab_size=1000, user_defined_symbols=['foo', 'bar'])
import sentencepiece as spm
import glob, os

files = []
os.chdir("./data")
for file in glob.glob("*.txt"):
    files.append(file)
# Train the SentencePiece model
spm.SentencePieceTrainer.train(
    input=files,  # Input text file
    model_prefix='tokenizer',   # Output model files: tokenizer.model and tokenizer.vocab
    vocab_size=3000,           # Vocabulary size (adjust as needed)
    model_type='bpe',           # You can choose: 'bpe', 'unigram', 'char', or 'word'
    user_defined_symbols=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"],  # Special tokens
)

print("Tokenizer training complete! Files saved: tokenizer.model and tokenizer.vocab")
