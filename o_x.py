import os, sys

def show(board):
  visual="""
___________________
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
"""
  for i in range(0,10):
    if(board[i]=="X" or board[i]=="O"):
      visual=visual.replace(str(i),board[i])
  print(visual)

def winner(board):
  if board[1]==board[2]==board[3]=="X" or board[1]==board[2]==board[3]=="0" :
    return True
  elif board[4]==board[5]==board[6]=="X" or board[4]==board[5]==board[6]=="O":
    return True
  elif board[7]==board[8]==board[9]=="X" or board[7]==board[8]==board[9]=="O":
    return True
  elif board[1]==board[5]==board[9]=="X" or board[1]==board[5]==board[9]=="O":
    return True
  elif board[3]==board[5]==board[7]=="X" or board[3]==board[5]==board[7]=="O":
    return True
  elif board[1]==board[4]==board[7]=="X" or board[1]==board[4]==board[7]=="O":
    return True
  elif board[2]==board[5]==board[8]=="X" or board[2]==board[5]==board[8]=="O":
    return True
  elif board[3]==board[6]==board[9]=="X" or board[3]==board[6]==board[9]=="O":
    return True
  else:
    return False

pomoc=0
board = ["#"] * 10
licznik=1
while True:
    while pomoc==0:
        show(board)
        a=int(input("w którym miejscu chcesz postawić X  "))
        os.system("cls")
    
        if a<=0 or a>9:
            print("zła wartość")
            print("wpisz ponownie")
        else:
            pomoc=1
            if board[a]=="#":
                board[a]="X"
                if winner(board):
                    os.system("cls")
                    show(board)
                    print("wygrana X")
                    sys.exit(0)
            else:
                pomoc=0
                print("nie można w tym samym miejscu")
                print("spróbuj ponownie")
    pomoc=0
    
    while pomoc==0:
        show(board)
        b=int(input("w którym miejscu chcesz postawić O  "))
        os.system("cls")
    
        if b<=0 or b>9:
            print("zła wartość")
            print("wpisz ponownie")
        else:
            pomoc=1
            if board[b]=="#" :
                board[b]="O"
                if winner(board):
                    os.system("cls")
                    show(board)
                    print("wygrana O")
                    sys.exit(0)
            else:
                pomoc=0
                print("nie można w tym samym miejscu")
                print("spróbuj ponownie")
    pomoc=0