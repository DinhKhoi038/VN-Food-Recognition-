#Import thu vien

from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import os
import numpy as np
import tensorflow as tf
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.optimizers import SGD, RMSprop
from keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.utils import validation
from sklearn import preprocessing
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array
from tensorflow.keras.preprocessing.image import ImageDataGenerator

#class ImageDataGenerator de chinh sua anh
train_datagen = ImageDataGenerator(rescale = 1./255, shear_range = 0.2, zoom_range = 0.2, horizontal_flip= True)

training_set = train_datagen.flow_from_directory('d:\Downloads\FoodRec\Images\Train', target_size=(150,150), batch_size=32, class_mode = 'categorical' )

#Tao bo du lieu validation
valid = train_datagen.flow_from_directory('d:\Downloads\FoodRec\Images\Validate', target_size=(150,150), batch_size = 32, class_mode = 'categorical')

#Labels trong training set
training_set.class_indices

#Labels trong validate
valid.class_indices
'''
#tao mang CNN
model = Sequential()
model.add(Conv2D(32,(3,3), activation = 'relu', kernel_initializer = 'he_uniform', input_shape = (150,150,3)))
model.add(Conv2D(32,(3,3), activation = 'relu', kernel_initializer = 'he_uniform', padding = 'same'))
model.add(MaxPooling2D(2,2))

model.add(Conv2D(64,(3,3), activation='relu', kernel_initializer='he_uniform', padding='same')) 
model.add(Conv2D(64,(3,3), activation='relu', kernel_initializer='he_uniform', padding='same'))
model.add(MaxPooling2D(2,2))

model.add(Conv2D(64,(3,3), activation='relu', kernel_initializer='he_uniform', padding='same')) 
model.add(Conv2D(64,(3,3), activation='relu', kernel_initializer='he_uniform', padding='same'))
model.add(MaxPooling2D(2,2))

model.add(Conv2D(128,(3,3), activation='relu', kernel_initializer='he_uniform', padding='same')) 
model.add(Conv2D(128,(3,3), activation='relu', kernel_initializer='he_uniform', padding='same'))
model.add(MaxPooling2D(2,2))

#Flatten du lieu
model.add(Flatten())

#Tao lop an thu nhat voi 128 output
model.add(Dense(128, activation = 'relu', kernel_initializer = 'he_uniform'))
model.add(Dropout(0.2))

#Tao lop an thu hai voi 3 tin hieu ra
model.add(Dense(30, activation = 'softmax'))
model.summary()

#Bien dich compile
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
history = model.fit(training_set, epochs = 50, batch_size=64, verbose = 1, validation_data = valid, callbacks = [EarlyStopping(monitor='val_loss', patience=30)])

#Danh gia do chinh xac
Score = model.evaluate(training_set, verbose = 0)
print('train loss', Score[0])
print('train accuracy', Score[1])

#save h5 file
model.save("FoodRec.h5")'''

model_CNN = load_model('D:\Downloads\FoodRec3.h5')

test= "d:\Downloads\Test2"

for i in os.listdir(test):
  img = load_img(test+'/'+i, target_size=(150,150))
  plt.imshow(img)
  img=img_to_array(img)
  img=img.astype('float32')
  img= img/255
  img = np.expand_dims(img, axis = 0)
  result = model_CNN.predict(img)
  if round(result[0][0]) == 1:
    prediction = 'Bánh bèo'
  if round(result[0][1]) == 1:
    prediction = 'Bánh bột lọc'
  if round(result[0][2]) == 1:
    prediction = 'Bánh căn'
  if round(result[0][3]) == 1:
    prediction = 'Banh canh'
  if round(result[0][4]) == 1:
    prediction = 'Bánh chưng' 
  if round(result[0][5]) == 1:
    prediction = 'Bánh cuốn'
  if round(result[0][6]) == 1:
    prediction = 'Bánh đúc'
  if round(result[0][7]) == 1:
    prediction = 'Bánh giò'
  if round(result[0][8]) == 1:
    prediction = 'Bánh khọt'
  if round(result[0][9]) == 1:
    prediction = 'Bánh mì'
  if round(result[0][10]) == 1:
    prediction = 'Bánh pía'
  if round(result[0][11]) == 1:
    prediction = 'Bánh tét'
  if round(result[0][12]) == 1:
    prediction = 'Bánh tráng nướng'
  if round(result[0][13]) == 1:
    prediction = 'Bánh xèo'
  if round(result[0][14]) == 1:
    prediction = 'Bún bò huế'
  if round(result[0][15]) == 1:
    prediction = 'Bún đậu mắm tôm' 
  if round(result[0][16]) == 1:
    prediction = 'Bún mắm'
  if round(result[0][17]) == 1:
    prediction = 'Bún riêu'
  if round(result[0][18]) == 1:
    prediction = 'Bún thịt nướng'
  if round(result[0][19]) == 1:
    prediction = 'Cá kho tộ'
  if round(result[0][20]) == 1:
    prediction = 'Canh chua'
  if round(result[0][21]) == 1:
    prediction = 'Cao lầu'
  if round(result[0][22]) == 1:
    prediction = 'Cháo lòng'
  if round(result[0][23]) == 1:
    prediction = 'Cơm tấm'
  if round(result[0][24]) == 1:
    prediction = 'Gỏi cuốn'
  if round(result[0][25]) == 1:
    prediction = 'Hủ tiếu'
  if round(result[0][26]) == 1:
    prediction = 'Mì Quảng' 
  if round(result[0][27]) == 1:
    prediction = 'nem chua'
  if round(result[0][28]) == 1:
    prediction = 'Phở'
  if round(result[0][29]) == 1:
    prediction = 'Xôi xéo'
  print("Đây là :", prediction)
  plt.show()



