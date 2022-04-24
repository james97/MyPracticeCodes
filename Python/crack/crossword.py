blank=' '
board=[[blank]*20 for i in range (20)]
# show the framework which is 20*20

#first step to print the matrix of 20*20
def printboard(board):
    for z in range(len(board)) :
        for q in range(len(board[z])) :
            print(board[z][q], end = ' ')
        print()

#Next step is to insert the first word into the matrix
def firstword(board,word):
    D=len(board)
    n=len(word)
    if n>D:
        return False #mention the precondition of the first word which is can not longer than the length of matrix
    for k in range(n):
        column=D//2-n//2+k #show the column of the word
        board[D//2][column]=word[k] #define the specific location of the first word
    return True

#Then define whether the location which is available to insert a new word
def checkvertical(board,word,row,col):
    if len(word)+row <= 20:     # check if the word can fit into the board
        for i in range (len(word)):
            boardletter=board[row+i][col]
            if word[i] == boardletter:
                for a in range (len(word)):
                    #define the left and right, if there has chars already,then the insert is false
                    left = board[row+a][col-1]
                    right = board[row+a][col+1]
                    if left != ' ' or right != ' ':
                        if a != i:
                            return False
                if board[row-1][col] != ' ' or board[row+len(word)][col] != ' ':
                    return False
                # check if the program want to change the existing word
                for b in range (len(word)):
                    if board[row+b][col] != ' ' and board[row+b][col] != word[i]:
                        return False
                return True
            elif boardletter==' ':
                continue
            elif boardletter != word[i]:
                return False
    return False

#Next step is very similar to checkvertical, here we want to check horizontal which confirm the location whether or-
#not insert word horizontally.
def checkhorizontal(board,word,row,col):
    if len(word)+col <= len(board):
        for i in range (len(word)):
            boardletter=board[row][col+i]
            if word[i] == boardletter:
                for a in range (len(word)):
                    # define the up and down, if there has chars already,then the insert is false
                    up = board[row-1][col+a]
                    down = board[row+1][col+a]
                    if up != ' ' or down != ' ':
                        if a != i:
                            return False
                if board[row][col-1] != ' ' or board[row][col+len(word)] != ' ':
                    return False
                # check if the program want to change the existing word
                for b in range(len(word)):
                    if board[row][col+b] != ' ' and board[row][col+b] != word[i]:
                        return False
                return True
            if boardletter==' ':
                continue
            if boardletter != word[i]:
                return False
    return False

#based on the result form last part,we can add the word vertically
def addveretical(board,word):
    for a in range(20):
        for b in range(20):
            if checkvertical(board,word,b,a):
                for i in range(len(word)):
                    board[i+b][a] = word[i]
                return True
    return False

#then insert the word horizontally
def addhorizontal(board,word):
    for a in range(len(board)):
        for b in range(len(board)):
            if checkhorizontal(board,word,a,b):
                for i in range(len(word)):
                    board[a][i+b] = word[i]
                return True
    return False

#the last step is to write the shell to call all the functions above in order to execute the program.
def crossword(L):
    blank=' '
    board = [[blank] * 20 for i in range(20)] #rewrite the framework 20*20 again
    firstword(board,L[0])
    for i in range (1,len(L)):
        # show the time to add the vertical words or horizontal words
        if i % 2 == 1:
            addveretical(board,L[i])
        else:
            addhorizontal(board,L[i])
    printboard(board)
# crossword(['adhjsgfuiwkwag','ehjiolejht','kdfshjkdfh','hjek','catftiusrjmrmkl','usighl', "kwayi"])
crossword(["addle", 'apple', 'clowning', 'incline', 'plan', 'burr'])
# crossword(["apple", 'addle', 'loon', 'clowning', 'incline', 'plan'])