import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf
import pathlib
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator

#%%
# batch_size = 4

# train = ImageDataGenerator(rescale=1/255,
#         featurewise_center=True,
#         featurewise_std_normalization=True,
#         rotation_range=20,  # randomly rotate images in the range 5 degrees
#         zoom_range = 0.2, # Randomly zoom image 10%
#         width_shift_range=0.2,  # randomly shift images horizontally 10%
#         height_shift_range=0.2,  # randomly shift images vertically 10%
#         horizontal_flip=True,  # randomly flip images
#         vertical_flip=True)  # randomly flip images)

# validation = ImageDataGenerator(rescale=1/255,
#         featurewise_center=True,
#         featurewise_std_normalization=True,
#         rotation_range=20,  # randomly rotate images in the range 5 degrees
#         zoom_range = 0.2, # Randomly zoom image 10%
#         width_shift_range=0.2,  # randomly shift images horizontally 10%
#         height_shift_range=0.2,  # randomly shift images vertically 10%
#         horizontal_flip=True,  # randomly flip images
#         vertical_flip=True)

# img_height = 640
# img_width = 640
# target_size = (img_height, img_width)

# train_dataset = train.flow_from_directory("C:/Users/kumralf/Desktop/nyp_mineral/dataset/train/", target_size=target_size, batch_size= batch_size, color_mode='rgb', shuffle=True)
# validation_dataset = train.flow_from_directory("C:/Users/kumralf/Desktop/nyp_mineral/dataset/validation/", target_size=target_size, batch_size= batch_size, color_mode='rgb', shuffle=True)

#%%
data_dir = "C:/Users/kumralf/Desktop/nyp_mineral/dataset/train"
data_dir = pathlib.Path(data_dir)
image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)

batch_size = 4
img_height = 640
img_width = 640

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
  data_dir,
  image_size=(img_height, img_width),
  batch_size=batch_size)

data_dir = "C:/Users/kumralf/Desktop/nyp_mineral/dataset/validation"
data_dir = pathlib.Path(data_dir)
image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
  data_dir,
  image_size=(img_height, img_width),
  batch_size=batch_size)

#%%
image_batch, labels_batch = next(iter(train_ds))

#%%
class_names = train_ds.class_names

#%%

normalization_layer = layers.experimental.preprocessing.Rescaling(1./255)
normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
image_batch, labels_batch = next(iter(normalized_ds))
first_image = image_batch[0]
# Notice the pixels values are now in `[0,1]`.
print(np.min(first_image), np.max(first_image)) 

#%%
num_classes = 10

model = Sequential([
  layers.experimental.preprocessing.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
  layers.Conv2D(16, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(64, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Dropout(0.3),
  layers.Conv2D(128, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(256, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(512, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Dropout(0.2),
  layers.Flatten(),
  layers.Dense(100, activation='relu'),
  layers.Dropout(0.1),
  layers.Dense(20, activation='relu'),
  layers.Dropout(0.1),
  layers.Dense(num_classes)
])

#%%

#callbacks = [keras.callbacks.ModelCheckpoint("/content/modelcnn/save_at_{epoch}.h5"),]
opt = keras.optimizers.Adam(learning_rate=0.0001)

model.compile(optimizer=opt,
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.summary() 

#%% 

# epochs=50

# model.fit(train_dataset, epochs=epochs, validation_data=validation_dataset, shuffle=True, validation_steps=len(validation_dataset))

#%%
epochs=50
history = model.fit(
  train_ds,
  callbacks=None,
  validation_data=val_ds,
  epochs=epochs
)
#%%

model.save("C:/Users/kumralf/Desktop/nyp_mineral/models/model_mineral3.h5")

#%%
print(history.history.keys())
# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
plt.savefig('accuracy2.jpg')
#%%
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
plt.savefig('loss2.jpg')


#%%
import cv2
import pickle
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from glob import glob
from tensorflow import keras
from keras.models import load_model
from scipy.interpolate import Rbf, InterpolatedUnivariateSpline
model = load_model("C:/Users/kumralf/Desktop/nyp_mineral/models/model_mineral.h5")

#%%

img_height = 640
img_width = 640
image_size=(img_height, img_width)
img = keras.preprocessing.image.load_img(
    "C:/Users/kumralf/Desktop/nyp_mineral/dataset/validation/kromit/1.jpg", target_size=image_size
)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # Create batch axis

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])
class_names[np.argmax(score)]
print(
    "This image most likely belongs to {} with a {:.2f} percent."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)
# print(predictions)
#%%
x = model.evaluate(val_ds)

#%%
# list all data in history
