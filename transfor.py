# from transformers import GPT2Config, GPT2LMHeadModel, Trainer, TrainingArguments

# # Tạo cấu hình
# config = GPT2Config(vocab_size=30000)
# model = GPT2LMHeadModel(config)

# # Huấn luyện mô hình
# training_args = TrainingArguments(output_dir="./model")
# trainer = Trainer(model=model, args=training_args, train_dataset=your_dataset)
# trainer.train()

# # Lưu mô hình
# model.save_pretrained("./model")
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained('./saved_model/')