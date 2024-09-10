import os
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

board = ["#"] * 10
licznik=1
while True:
  show(board)
  a=int(input("w którym miejscu chcesz postawić X  "))
  os.system("cls")
  if a<=0 or a>9:
    print("zła wartość")
  else:
    if board[a]=="#":
      board[a]="X"
      if winner(board):
        os.system("cls")
        show(board)
        print("wygrana X")
        break 
    else:
      print("nie można w tym samym miejscu")
  show(board)
  b=int(input("w którym miejscu chcesz postawić O  "))
  os.system("cls")
  if b<=0 or b>9:
    print("zła wartość")
  else:
    if board[b]=="#" :
      board[b]="O"
      if winner(board):
        os.system("cls")
        show(board)
        print("wygrana O")
        break
    else:
      print("nie można w tym samym miejscu")
