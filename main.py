"""This is a program that uses a set of data with 5 different attributes to
build a classifier that determines whether or not a set of data is real or
fake and outputs the percentage of accuracy.

Written by: Sarah Labrosse
Student Number: 20096507
Date: 2019-02-01
"""

import createData
import testClass
import buildClass
import ast

def main():
    '''Program execution starts here.'''

    urlWeb = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00267/data_banknote_authentication.txt';

    data = createData.separateData(urlWeb, ',')

    createData.writeData(data[0], data[1])

    # this is used so that the 2D list isn't read as a string from file
    with open("training.txt", "r") as file:
        trainingFile = ast.literal_eval(file.read())

    with open("testing.txt", "r") as file:
        testingFile = ast.literal_eval(file.read())

    midpoints = buildClass.buildClassifier(trainingFile)

    testData = testClass.testingData(testingFile, midpoints)

    # this is the total number of real data sets found by classifier
    totalOnes = testData[0]

    # this is the total number of fake data sets found by classifier
    totalZeros = testData[1]

    accuracy = testClass.testAccuracy(data, totalOnes, totalZeros)

    print('\nData is being imported from\n' + urlWeb + '.\n')

    print("The accuracy of finding real data is", accuracy[0], "%")
    print("The accuracy of finding fake data is", accuracy[1], "%")


main()
