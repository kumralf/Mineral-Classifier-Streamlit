def classify(img):
    import cv2
    import pickle
    import numpy as np
    import tensorflow as tf
    gpus = tf.config.experimental.list_physical_devices('GPU')
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)
    import matplotlib.pyplot as plt
    import pathlib
    from glob import glob
    from tensorflow import keras
    from keras.models import load_model
      
    data_dir = "C:/Users/kumralf/Desktop/nyp_mineral/dataset/train"
    data_dir = pathlib.Path(data_dir)
      

    img_height = 640
    img_width = 640
    
    class_names = ['Amethyst', 'Boron', 'Galena', 'Halite', 'Chalcopyrite',
                   'Chromite', 'Quartz', 'Malachite', 'Obsidian', 'Pyrite'] 
    
    model = load_model("C:/Users/kumralf/Desktop/nyp_mineral/models/model_mineral.h5")
    

    img = img.resize((img_height, img_width))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis
    
    predictions = model.predict(img_array)
    
    score = tf.nn.softmax(predictions[0])
    class_names[np.argmax(score)]
    print(
        "This image most likely belongs to {} with a {:.2f} percent."
        .format(class_names[np.argmax(score)], 100 * np.max(score))
    )

    return class_names[np.argmax(score)], int(round(100 * np.max(score)))

