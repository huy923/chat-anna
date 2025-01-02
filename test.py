# import glob, os
# os.chdir("./data")
# allfile = []
# for file in glob.glob("*.txt"):
#     allfile.append(file)
#     print(file)
# print([x for x in allfile])
import sentencepiece as spm
sp = spm.SentencePieceProcessor()
sp.load("tokenizer.model")
print(sp.IdToPiece(0))
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
print(tokenizer.tokenize("I love you"))
print(tokenizer.encode("I love you"))