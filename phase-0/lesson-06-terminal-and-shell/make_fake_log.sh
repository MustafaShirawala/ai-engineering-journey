#!/usr/bin/env bash
# Makes a fake training log: 100 lines where the loss shrinks like a learning model.
for i in $(seq 1 100); do
    echo "epoch $i loss: $(echo "scale=4; 1/$i" | bc)"
    sleep 0.1
done > fake_train.log