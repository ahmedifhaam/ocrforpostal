import cv2
import os
import numpy as np
import tensorflow as tf
from tensorflow import keras

# import pytesseract

def preprocess(imgpath):
    print(imgpath)
    img = cv2.imread(imgpath)

    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # denoised = cv2.medianBlur(img,3)

    denoised = cv2.GaussianBlur(gray_img,(5,5),0)



    gaussianadaptivethresimg = cv2.adaptiveThreshold(denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                                     cv2.THRESH_BINARY_INV, 11, 2)
    gaussianadaptivethresimg = cv2.erode(gaussianadaptivethresimg,(5,5),12)
    gaussianadaptivethresimg = cv2.dilate(gaussianadaptivethresimg,(10,10),25)

    return cv2.resize(gaussianadaptivethresimg,(32,32))



path = './segmented chars/grouped'
files = os.listdir(path)

trainingimages = []
trainingimages2D =[]
traininglabels = []

labelmapps = {
    '9' : 0,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    'A' : 6,
    'B' : 7,
    'C' : 8,
    'D' : 9,
    'E' : 10,
    'F' : 11,
    'G' : 12,
    'H' : 13,
    'I' : 14,
    'J' : 15,
    'K' : 16,
    'L' : 17,
    'M' : 18,
    'N' : 19,
    'O' : 20,
    'P' : 21,
    'Q' : 22,
    'R' : 23,
    'S' : 24,
    'T' : 25,
    'U' : 26,
    'V' : 27,
    'W' : 28,
    'X' : 29,
    'Y' : 30,
    'Z' : 31,

    # '9' : 32,
}

def trainandtest():

    for file in files:
        if os.path.isdir(os.path.join(path,file) ):
            # print(file.__str__()+" folder ")
            temppath = os.path.join(path,file)
            # print(temppath)
            tempfiles = os.listdir(temppath)
            for imgfile in tempfiles:
                if imgfile.endswith(".jpeg"):
                    print(file)
                    preprocessed = preprocess(os.path.join(temppath,imgfile))
                    reshaped = preprocessed.reshape(1024).astype(np.float32)
                    trainingimages2D.append((preprocessed))
                    print("=============================================================")
                    print (reshaped)
                    trainingimages.append(reshaped)
                    traininglabels.append(file)

    np.savetxt("trainingImages.csv",trainingimages,delimiter=',',fmt="%.0f")
    np.savetxt("traininglabels.csv",traininglabels,delimiter=',',fmt='%s')

    traininglabelsMod =[]
    for a in traininglabels:
        traininglabelsMod.append(labelmapps[a])

    name = "H.jpeg"
    imre = cv2.imread(name)
    preprocessedtest = preprocess(name)
    cv2.imshow("prec",preprocessedtest)
    reshapedtest = preprocessedtest.reshape(1024).astype(np.float32)
    #
    testdataarray = [reshapedtest]
    #

    #call ANN
    KANN(trainingimages,traininglabelsMod,testdataarray)

    #call kNearest
    kNearest(trainingimages,traininglabelsMod,testdataarray)

    #tesseract
    tesseract(imre)

    cv2.waitKey(0)


def kNearest(trainingimages,traininglabelsMod,testdataarray):
    # # using the k nearest neibour
    print("===========KNN==============================")
    knn = cv2.ml.KNearest_create()
    knn.train(np.array(trainingimages),cv2.ml.ROW_SAMPLE,np.array(traininglabelsMod))
    a, b, c, d = knn.findNearest(np.array(testdataarray), k=5)
    print(a,b,c,d)
    print("============================================")

def KANN(trainingimages,traininglabelsMod,testdataarray):
    # # using tensorflow

    # tf.reset_default_graph()
    #
    # classifier = keras.Sequential()
    # classifier.add(keras.layers.Dense(1024)) # # input layer for size of 32 32
    # classifier.add(keras.layers.Conv1D(8,(3),activation='relu'))
    # # classifier.add(keras.layers.Conv1D(32,(3,3),activation='relu'))
    # classifier.add(keras.layers.MaxPooling1D(pool_size= (2)))
    #
    # # classifier.add(keras.layers.Flatten())
    # classifier.add(keras.layers.Dense(units=64,activation='relu'))
    # classifier.add(keras.layers.Dense(units=32,activation='sigmoid')) # # ouput layer with output classes of 32

    # model = classifier

    model = keras.Sequential([
        keras.layers.Dense(1024),
        keras.layers.Dense(512,activation=tf.nn.relu),
        # keras.layers.Conv1D(1024,(3),input_shape=(None,32),activation=tf.nn.relu),
        # keras.layers.Dropout(0.2),
        # keras.layers.Dense(600,activation=tf.nn.relu),
        # keras.layers.Dense(300,activation=tf.nn.relu),
        # keras.layers.Dense(150,activation=tf.nn.relu),
        # keras.layers.Dropout(0.4),
        # keras.layers.Dense(75,activation=tf.nn.relu),
        keras.layers.Dense(32,activation=tf.nn.softmax)
    ])

    model.compile(optimizer=tf.train.AdamOptimizer(),
                  loss='sparse_categorical_crossentropy',
                  metics=['accuracy'])
    model.fit(np.array(trainingimages),np.array(traininglabelsMod))


    predictions = model.predict(np.array(testdataarray))

    print("===========ANN==============================")
    print(np.argmax(predictions[0]))
    print()

    print(predictions)
    print("============================================")

def tesseract(img):
    print("===========TES==============================")
    # result = pytesseract.image_to_string(img,lang="sin")
    # print(":"+result)
    print("============================================")