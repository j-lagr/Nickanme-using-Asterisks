nickname = "RON"

letter_R = [[" " for i in range (5)] for j in range (6)]
letter_O = [[" " for i in range (6)] for j in range (6)]
letter_N = [[" " for i in range (6)] for j in range (6)]


for row in range(6):
    for col in range(5):
        if col == 0 or (col == 4 and (row != 0 and row != 3)) or ((row == 0 or row == 3) and (col > 0 and col < 4)):
            letter_R[row][col]="*"

for row in range(6):
    for col in range(6):
         if ((row==0 or row==5) and (col!=0 and col!=5)) or ((col==0 or col==5) and (row!=0 and row!=5)):
             letter_O[row][col]="*"

for row in range(6):
    for col in range(6):
         if col==0 or col==5 or row==col:
             letter_N[row][col] = "*"


for i in range(6):
    for j in range (5):
        print(letter_R[i][j],end=" ")
    print(end="  ")
    for j in range (6):
        print(letter_O[i][j],end=" ")
    print(end="  ")
    for j in range (6):
        print(letter_N[i][j],end=" ")
    print()