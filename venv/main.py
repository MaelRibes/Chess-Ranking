from graph import *

inter = True

while inter:
    print("""\n=========================== Chess ranking ============================

Display the ranking according to the number of games or month by month ?
    
    1.Number of games
    2.Month by month
    3.Quit
    """)
    ans = input("What would you like to do? ")
    if ans == "1":
        graph()
        inter = False
    elif ans == "2":
        graph_month()
        inter = False
    elif ans == "3":
        print("\n Goodbye")
        ans = None
        inter = False
    else:
        print("\n Not Valid Choice Try again \n")
