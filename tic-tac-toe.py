board = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

def display(sample):
    for i in range(3):
        for j in range(3):
            print(sample[i][j], end=' ')
        print('\n')

def x_action(target,a,b):
    if (target[a][b] == '*'):
        target[a][b] = 'X'
    elif (target[a][b] == 'X' or target[a][b] == 'Y'):
        print ("Sorry, the location has been choosen! Choose again")
        cor_col = input("Column: ")
        val_cor_col = int (cor_col)
        val_cor_col = checkCol(val_cor_col)
        cor_row = input("Row: ")
        val_cor_row = int(cor_row)
        val_cor_row = checkRow(val_cor_row)
        x_action(target,val_cor_row,val_cor_col)

def y_action(target,a,b):
    if (target[a][b] == '*'):
        target[a][b] = 'Y'
    elif (target[a][b] == 'X' or target[a][b] == 'Y'):
        print ("Sorry, the location has been choosen! Choose again")
        cor_col = input("Column: ")
        val_cor_col = int (cor_col)
        val_cor_col = checkCol(val_cor_col)
        cor_row = input("Row: ")
        val_cor_row = int(cor_row)
        val_cor_row = checkRow(val_cor_row)
        y_action(target,val_cor_row,val_cor_col)

def checkCol(a):
    if a<0 or a>2:
        new_a = int(input ("The loction is not effective, choose again" +'\nNew Column: '))
        return checkCol(new_a)
    else:
        print ("Selected Column " + str(a))
        return a

def checkRow(a):
    if a<0 or a>2:
        new_a = int(input ("The loction is not effective, choose again" +'\nNew Row: '))
        return checkRow(new_a)
    else:
        print ("Selected Row " + str(a))
        return a

def x_endCheck(target):
    for i in range (3):
        if(target[i][0] == target[i][1] == target[i][2] == 'X' or target[0][i] == target[1][i] == target[2][i] == 'X' or target[0][0] == target[1][1] == target[2][2] == 'X'):
            print ("X win!")
            quit()
        else:
            for a in range (3):
                for b in range(3):
                    if board[a][b] == '*':
                        return False
    print("Draw!")
    quit()

def y_endCheck(target):
    for i in range (3):
        if(target[i][0] == target[i][1] == target[i][2] == 'Y' or target[0][i] == target[1][i] == target[2][i] == 'Y' or target[0][0] == target[1][1] == target[2][2] == 'Y'):
            print ("Y win!")
            quit()
        else:
            for a in range (3):
                for b in range(3):
                    if board[a][b] == '*':
                        return False
    print("Draw!")
    quit()

display(board)
while True:    
    val_col = int(input("Column: "))
    val_col = checkCol(val_col)
    val_row = int(input("Row: "))
    val_row = checkRow(val_row)
    x_action(board,val_row,val_col)
    print ('\n')
    display(board)
    x_endCheck(board)
    val_col = int(input("Column: "))
    val_col = checkCol(val_col)
    val_row = int(input("Row: "))
    val_row = checkRow(val_row)
    y_action(board,val_row,val_col)
    print ('\n')
    display(board)
    y_endCheck(board)
