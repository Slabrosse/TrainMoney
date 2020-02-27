'''This is the testClass module that tests the accuracy of the classifier in
determining if a data set is real or fake.

This module contains two different functions, one for testing the classifier
data and another to assess the accuracy.

- testingData()
- testAccuracy()

Written by: Sarah Labrosse
Student Number: 20096507
Date: 2019-02-01
'''

import random

def testingData(data, midpoints):
    """
    :param data:
        - list of data sets with even amount of real and fake data
    :param midpoints:
        - average for all attributes used to test the classifier
    :return:
        - number of real data sets found in testing data by classifier
        - number of fake data sets found in testing data by classifier
    """

    # this deletes the fifth attribute (0 or 1)
    for i in range(len(data)):
        del data[i][4]

    # counts number of fakes for each attribute
    countZero = [0, 0, 0, 0]

    # counts number of reals for each attribute
    countOne = [0, 0, 0, 0]

    # counts total real samples found in classifier
    totalReal = 0

    # counts total fake samples found in classifier
    totalFake = 0

    randomNum = random.randint(1,500)

    # this counts the number of real and fake data sets
    for i in range(len(data)):
        for j in range(len(data[i])):
            # if value is greater than attribute value then classified as fake
            if data[i][j] >= midpoints[j]:
                countZero[j] += 1

            else:
                countOne[j] += 1

        #if there are more fake than real attributes, data set is fake
        if sum(countZero) > sum(countOne):
            totalFake += 1

        elif sum(countOne) > sum(countZero):
            totalReal += 1

        # this is used to evenly split data between real and fake when tied
        elif sum(countOne) == sum(countZero):
            if randomNum >= 250:
                totalReal += 1
            else:
                totalFake += 1

        # this resets the attributes
        countZero = [0, 0, 0, 0]

        countOne = [0, 0, 0, 0]

    return totalReal, totalFake


def testAccuracy(data, totalOnes, totalZeros):
    """

    :param data:
        - this is the complete set of unscrambled data scraped from the website
    :param totalOnes:
        - this is the total number of real data sets found from 'data'
    :param totalZeros:
        - this is the total number of fake data sets found from 'data'
    :return:
        - percent accuracy of finding the real data
        - percent accuracy of finding the fake data
    """

    #classAccuracyFake, classAccuracyReal = 0, 0

    countFake = 0

    countReal = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j][4] == 0:
                countFake += 1
            else:
                countReal += 1

    classAccuracyReal = (totalOnes * 100) / countReal
    classAccuracyFake = (totalZeros * 100) / countFake

    return classAccuracyReal, classAccuracyFake


if __name__ == "__main__":
    # this tests the classifier
    data = [[7.34, 8.234, -1.253, -4.123, 1],
            [-5.623, -3.21, -0.231, 5.514, 1],
            [6.2361, -5.163, 3.615, -2.634, 0],
            [7.982, -8.452, 7.234, -4.234, 0]]

    midpoints = [3.981525, -2.14775, 2.34125, -1.36925]

    result = testingData(data, midpoints)

    totalOnes = result[0]

    print("totalOnes", totalOnes)

    totalZeros = result[1]

    print("totalZeros", totalZeros)

    data = [[-2.04, 4.432, -1.234, 5.745, 1],
            [-1.2342, -3.234, .3452, 5.1242, 1],
            [2.345, -7.567, 5.234, 8.6356, 0],
            [7.2342, -8.234, 4.234, 6.456, 0],
            [4.742, 3.414, 5.234, 7.234, 1]]

    testAccuracy(data, totalOnes, totalZeros)
