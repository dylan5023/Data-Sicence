from tensorflow import keras
import data_reader

# Set up EPOCHS
EPOCHS = 20

# Read Data
dr = data_reader.DataReader()

# Create DNN
model = keras.Sequential([
    keras.layers.Dense(20000),
    keras.layers.Dense(2048, activation="relu"),
    keras.layers.Dropout(rate=0.5),
    keras.layers.Dense(256, activation="relu"),
    keras.layers.Dropout(rate=0.5),
    keras.layers.Dense(4, activation='softmax')
])

# Compile
model.compile(optimizer="adam", metrics=["accuracy"],
              loss="sparse_categorical_crossentropy")

# Training
print("\n\n************ TRAINING START ************ ")
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)
history = model.fit(dr.train_X, dr.train_Y, epochs=EPOCHS,
                    validation_data=(dr.test_X, dr.test_Y),
                    callbacks=[early_stop])

# Draw result
data_reader.draw_graph(history)
