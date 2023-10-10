
from tensorflow import keras
import data_reader
import unet

# Set up EPOCHS
EPOCHS = 50  

# Read Data
dr = data_reader.DataReader()

# Set up U-net
model = unet.graph(128, 128)

# Compile
loss = keras.losses.BinaryCrossentropy(from_logits=True)
model.compile(optimizer="adam", loss=loss, metrics=['accuracy'])

# Training
print("\n\n************ TRAINING START ************ ")
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)
history = model.fit(dr.train_X, dr.train_Y, epochs=EPOCHS,
                    validation_data=(dr.test_X, dr.test_Y),
                    callbacks=[early_stop])

# Store result in Segmentation
data_reader.save_segmentation_results(dr.test_X, dr.test_Y, model)

# Output result
data_reader.draw_graph(history)
