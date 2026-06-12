# patterns, and basic syntax practice

def sqaure_pattern(n):
    for i in range(n):
        for j in range(n):
             print("*", end=" ") # use end=" " for spacing and avoid newline
        print()

def right_angled_triangle(n):
    for i in range(n):
        for j in range (i):
            print(" * ", end = " ")
        print()

def pyramid(n):
    for i in range(n):
        # print n rows
        # 3 items in each line - space, print, space

        # space loop
        for j in range(n-1, i, -1):
            print(" ", end=" ")
        
        # print the stars loop
        for j in range(1,i):
            print("* ", end=" ")
        
        print()

def hollow_sqaure(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def diamond(n):
    for i in range(n): # row count is n^2
        for j in range(n-i):
            print(" ",end=" ")
        
        for j in range(i):
            print(" * ", end=" ")
        print()
    
    for i in range(n-1):
        for j in range(i+2):
            print(" ", end=" ")
        
        for j in range(n-i-1):
            print(" * ",end=" ")
        print()

def hollow_diamond_upper(n):
    for i in range(n):

        # leading spaces
        for j in range(n-i-1):
            print(" ", end="")

        if i == 0:
            print("*")
        else:
            print("*", end="")

            # gap between stars
            for j in range(2*i-1):
                print(" ", end="")

            print("*")
    
    # lower half
    for i in range(n-2, -1, -1):
        # leading spaces
        for j in range(n-i-1):
            print(" ", end="")

        if i == 0:
            print("*")
        else:
            print("*", end="")

            for j in range(2*i-1):
                print(" ", end="")

            print("*")
        

hollow_diamond_upper(5)
    