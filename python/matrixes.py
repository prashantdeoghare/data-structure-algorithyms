
#get element in matixes
def getElementInMatrix(matrix, x):
    i=0
    j=len(matrix)-1
    if not matrix:
        print "Not a matrix"
    if x < matrix[0][0] or x> matrix[len(matrix)-1][len(matrix[0])-1]:
        print "%d not present in the matrix" % x
        return
    while(i<len(matrix)-1 and j>=0):
        if matrix[i][j] > x:
            print matrix[i][j]
            j = j-1
        if matrix[i][j] < x:
            print matrix[i][j]
            i+=1
        if matrix[i][j] ==x:
            print "Found at inder (%d, %d)"%(i,j)
            return
    print "%d not present in the matrix" %x
matrixes = [[11, 21, 31, 41, 51],
            [12, 22, 32, 42, 53],
            [13, 23, 33, 43, 54],
            [14, 24, 34, 44, 55],
            [15, 25, 35, 52, 56]]
getElementInMatrix(matrixes, 66)


#Printing elements of matrixes in spiral form
def printMatrixInSpiralForm(matrixes):
    fr = 0
    lr = len(matrixes)
    fc = 0
    lc = len(matrixes[0])
    while(fr < lr and fc <lc):
        for i in range(fc, lc):
            print(matrixes[fr][i])
        fr +=1
        for i in range(fr, lr):
            print(matrixes[i][lc-1])
        lc -= 1
        for i in range(lc-1, fc-1, -1):
            print(matrixes[lr-1][i])
        lr -= 1
        for i in range(lr-1, fr-1, -1):
            print(matrixes[i][fc])
        fc +=1
    return
matrixes = [[11, 21, 31, 41, 51],
            [12, 22, 32, 42, 53],
            [13, 23, 33, 43, 54],
            [14, 24, 34, 44, 55],
            [15, 25, 35, 52, 56]]
printMatrixInSpiralForm(matrixes)