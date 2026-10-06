from datasets import load_dataset

dataset = load_dataset("wikimedia/wikipedia", "20231101.en", split="train", streaming=True)

for example in dataset.take(5):
    print(example["title"])