"""Import load_dataset.
Load "glue" with the config "mrpc" and split="train".
Print the dataset, to see its columns.
Print the first 5 rows. You've seen two ways to get rows: indexing like dataset[0], and .take(5) for streamed data. Choose either one. For a normal (non-streamed) dataset, dataset[:5] gives the first five."""

from datasets import load_dataset

dataset = load_dataset("nyu-mll/glue", "mrpc", split="train")
print(dataset.features["label"])
print(dataset[:5])

