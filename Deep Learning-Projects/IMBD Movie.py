import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reproducibility
np.random.seed(42)
tf.random.set_seed(42)

vocab_size = 20000   # number of unique words to keep
maxlen = 200         # maximum sequence length
(x_train, y_train), (x_test, y_test) = keras.datasets.imdb.load_data(num_words=vocab_size)

print("Training samples:", len(x_train))
print("Test samples:", len(x_test))
x_train_padded = pad_sequences(x_train, maxlen=maxlen, padding="pre", truncating="pre")
x_test_padded = pad_sequences(x_test, maxlen=maxlen, padding="pre", truncating="pre")

print("Padded shape:", x_train_padded.shape, x_test_padded.shape)

embedding_dim = 128

model = keras.Sequential([
    layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=maxlen),
    layers.Bidirectional(layers.LSTM(128, dropout=0.2, recurrent_dropout=0.2)),
    layers.Dense(64, activation="relu"),
    layers.Dropout(0.5),
    layers.Dense(1, activation="sigmoid")
])

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
model.summary()
history = model.fit(
    x_train_padded, y_train,
    validation_split=0.2,
    epochs=5,
    batch_size=128,
    verbose=1
)
loss, acc = model.evaluate(x_test_padded, y_test, verbose=2)
print(f"Test Loss: {loss:.4f}, Test Accuracy: {acc:.4f}")
# Plotting training history
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history["loss"], label="Train Loss")
plt.plot(history.history["val_loss"], label="Val Loss")
plt.legend()
plt.title("Loss")

plt.subplot(1, 2, 2)
plt.plot(history.history["accuracy"], label="Train Accuracy")
plt.plot(history.history["val_accuracy"], label="Val Accuracy")
plt.legend()
plt.title("Accuracy")

plt.show()
# Inference on a sample review
word_index = keras.datasets.imdb.get_word_index()

def text_to_sequence(text, vocab_size=vocab_size):
    text = text.lower().split()
    seq = []
    for word in text:
        idx = word_index.get(word)
        if idx is not None and idx < vocab_size:
            seq.append(idx + 3)  # keras offset
        else:
            seq.append(2)  # <UNK>
    return seq

sample_review = "I loved this movie, it was amazing and the acting was great"
seq = text_to_sequence(sample_review)
seq_padded = pad_sequences([seq], maxlen=maxlen)

prediction = model.predict(seq_padded)[0][0]
print("Prediction (positive sentiment probability):", prediction)