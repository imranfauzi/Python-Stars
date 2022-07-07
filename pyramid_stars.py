
# Online IDE - Code Editor, Compiler, Interpreter

rows = input("Insert Odd Number > 5")
num_rows = int (rows)
if (num_rows % 2) == 0:
    print("Please insert an odd number")
else:
    if(num_rows>4):
        for i in range (0, num_rows):
            if i % 2 == 0:
                for j in range(0, i + 1):
                    print("* ", end='')
                print("\r")
        for i in range (num_rows, 0, -1):
            if i % 2 == 0:
                for j in range(0, i -1):
                    print("* ", end='')
                print("\r")
    else:
        print("Please insert number more than 5")