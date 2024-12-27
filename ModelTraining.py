import sentencepiece as spm

spm.SentencePieceTrainer.train(input='archwiki_pages.txt', model_prefix='tokenizer', vocab_size=1000, user_defined_symbols=['foo', 'bar'])
