#!/usr/bin/python

from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture, output_image
from ClassifyNB import classify

import numpy as np
import pylab as pl

import os

def main():
    features_train, labels_train, features_test, labels_test = makeTerrainData()

    ### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
    ### in together--separate them so we can give them different colors in the scatterplot,
    ### and visually identify them
    grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
    bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
    grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
    bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


    # You will need to complete this function imported from the ClassifyNB script.
    # Be sure to change to that code tab to complete this quiz.
    clf = classify(features_train, labels_train)
    print('Python Naive Bays Example')

    accuracy = clf.score(features_test, labels_test)
    print('Accuracy score: {}'.format(accuracy))


    ### draw the decision boundary with the text points overlaid
    prettyPicture(clf, features_test, labels_test)
    output_image("naive_bayes.png", "png", open("naive_bayes.png", "rb").read())
    os.system('display naive_bayes.png &')


if __name__ == '__main__':
    main()

