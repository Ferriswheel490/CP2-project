from move_recomender import show

def personal_portfolio():
    print("hello there and welcome to my person portfolio")
    print("""
        You get to see some of my projects that I made
          1. movie recomender
          2. 
          3. 
          4. Child's Drawing
          5. 
          6.
          7.quit
""")
    ans =  int(input("\nwhich one do you wanna see:"))
    if ans == 1:
        show()
    elif ans == 2:
        pass
    if ans == 3:
        pass
    if ans == 4:
        pass
    if ans == 5:
        pass
    if ans == 6:
        pass
    if ans == 7:
        quit("bye bye")
    else:
        print()
personal_portfolio()