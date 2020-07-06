import random
import time
m = "---------"
moves = list(m)
i = 0
j = 0
player = ''
pla1 = ''
pla2 = ''
win1 = 0
win2 = 0
count = 0
print("Choose Heads or Tails : ")
p1 = input("player1 choice : ")
p2 = input("player2 choice : ")
time.sleep(1)
coin = random.randrange(1, 3)
if p1 == "heads" and coin == 1 or p1 == "tails" and coin == 2:
    win1 = 1
    print("Its", p1, "Player 1 you won the toss.")
elif p2 == "heads" and coin == 1 or p2 == "tails" and coin == 2:
    win2 = 1
    print("Its", p2, "Player 2 you won the toss.")
print("1 : X")
print("2 : O")
if win1 == 1:
    pla1 = input("Pick your symbol : ")
else:
    pla2 = input("Pick your symbol : ")
if pla1 == 'X' or pla1 == 'O':
    if pla1 == 'X':
        pla2 = 'O'
    if pla1 == 'O':
        pla2 = 'X'
elif pla2 == 'X' or pla2 == 'O':
    if pla2 == 'X':
        pla1 = 'O'
    if pla2 == 'O':
        pla1 = 'X'
if win1 == 1:
    print("Player 1 make your move")
    player = pla1
elif win2 == 1:
    print("Player 2 make your move")
    player = pla2
print("---------")
print("|", moves[i], moves[i + 1], moves[i + 2], "|")
print("|", moves[i + 3], moves[i + 4], moves[i + 5], "|")
print("|", moves[i + 6], moves[i + 7], moves[i + 8], "|")
print("---------")
while (j < 10):
    count += 1
    if count > 9:
        print("DRAW")
        break
    if (moves[0] == 'O' and moves[1] == 'O' and moves[2] == 'O') or \
            (moves[3] == 'O' and moves[4] == 'O' and moves[5] == 'O') or \
            (moves[6] == 'O' and moves[7] == 'O' and moves[8] == 'O') or \
            (moves[0] == 'O' and moves[3] == 'O' and moves[6] == 'O') or \
            (moves[1] == 'O' and moves[4] == 'O' and moves[7] == 'O') or \
            (moves[2] == 'O' and moves[5] == 'O' and moves[8] == 'O') or \
            (moves[2] == 'O' and moves[4] == 'O' and moves[6] == 'O') or \
            (moves[0] == 'O' and moves[4] == 'O' and moves[8] == 'O'):
        print("Player O is Winner")
        break
    elif (moves[0] == 'X' and moves[1] == 'X' and moves[2] == 'X') or \
            (moves[3] == 'X' and moves[4] == 'X' and moves[5] == 'X') or \
            (moves[6] == 'X' and moves[7] == 'X' and moves[8] == 'X') or \
            (moves[0] == 'X' and moves[3] == 'X' and moves[6] == 'X') or \
            (moves[1] == 'X' and moves[4] == 'X' and moves[7] == 'X') or \
            (moves[2] == 'X' and moves[5] == 'X' and moves[8] == 'X') or \
            (moves[2] == 'X' and moves[4] == 'X' and moves[6] == 'X') or \
            (moves[0] == 'X' and moves[4] == 'X' and moves[8] == 'X'):
        print("Player X is Winner")
        break
    pos = int(input("Choose position you want to go for between 1 to 9: ")) - 1
    if pos >= 9:
        print("No such index exist in tic tac toe board. "
              "Choose a valid option.")
        continue
    if player == pla2:
        if moves[pos] == 'X' or moves[pos] == 'O':
            print("This position is occupied."
                  "Choose else.")
            count -= 1
            continue
        moves[pos] = pla2
        print(pla2)
    else:
        if moves[pos] == 'X' or moves[pos] == 'O':
            print("This position is occupied."
                  "Choose else.")
            count -= 1
            continue
        moves[pos] = pla1
    print("---------")
    print("|", moves[i], moves[i + 1], moves[i + 2], "|")
    print("|", moves[i + 3], moves[i + 4], moves[i + 5], "|")
    print("|", moves[i + 6], moves[i + 7], moves[i + 8], "|")
    print("---------")
    if player == pla1:
        player = pla2
    elif player == pla2:
        player = pla1
    j += 1








