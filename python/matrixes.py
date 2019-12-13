
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
#getElementInMatrix(matrixes, 66)


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
#printMatrixInSpiralForm(matrixes)



def printDuplicate(ele):
    dup = {}
    for i in range(len(ele)):
        if ele[i] in dup:
            dup[ele[i]] = dup[ele[i]]+1
        else:
            dup[ele[i]] = 1
    for i,j in dup.items():
        if dup[i] > 1:
            print i

ele = [1,2,2,2,2,4,5,4,4,7,8,8]
#printDuplicate(ele)

def setleftmostunsetbit(n):
    if not (n & n+1):
        return n
    temp = n
    count =0
    pos = 0
    # performing right shift and incresing the pos if the bit is unset
    while(temp):
        if not temp&1:
            pos +=1
        count +=1
        temp >>=1
    return n|1<<pos

# Driver Function
n = 17
#print(setleftmostunsetbit(n))
#print 7&8

def numOfBits(n):
    temp =n
    count = 0
    # performing right shift and incresing the count for each bit
    while(temp):
        temp >>= 1
        count += 1
    return count

#print numOfBits(1294)
n =1221
def checkPalindrom(n):
    x = n
    i=0
    while(x>0):
        i = i*10+x%10
        x = x/10
    if n==i:
        return True
    return False

#print checkPalindrom(1221)




def nextGreaterEle(arr):
    i=0
    while(i<len(arr)):
        second_max = None
        for j in range(i+1, len(arr)):
            if (arr[j]>arr[i]):
                second_max = arr[j]
                break
        print "The second highest numbe for %s is %s"%(arr[i],second_max)
        i+=1
arr = [4, 5, 2, 25, 7, 32, 8, 6]
#nextGreaterEle(arr)

# # Output:
# The second highest numbe for 4 is 5
# The second highest numbe for 5 is 25
# The second highest numbe for 2 is 25
# The second highest numbe for 25 is 32
# The second highest numbe for 7 is 32
# The second highest numbe for 32 is None
# The second highest numbe for 8 is None
# The second highest numbe for 6 is None

def stringToNum(string):
    res = 0
    for i in xrange(len(string)):
        # ord function is used to find the unicode of each char.. which is nothing but the ascii char of charecter
        if (ord(string[i])<48 or ord(string[i])>57) and (ord(string[i])!=43 and ord(string[i])!=45):
            break
        if ord(string[i]) != 43 and ord(string[i]) != 45:
            res = res * 10 + (ord(string[i]) - ord('0'))
    return res


# Driver program
string = "-88297 248252140B12 37"
output = 88297
string = "75 6"
output - 75
string = "+349A756"
output = 349
print stringToNum(string)




# def unsetAllBitsExceptMSB(n):
#     x = 1
#     #findig the largest power of 2 smaller than n
#     while(x<=n):
#         x*=2
#     return x/2

#print unsetAllBitsExceptMSB(8)