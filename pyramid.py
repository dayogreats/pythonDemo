# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.




def p1(n):
    for row in range(0, n):
        for col in range(0, n*2):
            if row ==8 or row+col == 9 or col-row == 7:
                print("*",end = "")
            else:
                print(end = " ")
        print()

def p2(n):
    for row in range(n):
        for col in range(row +1):
            print(col +1, end="x")
        print( )

def p3(n): #reverse order
    for row in range(n):
        for col in range(row, -1, -1 ):
            print(col + 1, end=" ")
        print( )


def p3(n):
    for row in range(n):
        for col in range(row, -1, -1 ):
            print(row + 1, end=" ")
        print( )

def p4(n): #revere order
    for row in range(n):
        for col in range(row + 1):
            print(n - 1, end=" ")
        print()
def p5(n): #revere order
    for row in range(n):
        for col in range(row + 1):
            print(n - col, end=" ")
        print()
def p6(n): #revere order
    for row in range(n):
        for col in range(row, -1, -1):
            print(n - col, end=" ")
        print()


#the reserve triangle pattern

def p7(n):
    for row in range(n):
        for col in range(n - row - 1):
            print(" ", end=" ")
        for col in range(row + 1):
            print(col + 1, end=" ")
        print()

def p8(n):
    for row in range(n):
        for col in range(n - row - 1):
            print(" ", end=" ")
        for col in range(row, - 1, - 1):
            print(col + 1, end=" ")
        print()

def p9(n):
    for row in range(n):
        for col in range(n - row - 1):
            print(" ", end=" ")
        for col in range(row, - 1, - 1):
            print(row + 1, end=" ")
        print()

def p10(n):
    for row in range(n):
        for col in range(n - row - 1):
            print(" ", end=" ")
        for col in range(row, - 1, - 1):
            print(n - row, end=" ")
        print()


def pyramid(n):
    for i in range(n):
        print(" "*(n-1-i)+"* "*(i+1))

def pyramid1(n):
    for row in range(n):

        for col in range(n-row-1):
            print(end="=")

        for col in range(row + 1):
            print("*", end=" ")

        for col in range(n - row + 1):
            print("=", end="")

        print()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #p10(5)

    pyramid1(9)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
