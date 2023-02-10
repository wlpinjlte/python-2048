import random

def updateFiledToFill(board,freeField):
    fieldToChoose=random.randint(0,len(freeField)-1)
    board[freeField[fieldToChoose][0]][freeField[fieldToChoose][1]]=2

def endGame():
    pass

def move(board,direction):
    isMarge=[[False for i in range(len(board[0]))]for j in range(len(board))]
    maxX=len(board)-1
    maxY=len(board)-1
    if(direction=='left'):
        for x in range(len(board)):
            firstIteam=0
            positonToPlaceIteam=0
            while firstIteam<len(board[0]) and board[x][firstIteam]==0:
                firstIteam+=1
            if firstIteam==len(board):
                continue
            for i in range(len(board)-firstIteam):
                if(board[x][firstIteam + i]):
                    continue
                temp = board[x][firstIteam + i]
                board[x][firstIteam + i] = 0
                board[x][positonToPlaceIteam]=temp

                if positonToPlaceIteam>0 and isMarge[x][positonToPlaceIteam-1]==False and board[x][positonToPlaceIteam-1]==board[x][positonToPlaceIteam]:
                    board[x][positonToPlaceIteam-1]=board[x][positonToPlaceIteam-1]*2
                    board[x][positonToPlaceIteam]=0
                    isMarge[x][positonToPlaceIteam - 1]=True
                else:
                    positonToPlaceIteam+=1

    elif(direction=='right'):
        for x in range(len(board)):
            firstIteam=maxY
            positonToPlaceIteam=maxY
            while firstIteam>-1 and board[x][firstIteam]==0:
                firstIteam-=1
            if firstIteam==-1:
                continue
            for i in range(firstIteam+1):
                if(board[x][firstIteam - i]==0):
                    continue
                temp = board[x][firstIteam - i]
                board[x][firstIteam - i] = 0
                board[x][positonToPlaceIteam]=temp

                if positonToPlaceIteam<maxY and isMarge[x][positonToPlaceIteam+1]==False and board[x][positonToPlaceIteam+1]==board[x][positonToPlaceIteam]:
                    board[x][positonToPlaceIteam+1]=board[x][positonToPlaceIteam+1]*2
                    board[x][positonToPlaceIteam]=0
                    isMarge[x][positonToPlaceIteam + 1]=True
                else:
                    positonToPlaceIteam-=1
    elif (direction == 'up'):
        for y in range(len(board)):
            firstIteam=0
            positonToPlaceIteam=0
            while firstIteam<len(board) and board[firstIteam][y]==0:
                firstIteam+=1
            if firstIteam==len(board):
                continue
            for i in range(len(board)-firstIteam):
                if(board[firstIteam + i][y]==0):
                    continue
                temp = board[firstIteam + i][y]
                board[firstIteam + i][y] = 0
                board[positonToPlaceIteam][y]=temp

                if positonToPlaceIteam>0 and isMarge[positonToPlaceIteam-1][y]==False and board[positonToPlaceIteam-1][y]==board[positonToPlaceIteam][y]:
                    board[positonToPlaceIteam-1][y]=board[positonToPlaceIteam-1][y]*2
                    board[positonToPlaceIteam][y]=0
                    isMarge[positonToPlaceIteam - 1][y]=True
                else:
                    positonToPlaceIteam+=1
    elif (direction == 'down'):
        for y in range(len(board)):
            firstIteam=maxX
            positonToPlaceIteam=maxX
            while firstIteam>-1 and board[firstIteam][y]==0:
                firstIteam-=1
            if firstIteam==-1:
                continue
            for i in range(firstIteam+1):
                if(board[firstIteam - i][y]==0):
                    continue
                temp = board[firstIteam - i][y]
                board[firstIteam - i][y] = 0
                board[positonToPlaceIteam][y]=temp

                if positonToPlaceIteam<maxY and isMarge[positonToPlaceIteam+1][y]==False and board[positonToPlaceIteam+1][y]==board[positonToPlaceIteam][y]:
                    board[positonToPlaceIteam+1][y]=board[positonToPlaceIteam+1][y]*2
                    board[positonToPlaceIteam][y]=0
                    isMarge[positonToPlaceIteam + 1][y]=True
                else:
                    positonToPlaceIteam-=1

def tempPrint(board):
    for i in board:
        for j in i:
            print(j,end=" ")
        print()

board=[[0 for j in range(4)]for i in range(4)]
board[0][0]=2
board[0][1]=2
board[0][3]=2
board[0][2]=2
board[3][0]=2
board[1][0]=2
board[2][0]=2
print(tempPrint(board))
move(board,"up")
print(tempPrint(board))