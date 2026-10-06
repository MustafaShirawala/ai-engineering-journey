from datasets import load_dataset

dataset = load_dataset("stanfordnlp/imdb")
print(dataset["train"].features["label"])
print(dataset["test"][1]["text"])