#Game of snake and snack Portotype
import random
class snake:
    length = 1
    x_location = [3]
    y_location = [6]
    current_location = [3][6]
board = [['*', '*', '*', '*', '*', '*','*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*','*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*','*', '*', '*', '*', '*', '*', '*', '*'],['*', '*', '*', '*', '*', '*','*', '*', '*', '*', '*', '*', '*'],['*', '*', '*', '*', '*' ,'*', '*','*', '*', '*', '*', '*', '*'],['*', '*', '*', '*', '*', '*','*', '*', '*', '*', '*', '*', '*'],['*', '*', '*', '*', '*', '*','*', '*', '*', '*', '*', '*', '*']]
boardList = [[0,1,2,3,4,5,6,7,8,9,10,11,12],[0,1,2,3,4,5,6,7,8,9,10,11,12],[0,1,2,3,4,5,6,7,8,9,10,11,12],[0,1,2,3,4,5,6,7,8,9,10,11,12], [0,1,2,3,4,5,6,7,8,9,10,11,12],[0,1,2,3,4,5,6,7,8,9,10,11,12],[0,1,2,3,4,5,6,7,8,9,10,11,12]]
def eat(snake):
    snake.length += 1
def generate_snack(board):
    a = random.randint(0,6)
    b = random.randint(0,12)
    if board[a][b] == '*':
        board[a][b] = 'S'
    else:
        generate_snack(board)
def display(board,snake):
    for i in range(7):
        for j in range(13):
            if i in snake.x_location and j in snake.y_location:
                print ('X', end=' ')
            else:
                print(board[i][j] , end=' ')
        print('\n')
def move(snake,board):
    direction = input("Move:")
    if (direction ='w'):
        snake.length+=1

hunter = snake()
generate_snack(board)
display(board,hunter)
