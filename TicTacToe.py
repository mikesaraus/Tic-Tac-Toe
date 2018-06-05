from IPython.display import clear_output #to clear the output (specific to Jupyter notebooks and ipython)
from random import randint

def draw(board):
    for num in range(0,3):
        for n in range(0,3):
            print("{:^3s}".format(board[num][n]),end='')
            if n != 2:
                print("|", end='')
        if num != 2:
            print("\n"+ 10 * "-")
    # this contain error in the grader tool at edx but this works fine here and all keyword and functions and in used
        # tell me if i am wrong, I am confident with my code @ mizkie98@gmail.com
    
def available(location, board):
    isAvailable = False
    for n in board:
        for num in n:
            if num == location:
                isAvailable = True
                break
    return isAvailable
    

def mark(player, location, board):
    for n in board:
        for i in range(0,len(board)):
            if n[i] == location:
                n[i] = player
                break
    return board # Seriously? in the discription their none to return and the require keywords and function return is required... ok fine make it clear. Thanks :)
        
def check_win(board):
    mark = ['X','O']
    win = False
    for n in range(0,3):
        for m in range(0,2):
            if (board[n][0] == mark[m]) and (board[n][1] == mark[m]) and (board[n][2] == mark[m]): # across winner
                win = True
                break
            if (board[0][n] == mark[m]) and (board[1][n] == mark[m]) and (board[2][n] == mark[m]): # down winner
                win = True
                break

            if (board[0][0] == mark[m]) and (board[1][1] == mark[m]) and (board[2][2] == mark[m]): # diagonal
                win = True
                break
            if (board[0][2] == mark[m]) and (board[1][1] == mark[m]) and (board[2][0] == mark[m]): # diagonal
                win = True
                break
    return win

def check_tie(board):
    nums = ['1','2','3','4','5','6','7','8','9']
    result = True
    for n in board:
        for x in n:
            for i in nums:
                if i in x:
                    result = False
    return result

def dashes():
    """Print a fancy line of dashes"""
    print("o" + 35 *'-' + "o")
    
def display(message):
    print("|{:^35s}|".format(message))
    
def main():
    # initializing game
    board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
    # select the first player randomly
    player = ['X', 'O']
    turn = randint(0, 1)

    win = False
    tie = False
    while(not win and not tie):
        # switch players
        turn = (turn + 1) % 2
        current_player = player[turn] # contains 'X' or 'O'

        clear_output()
        
        # display header
        dashes()
        display("TIC TAC TOE")
        dashes()

        # display game board
        print()
        draw(board)
        print()

        # display footer
        dashes()
        # player select a location to mark
        while True:
            location = input("|{:s} Turn, select a number (1, 9): ".format(current_player))
            if available(location, board):
                break # Only the user input loop, main loop does NOT break
            else:
                print("Selection not available!")
        dashes()

        # mark selected location with player symbol ('X' or 'O')
        mark(current_player, location, board)
        
        # check for win
        win = check_win(board)
        
        # check for tie
        tie = check_tie(board)
        

    # Display game over message after a win or a tie
    clear_output()
    
    # display header
    dashes()
    display("TIC TAC TOE")
    dashes()

    # display game board (Necessary to draw the latest selection)
    print()
    draw(board)
    print()

    # display footer
    dashes()
    display("Game Over!")
    if(tie):
        display("Tie!")
    elif(win):
        display("Winner:")
        display(current_player)
    dashes()
  

# Run the game
main()
