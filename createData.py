"""This is the createData module to create and write data to a file

This module contains two functions, one for scraping data and appending it to
a list, and the other writes those data sets to their own file.

- separateData()
- writeData()

Written by: Sarah Labrosse
Student Number: 20096507
Date: 2019-02-01
"""

import webScraper
import urllib.request
import random

def separateData(urlWeb, separator=None):
    """ Scrapes the information from a website, randomly shuffles the data and
then evenly splits the data between a list of training data and a list of
testing data to be used in building and testing the classifer.

    :param urlWeb:
        - url of the website being scraped
    :param separator:
        - whitespeace is used to separate elements
    :return:
        - set of training data with randomly sorted fake and real data
        - set of testing data with randomly sorted fake and real data
    """

    stream = urllib.request.urlopen(urlWeb)
    data = webScraper.get_all_data(stream, separator)

    random.shuffle(data)

    training = []
    testing = []

    #this randomly appends half the data to training and the other to testing
    for num in range(len(data)):
        randNum = random.randint(1, 10)

        if data[num][4] == 1:
            if randNum >= 5:
                testing.append(data[num])
            else:
                training.append(data[num])

        if data[num][4] == 0:
            if randNum >= 5:
                testing.append(data[num])
            else:
                training.append(data[num])

    return (training, testing)


def writeData(trainingData, testingData):
    ''' writes training and testing data each to their own file

    :param trainingData:
        - set of training data with randomly sorted fake and real data
    :param testingData:
        - set of testing data with randomly sorted fake and real data
    :return:
        - none
    '''

    trainingFile = open("training.txt", "w")

    trainingFile.write(str(trainingData))

    trainingFile.close()

    testingFile = open("testing.txt", "w")

    testingFile.write(str(testingData))

    testingFile.close()

if __name__ == "__main__":
    urlWeb = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00267/data_banknote_authentication.txt'
    result = separateData(urlWeb, ',')
    trainingData = result[0]
    testingData = result[1]
    #should be a doubled nested loop with random data everytime
    print("trainingData:", trainingData) 
    print("testingData:", testingData)

    #this writes the file
    writeData(trainingData, testingData)

