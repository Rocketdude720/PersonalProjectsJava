# -*- coding: utf-8 -*-
"""TF NN Perceptron.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vovkRNqMPYr2YYlM0lg212eV7Va_H415
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 2.x  # this line is not required unless you are in a notebook
import tensorflow as tf #Tensorflow handles the Training and Testing
from tensorflow import keras #Keras handles the importing of Data
import numpy as np #NumPy does funny math good
import matplotlib.pyplot as plt #MatPlotLib visualizes data

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data(path="mnist.npz") # loads MNIST Digits dataset and splits it into training and testing data

#Uses MatPlot to show the first digit
# plt.figure()
# plt.imshow(train_images[1])
# plt.show()

#Data Formatting: Converts the 0-255 int range of each pixel to a 0-1 float  
train_images = train_images / 255.0
test_images = test_images / 255.0
#Note: You can't use /= for some reason. Something about datatype mismatch

#Creating the Network: Sets up the NN Structure, connection types, and activation functions
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)), #Sets input layer equal to flattened 28x28       
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(10, activation='softmax'),                     
])

#Compile the Model: Sets up the models loss function, optimizer, and metrics
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics = ['accuracy'])

#Training the model: feeds in training images and labels to create preliminary connections
model.fit(train_images, train_labels, epochs=12) 
# Note: Epochs are the number of thimes the data is fed through the system
#       More epochs are not necessarily good as you risk overfitting a model which is where the model is 
#       more or less remembering the data rather than developing useful prediction about it

#Testing the model: uses testing images and labels to verify accuracy of training
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=1) 

print('Test accuracy:', test_acc)

def getNum():
  while True:
    num = input("Pick a number from 0 to "+ str(test_images.shape[0])+ ": ")
    if num.isdigit():
      num = int(num)
      if 0 <= num <= test_images.shape[0]:
        return num
    else:
      print("Try again...")
def display(num):
  plt.figure()
  plt.imshow(test_images[num])
  plt.axis('off')
  plt.show()
def img_to_pixel():
  pass
# custom_digit = img_to_pixel("digit.jpg")

while True:
  num = getNum()
  prediction = model.predict(test_images)
  display(test_images[num])
  print(prediction.shape)
  print(np.argmax(prediction[0]))
  # print("The Neural Network thinks its a", np.argmax(prediction[0]), "with a", prediction[0][np.argmax(prediction[0])], "Confidence")

