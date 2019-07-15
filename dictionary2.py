#keys and values dicti
import pprint
def main():
    theboard = {'topl': ' ', 'topm': ' ', 'topr':'','midl': ' ', 'midm': ' ', 'midr':' ','lowl': ' ', 'lowm': ' ', 'lowr':' '}
    firstdicti = {"size": 20, 2 : 'green'}
    boarde = printBoard(theboard)
    makeamove(boarde,theboard)
    print(firstdicti)
    for i in firstdicti.values():
        print(i)
    for i in firstdicti.keys():
        print(i)
    firstdicti.setdefault('3', 'tall')
    yes ='size' in firstdicti.keys()
    pprint.pprint(yes)
    print("what size are you?\n" + str(firstdicti.get('size',0)))
def printBoard(board):
    print(board['topl'] + '|' + board['topm']+ '|' + board['topr'])
    print('-+-+-')
    print(board['midl'] + '|' + board['midm']+ '|' + board['midr'])
    print('-+-+-')
    print(board['lowl'] + '|' + board['lowm'] + '|' + board['lowr'])
    return board
def isWinner(board):
    #if board['topr'] == "X" and board['topm'] == 'X' and board['topl'] == 'X':
    if 'X' ==  ((board['topr'] and board['topm'] and board['topl']) or (board['midr'] and board['midm'] and board['midl'])
                or (board['lowr'] and board['lowm'] and board['lowl'])or (board['topr'] and board['midm'] and board['lowl'])):
        print('player x wins')
        return True
    elif 'X' == (board['topl'] and board['midm'] and board['lowr']) :
        print('player x by diag wins')
        return True
    elif 'O' == ((board['topr'] and board['topm'] and board['topl']) or (board['midr'] and board['midm'] and board['midl']) or
               (board['lowr'] and board['lowm'] and board['lowl']) or (board['topr'] and board['midm'] and board['lowl'])
                 or (board['topl'] and board['midm'] and board['lowr'])):
        print('player o wins')
        return True
    else:
        return False
def makeamove(board, theboard):
    turn = 'X'
    for i in range(9):
        printBoard(board)
        win = isWinner(board)
        if win == True:
            break
        print(theboard)
        print('your turn ' + turn + ' move where')
        urmove = input()
        board[urmove] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    print(board)
main()