import sys

import numpy as np


class SearchAlgorithm:

    def ed(self, x, y):
        n = len(x)
        m = len(y)

        # Zero matrix
        w = np.zeros((n + 1, m + 1))

        # Init, first column
        for j in range(1, n + 1):
            w[j, 0] = w[j - 1, 0] + 1

        # Computing partial edit distances between xi and yj
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                w[i, j] = float('inf')
                if x[i - 1] == y[j - 1]:
                    # delta = 0  # No cost, same letter
                    w[i, j] = w[i - 1, j - 1]
                else:
                    w[i, j] = 1 + np.sort(np.array([w[i - 1, j - 1], w[i - 1, j], w[i, j - 1]]))[0]
                """else:
                    delta = 1
                if w[i - 1, j] + 1 < w[i, j]:
                    w[i, j] = w[i - 1, j] + 1  # Delete character
                if w[i - 1, j - 1] + delta < w[i, j]:
                    w[i, j] = w[i - 1, j - 1] + delta  # Substitute character (0 if same)
                if w[i, j - 1] + 1 < w[i, j]:
                    w[i, j] = w[i, j - 1] + 1  # Insert character
                """

        return w

    def printMatrix(self, matrix, x, y):
        # print('\n'.join([''.join(['{:4}'.format(item) for item in row])
        # for row in matrix]))
        output = "           "
        for c in y:
            output += c + "   "
        print(output + "\n")
        output = ""
        for i in range(len(x) + 1):
            if i == 0:
                output += "       "
                for l in matrix[i]:
                    output += str(int(l)) + "   "
            else:
                output += x[i - 1] + "      "
                for l in matrix[i]:
                    output += str(int(l)) + "   "
            output += "\n"
        print(output)

    def checkError(self, w, k):
        counter = 0
        for i in w[-1]:
            if i <= k:
                counter += 1
        print("There are " + str(counter) + " number of occurrences that allows the error, k = " + str(k))


s = SearchAlgorithm()
string1 = "tomorr"
string2 = "two"
matrix = s.ed(string2, string1)
s.printMatrix(matrix, string2, string1)
s.checkError(matrix, 2)
