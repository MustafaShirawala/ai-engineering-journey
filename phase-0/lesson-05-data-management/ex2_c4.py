"""Import load_dataset, and also time (Python's built-in clock).
Load the dataset with streaming=True and split="train". As far as I know the name is allenai/c4 with the config "en", but I haven't tested it on your setup, so if it errors, paste the message.
Record the start time with start = time.time(), and start a counter at count = 0.
Loop through the dataset. For each example, add 1 to count. When time.time() - start >= 10, break.
Print count after the loop."""

from datasets import load_dataset
import time

dataset = load_dataset("allenai/c4", "en", streaming=True, split="train")
start = time.time()
count = 0

for example in dataset:
    count += 1
    if time.time() - start >= 10:
        break

print(f"Count: {count}")