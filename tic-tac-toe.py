board = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

def display(sample):
    for i in range(3):
        for j in range(3):
            print(sample[i][j], end=' ')
        print('\n')

def x_action(target,a,b):
    if (target[a][b] == '*'):
        target[a][b] = '0'
    elif (target[a][b] == '0' or target[a][b] == '1'):
        print ("Sorry, the location has been choosen! Choose again")
        cor_col = input("Column: ")
        val_cor_col = int (cor_col)
        cor_row = input("Row: ")
        val_cor_row = int(cor_row)
        x_action(target,val_cor_col,val_cor_row)

def y_action(target,a,b):
    if (target[a][b] == '*'):
        target[a][b] = '1'
    elif (target[a][b] == '0' or target[a][b] == '1'):
        print ("Sorry, the location has been choosen! Choose again")
        cor_col = input("Column: ")
        val_cor_col = int (cor_col)
        cor_row = input("Row: ")
        val_cor_row = int(cor_row)
        y_action(target,val_cor_col,val_cor_row)


def checkInput(a):
    if a<0 or a>2:
        new_a = int(input ("The loction is not effective, choose again"))
        checkInput(new_a)
        a = new_a

def x_check(target):
    for i in range (3):
        if(target[i][0] == target[i][1] == target[i][2] == '0' or target[0][i] == target[1][i] == target[2][i] == '0' or target[0][0] == target[1][1] == target[2][2] == '0'):
            print ("X win!")
            quit()

def y_check(target):
    for i in range (3):
        if(target[i][0] == target[i][1] == target[i][2] == '1' or target[0][i] == target[1][i] == target[2][i] == '1' or target[0][0] == target[1][1] == target[2][2] == '1'):
            print ("Y win!")
            quit()

display(board)

while True:    
    val_col = int(input("Column: "))
    checkInput(val_col)
    val_row = int(input("Row: "))
    checkInput(val_row)
    x_action(board,val_col,val_row)
    print ('\n')
    display(board)
    x_check(board)
    val_col = int(input("Column: "))
    checkInput(val_col)
    val_row = int(input("Row: "))
    checkInput(val_col)
    checkInput(val_row)
    y_action(board,val_col,val_row)
    print ('\n')
    display(board)
    y_check(board)
