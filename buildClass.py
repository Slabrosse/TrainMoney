"""This is the buildClass module that builds the classifier in preparation
to be tested

This module contains one function to build the classifier by finding the
midpoints: the average between both the real and the fake data set.

- buildClassifier()

Written by: Sarah Labrosse
Student Number: 20096507
Date: 2019-02-01
"""
def buildClassifier(trainingData):
    """
    :param trainingData:
        - set of data with randomly sorted even number of fake and real data
    :return:
        - list of midpoints calculated from the average of real and fake attributes
    """

    # loops through data and deletes the 5th attribute (0 or 1)
    for i in range(len(trainingData)):
        del trainingData[i][4]

    attributeList = [0, 0, 0, 0]

    # appends the all attributes across data into
    for num in range(len(trainingData)):
        for i in range(len(trainingData[num])):
            attributeList[i] += (trainingData[num][i])

    # this finds the midpoint across the data (real and fake)
    for i in range(len(attributeList)):
        attributeList[i] /= len(trainingData)

    return attributeList

if __name__ == "__main__":

    #this tests that the function is properly calculating the midpoints
    data = [[-2, 4, -1, -4, 1], [-1, -3, 1, 5, 1],
            [2, -7, 3, -4, 0], [7, -8, 4, -2, 0]]
    
    #should print [1.5, -3.5, 1.75, -1.25]
    print(buildClassifier(data)) 

    data = [[7.34, 8.234, -1.253, -4.123, 1],
            [-5.623, -3.21, -0.231, 5.514, 1],
            [6.2361, -5.163, 3.615, -2.634, 0],
            [7.982, -8.452, 7.234, -4.234, 0]]

    # should print [3.981525, -2.14775, 2.34125, -1.36925]
    print(buildClassifier(data))  



